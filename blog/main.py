from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from typing import List
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash


app = FastAPI()
models.Base.metadata.create_all(engine)


### * DataBase Connection:-----
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


####### * Blogs ########

## ? Create Blog ------

@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


## ? Delete Blog ----- 

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')
    
    blog.delete(synchronize_session=False)
    db.commit()
    
    return {'detial':'Deleted SuccessFully !!'}


##  ? Update Blog -----

@app.put('/blog-update/{id}',status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')   
     
    blog.update(request.dict(),synchronize_session=False)
    db.commit()
    return {"detail": "Updated Successfully"}


## ? Get all Blogs ------

@app.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=["Blogs"])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


## ? Get an indiviusal Blog -----

@app.get('/blog/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["Blogs"])
def get_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available.')
    return blog




####### * Users ############

## ? Create Users -------

@app.post('/create-user', tags=["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User(username=request.username,
                           email=request.email,
                           password=Hash.bcrypt(request.password)
                           )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


## ? Get all Users -------

@app.get('/users',response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK, tags=['Users'])
def all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


## ? Get user ----

@app.get('/user/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_302_FOUND, tags=['Users'])
def get_user(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user: 
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'User with the id {id} is not available.')
    return user