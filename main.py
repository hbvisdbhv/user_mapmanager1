from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine
from fastapi.templating import Jinja2Templates



models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/uploads", StaticFiles(directory="uploads"),name="uploads")


# Залежність
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=list[schemas.Author])
def read_authors(request: Request, skip: int =0, limit: int = 100, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return templates.TemplateResponse("authors.html", context={"request": request, "authors": authors})

@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@app.get("/author/{author_id}", response_model=schemas.Author)
def read_author(request: Request, author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return templates.TemplateResponse("author.html", context={"request": request, "author": db_author})



@app.get("/book/{book_id}", response_model=schemas.Author)
def read_book(request: Request, book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return templates.TemplateResponse("book.html", context={"request": request, "book": db_book})




