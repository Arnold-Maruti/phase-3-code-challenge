from lib.db.connection import CONN,CURSOR

class Article:
    def __init__(self, id, title, author_id, magazine_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def find_by_id(cls,id):
        sql="""SELECT * FROM articles WHERE id = ?"""
        rows=CURSOR.execute(sql,(id,)).fetchone()
        return rows[1] if rows else None