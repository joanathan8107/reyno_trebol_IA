from fastapi import FastAPI, HTTPException
from database import database as connection
from database import solicitud as Solicitud
from schemas import solicitudRequestModel
from database import AFINIDAD, GRIMORIO
from playhouse.shortcuts import model_to_dict

app = FastAPI()


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([Solicitud])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.post('/solicitud/')
async def Alta_Solicitud(solicitud: solicitudRequestModel):
    if solicitud.afinidad not in AFINIDAD:
        return HTTPException(400, f'Error de Datos Afinidad {AFINIDAD}')

    if solicitud.trebol is not None:
        if solicitud.trebol not in range(1, 6):
            return HTTPException(400, f'Error de Datos Trebol [1 ... 5]')

    dato = Solicitud(
        nombre=solicitud.nombre,
        apellido=solicitud.apellido,
        identificacion=solicitud.identificacion,
        edad=solicitud.edad,
        afinidad=solicitud.afinidad,
        estatus=solicitud.estatus,
        trebol=solicitud.trebol
    )
    dato.save()
    return model_to_dict(dato)


@app.get('/solicitud/id/{id}')
async def Get_Solicitud_Por_Id(id):
    data = Solicitud.select().where(Solicitud.id == id).execute()
    if not data:
        return HTTPException(404, 'Solicitud No Encontrada')
    return model_to_dict(data)

@app.get('/solicitud/identificador/{iden}')
async def Get_Solicitud_Por_Identificador(iden):
    data = Solicitud.select().where(Solicitud.identificacion == iden).execute()
    if not data:
        return HTTPException(404, 'Solicitud No Encontrada')
    return [model_to_dict(row, recurse=True) for row in data]



@app.put('/solicitud/{id}')
async def Update_Solicitud(solicitud: solicitudRequestModel, id):
    if not solicitud:
        return HTTPException(400, 'Error de Datos')
    data = Solicitud.get_by_id(id)
    if not data:
        return HTTPException(404, 'Solicitud No Encontrada')
    Solicitud.update(
        nombre=solicitud.nombre,
        apellido=solicitud.apellido,
        identificacion=solicitud.identificacion,
        edad=solicitud.edad,
        afinidad=solicitud.afinidad,
        estatus=solicitud.estatus,
        trebol=solicitud.trebol
    ).where(Solicitud.id == id).execute()
    return solicitud


@app.patch('/solicitud/{id}{estado}')
async def Update_Estado(id, estado):
    data = Solicitud.get_by_id(id)
    if not data:
        return HTTPException(404, 'Solicitud No Encontrada')
    # Solicitud.update(estatus=estado).where(Solicitud.id == id).execute()
    data.estatus = estado
    data.save()
    return {"message": "Estado Actualizado"}


@app.get('/solicitud/')
async def Get_Solicitudes():
    return [model_to_dict(data, recurse=True) for data in Solicitud.select().execute()]


@app.get('/solicitud/grimorios/')
async def Get_Grimorios():
    data = Solicitud.select().where(Solicitud.estatus == 1).execute()
    response = []
    for row in data:
        regis = {}
        regis["nombre"] = row.nombre
        regis["apellido"] = row.apellido
        regis["identificacion"] = row.identificacion
        regis["edad"] = row.edad
        regis["afinidad"] = row.afinidad
        regis["grimorio"] = GRIMORIO[str(row.trebol)]
        response.append(regis)
    return response


@app.delete('/solicitud/{id}')
async def Delete_Solicitud(id):
    data = Solicitud.get_by_id(id);
    if not data:
        return HTTPException(404, 'Solicitud No Encontrada')
    data.delete_instance()
    return model_to_dict(data)