from lib.db.connection import CONN,CURSOR

class Magazine:
      all={}
      def __init__(self,name, category,id=None):
           self.id = id
           self.name = name
           self.category = category

      def save(self):
            sql="""
            INSERT INTO magazines(name,category) VALUES(?,?)
            """
            CURSOR.execute(sql,(self.name,self.category))
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self

      @classmethod
      def find_by_id(cls, id):
            sql="""SELECT * FROM magazines WHERE id = ?"""
            rows=CURSOR.execute(sql,(id,)).fetchone()
            return rows[1] if rows else None
        
      def articles(self):
            sql="""SELECT * FROM articles WHERE magazine_id = ?"""
            rows=CURSOR.execute(sql,(self.id,)).fetchall()
            return [row[1] for row in rows]
        
      def article_titles(self):
            sql="""SELECT title FROM articles WHERE magazine_id = ?"""
            rows=CURSOR.execute(sql,(self.id,)).fetchall()
            return [row[1]for row in rows]
        
      def contributing_authors(self):
            sql="""
            SELECT au.*, COUNT(*) as article_count FROM authors au
            JOIN articles ar ON ar.author_id = au.id
            WHERE ar.magazine_id = ?
            GROUP BY au.id
            HAVING COUNT(*) > 2"""
            rows=CURSOR.execute(sql,(self.id,)).fetchall()
            return [row[1] for row in rows]
        
      def article_counts(self):
            sql="""
            SELECT m.id, m.name, COUNT(a.id) AS article_count
            FROM magazines m
            LEFT JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id, m.name
            ORDER BY article_count DESC"""
            results=CURSOR.execute(sql).fetchall()
            return results
        
        