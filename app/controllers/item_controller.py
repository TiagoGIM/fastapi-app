from fastapi import APIRouter, HTTPException
from app.services.item_service import ItemService
from app.model.item import Item

router = APIRouter()
item_service = ItemService()

@router.post("/items/")
def create_item(item: Item):
    return item_service.create_item(item)

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return item_service.read_item(item_id)

@router.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return item_service.read_items(skip, limit)

@router.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    return item_service.update_item(item_id, updated_item)

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    return item_service.delete_item(item_id)
