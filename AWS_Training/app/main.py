import os
from fastapi import FastAPI, HTTPException
import google.generativeai as genai
from dotenv import load_dotenv

# .envファイルがある場合に読み込む（ローカル開発用）
load_dotenv()

app = FastAPI()

# Geminiの初期設定
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 1. ヘルスチェック用エンドポイント（AWS ELBで必須になります）
@app.get("/")
def read_root():
    return {"status": "ok", "message": "Gemini API Wrapper is running"}

# 2. チャット用エンドポイント
@app.get("/chat")
async def chat(prompt: str):
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
    
    try:
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))