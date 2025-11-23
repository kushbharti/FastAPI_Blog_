from fastapi import APIRouter, Depends, status
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/v2',
    tags=['Blogs']
)

get_db = database.get_db


####### * Blogs ########

## ? Get all Blogs ------

@router.get('/get-all-blogs', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):

    return blog.get_blogs(db)

## ? Create Blog ------

@router.post('/create-blog', status_code=status.HTTP_201_CREATED )
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    
    return blog.create_blog(request, db)


## ? Delete Blog ----- 

@router.delete('/delete-blog/{id}', status_code=status.HTTP_204_NO_CONTENT )
def delete_blog(id: int, db: Session = Depends(get_db)):
    
    return blog.destroy(id, db)


##  ? Update Blog -----

@router.put('/update-blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db) ):
    
    return blog.update_blog(id, request, db)


## ? Get an indiviusal Blog -----

@router.get('/get-blog/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog )
def get_blog(id: int, db: Session = Depends(get_db)):
    
    return blog.get_a_blog(id, db)



