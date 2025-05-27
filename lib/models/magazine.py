from lib.db.connection import CONN,CURSOR

class Magazine:
        def __init__(self, id, name, category):
           self.id = id
           self.name = name
           self.category = category

        @classmethod
        def find_by_id(cls, id):
              sql="""SELECT * FROM magazines WHERE id = ?"""
              rows=CURSOR.execute(sql,(id,)).fetchone
              return rows[1] if rows else None
        
        def articles(self):
              sql="""SELECT * FROM articles WHERE magazine_id = ?"""
              return CURSOR.execute(sql,(self.id,)).fetchall()
        
        def article_titles(self):
              sql="""SELECT title FROM articles WHERE magazine_id = ?"""
              rows=CURSOR.execute(sql,(self.id,)).fetchall()
              return [row["title"]for row in rows]
        
        def contributing_authors(self):
            sql="""
            SELECT au.*, COUNT(*) as article_count FROM authors au
            JOIN articles ar ON ar.author_id = au.id
            WHERE ar.magazine_id = ?
            GROUP BY au.id
            HAVING COUNT(*) > 2"""
            return CURSOR.execute(sql,(self.id,)).fetchall()
        
        def article_counts(cls):
            sql="""
            SELECT m.id, m.name, COUNT(a.id) AS article_count
            FROM magazines m
            LEFT JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id, m.name
            ORDER BY article_count DESC"""
            results=CURSOR.execute(sql).fetchall()
            return results
        
        