### All code has been created by claude.ai.<br>全てのコードがclaude.aiで作成されたものです。
### All Issues and Pull requests will also be posted to claude.ai.<br>IssuesやPull requestsに関しても全てclaude.aiに転載します。

# Discord Translator Bot

### This project is a multilingual Discord translation bot that provides speech recognition, translation, and text-to-speech functionality.<br>このプロジェクトは、多言語対応のDiscord翻訳ボットです。音声認識、翻訳、テキスト読み上げ機能を提供します。

# Setup Instructions<br>セットアップ手順

## 1. Clone this repository<br>このリポジトリをクローンします

    git clone https://github.com/DuckArrow/discord-translator-bot.git

    cd discord-translator-bot


## 2. Copy the .env.example file to .env and input the necessary information<br>`.env.example` ファイルを `.env` にコピーし、必要な情報を入力します

    cp .env.example .env

## Open .env in a text editor and enter the Discord token, Google Cloud credentials path, DeepL API key (if using), etc.<br>テキストエディタで `.env` を開き、Discord トークン、Google Cloud 認証情報のパス、DeepL API キー（使用する場合）などを入力してください。


## 3. Place the Google Cloud credentials file (JSON) in the project's root directory and properly set the GOOGLE_APPLICATION_CREDENTIALS path in the .env file.<br>Google Cloud の認証情報ファイル（JSON）をプロジェクトのルートディレクトリに配置し、`.env` ファイル内の `GOOGLE_APPLICATION_CREDENTIALS` パスを適切に設定してください。


##  4. Build the Docker image<br>Dockerイメージをビルドします

    docker build -t discord-translator-bot .


##  5. Run the container<br>コンテナを実行します

    docker run -d --name discord-bot discord-translator-bot


# Precautions<br>注意事項

- If using this bot on a public server, please pay close attention to security.
<br>このボットを公開サーバーで使用する場合は、セキュリティに十分注意してください。<br>

- Be mindful of API usage and costs. Check the terms of service and pricing plans for each service (Google Cloud, DeepL). 
<br>API使用量とコストに注意してください。各サービス（Google Cloud、DeepL）の利用規約と料金プランを確認してください。

- This bot is created for educational purposes. For actual use, please comply with applicable laws and regulations.
<br>このボットは教育目的で作成されています。実際の使用では、適用される法律と規制を遵守してください。

# License<br>ライセンス

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Contribution<br>貢献
Pull requests are welcome. For major changes, please open an issue first to discuss the proposed changes.<br>
プルリクエストは歓迎します。大きな変更を加える場合は、まずissueを開いて変更内容を議論してください。

# Support<br>サポート
If you have any problems or questions, please open an issue on GitHub.<br>
問題や質問がある場合は、GitHubのissueを開いてください。
