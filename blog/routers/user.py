from fastapi import APIRouter, Depends, status
from blog import schemas, database
from typing import List
from sqlalchemy.orm import Session
from blog.repository import user


router = APIRouter(
    prefix='/v1',
    tags=['Users']
)

get_db = database.get_db


####### * Users ############

## ? Get all Users -------

@router.get('/get-all-users', response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    
    return user.get_all(db)


## ? Create Users -------

@router.post('/create-user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
   return user.create(request, db)


## ? Get user ----

@router.get('/get-user/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_302_FOUND)
def get_user(id: int, db: Session = Depends(get_db)):
    
   return user.get(id, db)

