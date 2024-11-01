# app/dify_client/client.py
import requests

class DifyClient:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def get_response(self, message):
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json={'query': message}
            )
            response.raise_for_status()
            return response.json()['answer']
        except Exception as e:
            print(f"Error calling Dify API: {e}")
            return "申し訳ありません。現在応答を生成できません。"
