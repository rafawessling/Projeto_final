from source.schemas.address_schema import Address
from pycep_correios import get_address_from_cep , WebService

def adress(cep: Address ):
    adress = get_address_from_cep({cep}, webservice=WebService.CORREIOS)
    return adress

def cep_validation(cep: Address):
    if cep < 9 or cep > 9:
        raise TypeError("CEP inválido!")

