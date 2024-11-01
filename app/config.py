# app/config.py 設定ファイル
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
    DIFY_API_KEY = os.getenv('DIFY_API_KEY')
    DIFY_API_URL = os.getenv('DIFY_API_URL')