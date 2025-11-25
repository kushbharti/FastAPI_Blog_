from blog import schemas, models
from sqlalchemy.orm import Session
from fastapi import status, HTTPException


def get_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs



def create_blog(request: schemas.Blog, db: Session):
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


def destroy(id: int, db: Session ):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')
    
    blog.delete(synchronize_session=False)
    db.commit()
    
    return {'detial':'Deleted SuccessFully !!'}



def update_blog(id: int, request: schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')   
     
    blog.update(request.dict(),synchronize_session=False)
    db.commit()
    return {"detail": "Updated Successfully"}



def get_a_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')
    return blog