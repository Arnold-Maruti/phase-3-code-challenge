from lib.db.connection import CONN,CURSOR

class Author:
    all={}
    def __init__(self,id,name):
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
        INSERT INTO authors(id,name) VALUES(?,?)
        """
        CURSOR.execute(sql,(self.id,self.name))
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
        rows=CURSOR.execute(sql,(self.id,))
        return [row[1] for row in rows]
    
    def magazines(self):
        sql="""SELECT DISTINCT m.* FROM magazines m
        JOIN articles a on a.magazine_id=m.id
        WHERE a.author_id=?"""
        data=CURSOR.execute(sql,(self.id,)).fetchall()
        return [dats[1] for dats in data]
    
    @classmethod
    def authors_for_magazine(cls,magazine_id):
        sql="""            
        SELECT DISTINCT a.* FROM authors a
        JOIN articles ar ON a.id = ar.author_id
        WHERE ar.magazine_id = ?
        """
        datas=CURSOR.execute(sql,(magazine_id,)).fetchall()
        return [data[1]for data in datas]
    
    @classmethod
    def magazines_with_multiple_authors(cls):
        sql="""
        SELECT m.*
        FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
        HAVING COUNT(DISTINCT a.author_id) >= 2
        """
        rows=CURSOR.execute(sql).fetchall()
        return [rows[1]for row in rows]
    


    




    

    

