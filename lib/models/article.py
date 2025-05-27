from lib.db.connection import CONN,CURSOR

class Article:
    all={}
    def __init__(self,title, author_id, magazine_id,id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        sql="""
        INSERT INTO articles(title,author_id,magazine_id) VALUES(?,?,?)
        """
        CURSOR.execute(sql,(self.title,self.author_id,self.magazine_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def find_by_id(cls,id):
        sql="""SELECT * FROM articles WHERE id = ?"""
        rows=CURSOR.execute(sql,(id,)).fetchone()
        return rows[1] if rows else None