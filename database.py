from peewee import *

database = MySQLDatabase(
    database='reynoTrebolIA',
    user='chava', password='chko+P2021',
    host='enebro.myddns.me', port=33060
)

AFINIDAD = ("Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra")
GRIMORIO = {"1":"Sinceridad", "2":"Esperanza", "3":"Amor", "4":"Buena Fortuna", "5":"Desesperación"}

class solicitud(Model):
    # Nombre del Colicitante
    # Apellido del Solicitante
    # Identificación del Solicitante
    # Edad del Colicitante
    # Afinidad del Solicitante [Catologo de Afinidad]
    # Define el estado de la Solicitud [1 --> Aprobada, 0 --> Capturada]
    # Define el Trebol asignado Valores[1 ... 5]

    nombre = CharField(max_length=20)
    apellido = CharField(max_length=20)
    identificacion = CharField(max_length=10, unique=True)
    edad = IntegerField()
    afinidad = CharField(max_length=10)
    estatus = IntegerField(default=0, null=True)
    trebol = IntegerField(null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}\n" \
               f"Identificación: {self.identificacion} Edad: {self.edad}\n" \
               f"Afinidad: {self.afinidad}\n" \
               f"Grimorio: {self.grimorio}";

    class Meta:
        database = database
        table_name = 'reynoTrebolIA'
