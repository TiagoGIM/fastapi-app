from ..repositories.item_repository import ItemRepository
from ..model.item import Item

class ItemService:
    def __init__(self):
        self.item_repository = ItemRepository()

    def create_item(self, item: Item):
        return self.item_repository.create_item(item)

    def read_item(self, item_id: int):
        return self.item_repository.read_item(item_id)

    def read_items(self, skip: int = 0, limit: int = 10):
        return self.item_repository.read_items(skip, limit)

    def update_item(self, item_id: int, updated_item: Item):
        return self.item_repository.update_item(item_id, updated_item)

    def delete_item(self, item_id: int):
        return self.item_repository.delete_item(item_id)
