# 1. ベースイメージ（軽量なslim版を使用）
FROM python:3.11-slim

# 2. 作業ディレクトリの設定
WORKDIR /app

# 3. 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. ソースコードのコピー
COPY main.py .

# 5. ポート8000を公開
EXPOSE 8000

# 6. アプリケーションの起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]