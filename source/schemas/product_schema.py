from typing import Optional
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=80, description="Nome do produto",)
    description: str = Field(..., min_length=3, description="Descricão do produto")
    code: str = Field(..., description="Código do produto")
    price: float = Field(..., ge=0.01, description="Valor do produto")
    image: str = Field(..., description="Imagem do produto")
    stock: int = Field(..., ge=1, description="Quantidade em estoque")
    brand: Optional[str] = Field(None, min_length=1, max_length=30, description="Marca (opcional) do produto")
    color: Optional[str] = Field(None, min_length=3, max_length=50, description="Cor (opcional) do produto")
    material: Optional[str] = Field(None, min_length=3, max_length=100, description="Material (opcional) do produto")

class ProductUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=80, description="Nome (opcional) do produto",)
    description: Optional[str] = Field(None, min_length=3, description="Descricão (opcional) do produto")
    code: str = Field(..., description="Código do produto")
    price: Optional[float] = Field(None, ge=0.01, description="Valor (opcional) do produto")
    image: Optional[str] = Field(None, description="Imagem (opcional) do produto")
    stock: Optional[int] = Field(None, ge=1, description="Quantidade (opcional) em estoque")
    brand: Optional[str] = Field(None, min_length=1, max_length=30, description="Marca (opcional) do produto")
    color: Optional[str] = Field(None, min_length=3, max_length=50, description="Cor (opcional) do produto")
    material: Optional[str] = Field(None, min_length=3, max_length=100, description="Material (opcional) do produto")