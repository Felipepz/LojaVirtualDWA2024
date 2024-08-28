from fastapi import APIRouter

from dtos.novo_produto_dto import NovoProdutoDTO
from repositories.produto_repo import ProdutoRepo


router = APIRouter(prefix="/manager")


@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.get("/inseir_produto")
async def inseir_produto(produtos: NovoProdutoDTO):
    return produtos