from pydantic import BaseModel
from model.endereco import Endereco

class EnderecoSchema(BaseModel):
    """ Define quais dados devem ser fornecidos para um novo endereço ser inserido.
    """
    cep: str
    logradouro: str
    complemento: str
    unidade: str
    bairro: str
    localidade: str
    uf: str
    ibge: str
    gia: str
    ddd: str
    siafi: str

class EnderecoViewSchema(BaseModel):
    """ Define como um endereço será retornado.
    """
    cep: str
    logradouro: str
    complemento: str
    unidade: str
    bairro: str
    localidade: str
    uf: str
    ibge: str
    gia: str
    ddd: str
    siafi: str

class EnderecoBuscaSchema(BaseModel):
    """ Define qual dado deve ser fornecido para que seja buscado um endereço na API externa. A busca será
        feita apenas com base no CEP do endereço que é formado por 9 caracteres.
    """

    cep: str = "01001-000"

class EnderecoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    message: str
    cep: str

def apresenta_endereco(endereco: Endereco):
    """ Retorna uma representação de um endereço.
    """
    return {
        "cep": endereco.cep,
        "logradouro": endereco.logradouro,
        "complemento": endereco.complemento,
        "unidade": endereco.unidade,
        "bairro": endereco.bairro,
        "localidade": endereco.localidade,
        "uf": endereco.uf,
        "ibge": endereco.ibge,
        "gia": endereco.gia,
        "ddd": endereco.ddd,
        "siafi": endereco.siafi
    }
