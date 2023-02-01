from typing import Optional

from pydantic import BaseModel


class solicitudRequestModel(BaseModel):
    nombre: str                     # Nombre del Colicitante
    apellido: str                   # Apellido del Solicitante
    identificacion: str             # Identificación del Solicitante
    edad: int                       # Edad del Colicitante
    afinidad: Optional[str] = None  # Afinidad del Solicitante [Catologo de Afinidad]
    estatus: Optional[int] = 0      # Define el estado de la Solicitud [1 --> Aprobada, 0 --> Capturada]
    trebol: Optional[int] = 0       # Define el Trebol asignado Valores[1 ... 5]