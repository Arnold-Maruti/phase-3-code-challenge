from lib.db.connection import CONN,CURSOR

class Author:
    all={}
    def __init__(self,name,id=None):
        self.id=id
        self.name=name

    @classmethod
    def find_by_id(cls,id):
        sql="""
        SELECT * 
        FROM authors WHERE id=?
        """
        row=CURSOR.execute(sql,(id,)).fetchone()
        return row[1] if row else None
    
    def save(self):
        sql="""
        INSERT INTO authors(name) VALUES(?)
        """
        CURSOR.execute(sql,(self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @property
    def id(self):
        return self._id
    @id.setter
    def id (self,id):
        if isinstance(id,int):
            self._id=id
        else:
            raise ValueError("id attribute is not an integer")
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self._name=name
        else:
            raise ValueError("name entered is not a string")
    
    def articles(self):
        sql="""SELECT * FROM articles WHERE author_id=?"""
        rows=CURSOR.execute(sql,(self.id,)).fetchall()
        return [row[1] for row in rows]
    
    def magazines(self):
        sql="""SELECT DISTINCT m.* FROM magazines m
        JOIN articles a on a.magazine_id=m.id
        WHERE a.author_id=?"""
        data=CURSOR.execute(sql,(self.id,)).fetchall()
        return [dats[1] for dats in data]
    
    def add_article(self,magazine,title):
        sql="""
        INSERT INTO articles (title, author_id, magazine_id)
        VALUES (?, ?, ?)
        """
        CURSOR.execute(sql,(title,self.id,magazine.id))
        CONN.commit()

    def topic_areas(self):
        sql="""
        SELECT DISTINCT m.category FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        WHERE a.author_id = ?
        """
        rows=CURSOR.execute(sql,(self.id,)).fetchall()
        return [row[0] for row in rows]
    
    @classmethod
    def top_author(cls):
        sql="""
        SELECT a.*, COUNT(ar.id) AS article_count
        FROM authors a
        JOIN articles ar ON a.id = ar.author_id
        GROUP BY a.id
        ORDER BY article_count DESC
        LIMIT 1
        """
        rows=CURSOR.execute(sql).fetchone()
        return rows[1] if rows else None
    

    


    




    

    

