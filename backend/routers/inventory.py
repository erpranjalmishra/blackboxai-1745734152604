from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend import schemas, models, crud, auth
from backend.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.InventoryOut)
def create_inventory_item(item: schemas.InventoryCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    return crud.create_inventory(db, item)

@router.get("/", response_model=List[schemas.InventoryOut])
def read_inventory_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    return crud.get_inventory(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=schemas.InventoryOut)
def read_inventory_item(item_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    db_item = crud.get_inventory_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.InventoryOut)
def update_inventory_item(item_id: int, item: schemas.InventoryUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    db_item = crud.update_inventory(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return db_item

@router.delete("/{item_id}", response_model=schemas.InventoryOut)
def delete_inventory_item(item_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_active_user)):
    db_item = crud.delete_inventory(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return db_item
