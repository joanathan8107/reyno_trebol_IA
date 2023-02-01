# reyno_trebol_IA
ia test python

Caso Práctico:

En el Reino del Trébol, El Rey Mago requiere diseñar un sistema para la academia de magia; este debe realizar el registro de solicitud del estudiante y la asignación aleatoria de su Grimorio. El nivel de estos Grimorios está categorizado por el tipo de trébol en la portada:

▪ Sinceridad – Trébol de 1 hoja.

▪ Esperanza – Trébol de 2 hojas.

▪ Amor – Trébol de 3 hojas.

▪ Buena Fortuna - Trébol de 4 hojas. 

▪ Desesperación – Trébol de 5 hojas.

Los estudiantes tendrán una de las siguientes afinidades de magia:

▪ Oscuridad 

▪ Luz

▪ Fuego

▪ Agua

▪ Viento 

▪ Tierra


Instrucciones:

Para este requerimiento se requiere exponer un API Rest, construida en Python.

Deben exponerse los endpoints necesarios para soportar las siguientes operaciones:

▪ Enviar solicitud de ingreso.

▪ Actualizar solicitud de ingreso.

▪ Actualizar estatus de solicitud.

▪ Consultar todas las solicitudes.

▪ Consultar asignaciones de Grimorios. 

▪ Eliminar solicitud de ingreso.


Una vez aprobada la solicitud se debe realizar la auto asignación de Grimorio y de portada. Las solicitudes de ingreso deben indicar como mínimo los siguientes datos del aspirante:

▪ Nombre (solo letras, máximo 20 caracteres).

▪ Apellido (solo letras, máximo 20 caracteres).

▪ Identificación (números y letras, máximo 10 caracteres). 

▪ Edad (solo números, 2 dígitos).

▪ Afinidad Mágica (mencionadas anteriormente).


Al incumplir cualquiera de estos criterios automáticamente la solicitud queda rechazada y no se debe asignar Grimorio.


ESTRUCTURA DEL CÓDIGO

database.py 

Contiene la estructura y datos de conexion a una base datos, para este caso MySQL, la cual puede modificarse, esto lo hace mediante el uso de la libreria ORM peewee.
Este debe modificarse con los datos del repositorio de datos a utilizar:

  database='reynoTrebolIA',
  user='root', password='password',
  host='localhost', port=3306


schemas.py

Contiene la estructura del modelo de datos que se utilizan para transporte de datos a traves de peticiones tipo Request.
Implementa la libreria pydantic.

main.py

Mediante la libreria fastAPI, y el servidor uvicorn, este archivo contiene el código de las peticiones tipo Request, del ejercicio:

▪ Enviar solicitud de ingreso.

post('/solicitud/')


▪ Actualizar solicitud de ingreso.

put('/solicitud/{id}')


▪ Actualizar estatus de solicitud.

patch('/solicitud/{id}{estado}')


▪ Consultar todas las solicitudes.

get('/solicitud/')

get('/solicitud/id/{id}')

get('/solicitud/identificador/{iden}')


▪ Consultar asignaciones de Grimorios. 

get('/solicitud/grimorios/')


▪ Eliminar solicitud de ingreso.

delete('/solicitud/{id}')



requirements.txt

Este archivo contiene el listado de librerias necesarias para ejecutar el ejercicio.















