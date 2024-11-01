
# app/routes/webhook.py
from flask import Blueprint, request, abort
from ..line_bot.handler import handler, handle_message
from linebot.exceptions import InvalidSignatureError

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route("/webhook", methods=['POST'])
def webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'