from pydantic import BaseModel, field_validator
from util.validators import *  # Importa os validadores personalizados


class NovaCategoriaDto(BaseModel):
    nome: str
    descricao: str

    @field_validator("nome")
    def validar_nome(cls, v):
        """Valida o nome da categoria (tamanho entre 2 e 128 caracteres)."""
        msg = is_size_between(v, "Nome", 2, 128)
        if msg: 
            raise ValueError(msg)
        return v

    @field_validator("descricao")
    def validar_descricao(cls, v):
        """Valida a descrição da categoria (não vazia e tamanho entre 16 e 1024 caracteres)."""
        msg = is_not_empty(v, "Descrição")
        msg = msg or is_size_between(v, "Descrição", 16, 1024)
        if msg: 
            raise ValueError(msg)
        return v
