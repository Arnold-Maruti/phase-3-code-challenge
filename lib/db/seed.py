from lib.db.connection import CONN,CURSOR

def seed():
    CURSOR.execute("INSERT INTO authors (name) VALUES ('Alice')")
    CURSOR.execute("INSERT INTO authors (name) VALUES ('Bob')")

    CURSOR.execute("INSERT INTO magazines (name, category) VALUES ('Tech Monthly', 'Technology')")
    CURSOR.execute("INSERT INTO magazines (name, category) VALUES ('Nature Weekly', 'Science')")

    CURSOR.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI Revolution', 1, 1)")
    CURSOR.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Climate Change', 2, 2)")

    CONN.commit()

    
