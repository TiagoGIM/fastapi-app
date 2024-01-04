from app.model.item import Item

class ItemRepository:
    items = []

    def create_item(self, item: Item):
        self.items.append(item)
        return item

    def read_item(self, item_id: int):
        if item_id < 0 or item_id >= len(self.items):
            return None
        return self.items[item_id]

    def read_items(self, skip: int = 0, limit: int = 10):
        return self.items[skip: skip + limit]

    def update_item(self, item_id: int, updated_item: Item):
        if item_id < 0 or item_id >= len(self.items):
            return None
        self.items[item_id] = updated_item
        return updated_item

    def delete_item(self, item_id: int):
        if item_id < 0 or item_id >= len(self.items):
            return None
        deleted_item = self.items.pop(item_id)
        return {"message": "Item deleted successfully", "deleted_item": deleted_item}
