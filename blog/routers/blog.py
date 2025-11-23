from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/v2',
    tags=['Blogs']
)

get_db = database.get_db


####### * Blogs ########

## ? Get all Blogs ------

@router.get('/get-all-blogs', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

## ? Create Blog ------

@router.post('/create-blog', status_code=status.HTTP_201_CREATED )
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')
    
    new_blog = models.Blog(
        title=request.title, 
        body=request.body,
        user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


## ? Delete Blog ----- 

@router.delete('/delete-blog/{id}', status_code=status.HTTP_204_NO_CONTENT )
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')
    
    blog.delete(synchronize_session=False)
    db.commit()
    
    return {'detial':'Deleted SuccessFully !!'}


##  ? Update Blog -----

@router.put('/update-blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db) ):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')   
     
    blog.update(request.dict(),synchronize_session=False)
    db.commit()
    return {"detail": "Updated Successfully"}


## ? Get an indiviusal Blog -----

@router.get('/get-blog/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog )
def get_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')
    return blog



