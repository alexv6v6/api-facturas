from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos
class Factura(BaseModel):
    id: int
    cliente: str
    total: float

# "Base de datos" en memoria (lista)
facturas = [
    Factura(id=1, cliente="Empresa X", total=120000.0),
    Factura(id=2, cliente="Empresa Y", total=300000.0)
]

# Endpoint para listar todas las facturas
@app.get("/facturas", response_model=List[Factura])
def listar_facturas():
    return facturas

# Endpoint para consultar una factura por ID
@app.get("/facturas/{factura_id}", response_model=Factura)
def obtener_factura(factura_id: int):
    for factura in facturas:
        if factura.id == factura_id:
            return factura
    return {"error": "Factura no encontrada"}

# Endpoint para crear una nueva factura
@app.post("/facturas", response_model=Factura)
def crear_factura(factura: Factura):
    facturas.append(factura)
    return factura
