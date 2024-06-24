全てのコードがclaude.aiで作成されたものです。
IssuesやPull requestsに関しても全てclaude.aiに転載します。

# Discord Translator Bot

このプロジェクトは、多言語対応のDiscord翻訳ボットです。音声認識、翻訳、テキスト読み上げ機能を提供します。

## セットアップ手順

1. このリポジトリをクローンします

    git clone https://github.com/your-username/discord-translator-bot.git
    cd discord-translator-bot


2. `.env.example` ファイルを `.env` にコピーし、必要な情報を入力します

    cp .env.example .env

テキストエディタで `.env` を開き、Discord トークン、Google Cloud 認証情報のパス、DeepL API キー（使用する場合）などを入力してください。


3. Google Cloud の認証情報ファイル（JSON）をプロジェクトのルートディレクトリに配置し、`.env` ファイル内の `GOOGLE_APPLICATION_CREDENTIALS` パスを適切に設定してください。


4. Dockerイメージをビルドします

    docker build -t discord-translator-bot .


5. コンテナを実行します

    docker run -d --name discord-bot discord-translator-bot


## 注意事項

- このボットを公開サーバーで使用する場合は、セキュリティに十分注意してください。
- API使用量とコストに注意してください。各サービス（Google Cloud、DeepL）の利用規約と料金プランを確認してください。
- このボットは教育目的で作成されています。実際の使用では、適用される法律と規制を遵守してください。

## ライセンス

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 貢献

プルリクエストは歓迎します。大きな変更を加える場合は、まずissueを開いて変更内容を議論してください。

## サポート

問題や質問がある場合は、GitHubのissueを開いてください。
