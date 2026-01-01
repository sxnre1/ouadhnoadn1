import duckdb

def init_db():
      con = duckdb.connect("database.duckdb")
      cur = con.cursor()

      cur.execute("""
            CREATE TABLE IF NOT EXISTS licenses (
                  key TEXT PRIMARY KEY,
                  length INTEGER
            );
      """)
      
      cur.execute("""
            CREATE TABLE IF NOT EXISTS guilds (
                  id INTEGER PRIMARY KEY,
                  token TEXT,
                  expiredate TEXT,
                  link TEXT
            );
      """)

      cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                  id TEXT,
                  token TEXT,
                  guild_id INTEGER
            );
      """)

      con.commit()
      con.close()
      print("DuckDB 초기화 완료")

if __name__ == "__main__":
      init_db()