## プロジェクト構造

project-root/
├── .env.example              # 環境変数のテンプレート
├── .gitignore               # Gitの除外ファイル設定
├── Dockerfile               # Dockerコンテナ設定
├── docker-compose.yml       # Docker Compose設定
├── requirements.txt         # Pythonパッケージ依存関係
├── app/
│   ├── __init__.py         # Flaskアプリケーション初期化
│   ├── config.py           # 設定ファイル
│   ├── line_bot/
│   │   ├── __init__.py
│   │   ├── handler.py      # LINEメッセージハンドラー
│   │   └── models.py       # LINEメッセージモデル
│   ├── dify_client/
│   │   ├── __init__.py
│   │   └── client.py       # Dify API クライアント
│   └── routes/
│       ├── __init__.py
│       └── webhook.py      # Webhookエンドポイント
└── run.py                  # アプリケーション起動スクリプト