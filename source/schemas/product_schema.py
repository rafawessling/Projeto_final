
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
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Mop Perfect Pro Giratório 360 com 3 Refis Esfregão e Balde Cesto Inox",
                "description": "Com uma concepção inovadora, baseada na teoria da centrifugação, apresenta um excelente poder de limpeza e 100% de centrifugação. Com um fantástico dispositivo de centrifugação você pode controlar o percentual de umidade do mop facilmente. Produzido em microfibra, o mop apresenta um grande poder de absorção de poeira ou água com secagem fácil, limpando de forma segura e eficiente. Seu elegante design faz com que gire 360 graus e permite chegar em qualquer canto onde antes não era possível.\nVantagens: centrifuga inox removível; rolha de vedação para facilitar o escoamento da agua; alça para carregamento mais resistente; eixo interno para facilitar a lavagem do refil; cabo com inclinação de 180°; cabo com sistema de trava on/off para regulagem de altura e função giratória; remove rapidamente o excesso de agua; material, mais resistente e durável dentre todos da categoria.\nDimensões:\nCabo: Altura max: 1,60m;\nBalde: Altura: 24 cm; Largura: 28 cm; Comprimento: 46 cm.",
                "code": "123456",
                "price": 169.89,
                "image": "https://a-static.mlcdn.com.br/800x560/balde-mop-pro-esfregao-com-cesto-inox-cabo-160-metros-com-3-refis-1-microfibra-1-limpeza-po-1-limpeza-pesada-perfect/gahe/5916911504/e594d771b7140096b37d35479097d3e1.jpeg",
                "stock": 5,
                "brand": "MOP",
                "color": "Azul",
                "material": "Balde plástico com cesto inox, cabo inox e refis de microfibra."
            }
        }

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
    
    class Config:
        schema_extra = {
            "example": {
                "code": "123456",
                "stock": 12
            }
        }