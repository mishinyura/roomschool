from app.repositories.base_crud import BaseCrud
from app.models import AddressModel


class AddressCrud(BaseCrud):
    def __init__(self):
        super().__init__(AddressModel)



address_crud = AddressCrud()