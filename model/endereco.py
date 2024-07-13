import urllib.request
import json
import logging

log = logging.getLogger(__name__)

class Endereco:
    def __init__(self, cep, logradouro, complemento, unidade, bairro, localidade, uf, ibge, gia, ddd, siafi):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.unidade = unidade
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi
   
def busca_endereco(cep):
    try:
        log.info(f"Obtendo endereço para CEP: {cep}")
        with urllib.request.urlopen(f"https://viacep.com.br/ws/{cep}/json/") as url:
            data = json.loads(url.read().decode())

            if "erro" not in data:
                return Endereco(
                    cep = data.get("cep", ""),
                    logradouro = data.get("logradouro", ""),
                    complemento = data.get("complemento", ""),
                    unidade = data.get("unidade", ""),
                    bairro = data.get("bairro", ""),
                    localidade = data.get("localidade", ""),
                    uf = data.get("uf", ""),
                    ibge = data.get("ibge", ""),
                    gia = data.get("gia", ""),
                    ddd = data.get("ddd", ""),
                    siafi = data.get("siafi", "")
                )
            else:
                return None
            
    except Exception as e:
        log.error(f"Erro ao obter endereço do CEP: {cep}. Erro: {e}")
        raise ValueError(f"Erro ao obter endereço do CEP: {cep}. Erro: {e}")
