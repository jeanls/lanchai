from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class Piada(BaseModel):
    """piada para contar ao usuário"""
    introducao: str = Field(description="a introdução da piada")
    punchline: str = Field(description="a conclusão da piada")
    avaliacao: Optional[int] = Field(description='o quao engraçada a piada é')


class AvaliacaoReview(BaseModel):
    """avalia review do cliente"""
    presente: bool = Field(description='verdadeiro se foi presente e false se não foi')
    dias_entrega: int = Field(description='quantos dias para entrega do produto')
    percepcao_valor: list[str] = Field(description='extraia qualquer frase sobre o valor ou preço do produto. retorne '
                                                   'uma lista')
