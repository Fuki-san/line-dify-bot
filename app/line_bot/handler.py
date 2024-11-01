
# app/line_bot/handler.py
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from ..dify_client.client import DifyClient
from ..config import Config

line_bot_api = LineBotApi(Config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(Config.LINE_CHANNEL_SECRET)
dify_client = DifyClient(Config.DIFY_API_KEY, Config.DIFY_API_URL)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Difyからの応答を取得
    response = dify_client.get_response(event.message.text)
    
    # LINEに応答を送信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )
