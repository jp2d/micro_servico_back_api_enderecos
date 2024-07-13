from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model.endereco import busca_endereco
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API Endereços", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
endereco_tag = Tag(name="Endereço", description="Visualização de endereço de api externa")


@app.get('/', tags=[home_tag])
def home():
    
    return redirect('/openapi')


@app.get('/get_endereco', tags=[endereco_tag],
         responses={"200": EnderecoViewSchema, "404": ErrorSchema})
def get_endereco(query: EnderecoBuscaSchema):
    """Faz a busca por um Endereço a partir do CEP

    Retorna uma representação do endereço cadastrado.
    """
    cep = query.cep
    logger.debug(f"Coletando dados sobre endereço com CEP {cep}")
    
    _endereco = busca_endereco(cep)

    if not _endereco:
        error_msg = "Endereço não encontrado :/"
        logger.warning(f"Erro ao buscar endereço com CEP '{cep}', {error_msg}")

        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Endereço encontrado: '{_endereco.logradouro}'")
        
        return apresenta_endereco(_endereco), 200