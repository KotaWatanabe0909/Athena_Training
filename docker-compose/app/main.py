from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    # docker-compose.ymlで指定するサービス名「db」で接続可能
    conn = psycopg2.connect(
        host='db',
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visits (count serial PRIMARY KEY);')
    
    # データを挿入
    cur.execute('INSERT INTO visits DEFAULT VALUES;')
    
    # 【重要】ここを追加！ これがないとリロードしてもデータが残りません
    conn.commit() 
    
    cur.execute('SELECT COUNT(*) FROM visits;')
    count = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    return f"あなたは {count} 番目の訪問者です！"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)