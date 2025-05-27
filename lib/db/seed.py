from lib.db.connection import CONN,CURSOR

def seed():
    CURSOR.execute("INSERT INTO authors (name) VALUES ('Alice')")
    CURSOR.execute("INSERT INTO authors (name) VALUES ('Bob')")

    CURSOR.execute("INSERT INTO magazines (name, category) VALUES ('Tech Monthly', 'Technology')")
    CURSOR.execute("INSERT INTO magazines (name, category) VALUES ('Nature Weekly', 'Science')")

    CURSOR.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI Revolution', 1, 1)")
    CURSOR.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Climate Change', 2, 2)")

    CONN.commit()

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
    
    @classmethod
    def article_counts_by_magazine(cls):
        sql="""
        SELECT m.id, m.name, m.category, COUNT(a.id) AS article_count
        FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
        """
        rows=CURSOR.execute(sql).fetchall
        return [dict(row)for row in rows]
    
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