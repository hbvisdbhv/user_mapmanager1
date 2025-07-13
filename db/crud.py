from sqlalchemy.orm import Session
from . import models, schemas


#def get_department(db: Session, department_id: int):
    #return db.query(models.Department).filter(models.Department.id == department_id).first()
def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()



def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
    name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author



#def create_playlist(db: Session, name: str, user_id: int):
 #   playlist = Playlist(name=name, owner_id=user_id)
  #  db.add(playlist)
   # db.commit()
    #db.refresh(playlist)
    #return playlist

#def get_playlist(db: Session, playlist_id: int):
    return db.query(Playlist).filter(Playlist.id == playlist_id).first()





def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()



def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
    name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


