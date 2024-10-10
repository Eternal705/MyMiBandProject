# Git 利用ガイド
## 基本的な Git コマンド
### 1. リポジトリのクローン
リモートリポジトリをローカルにクローンするには、以下のコマンドを使用します。

bash

git clone <リポジトリのURL>
例:

bash

git clone https://github.com/Eternal705/MyMiBandProject.git
### 2. ステージング
変更をステージングエリアに追加するには、以下のコマンドを使用します。

bash

git add <ファイル名>
すべての変更をステージングする場合は、次のコマンドを使用します。

bash

git add .
### 3. コミット
ステージングされた変更をリポジトリにコミットするには、次のコマンドを使用します。

bash

git commit -m "コミットメッセージ"
例:

bash

git commit -m "Initial project structure"
### 4. リモートリポジトリへのプッシュ
コミットをリモートリポジトリにプッシュするには、以下のコマンドを使用します。

bash

git push -u origin main
## トラブルシューティング
### 1. "Please tell me who you are" エラー
このエラーは、Gitのユーザー情報が設定されていない場合に発生します。次のコマンドでユーザー名とメールアドレスを設定してください。

bash

git config --global user.name "Your Name"
git config --global user.email "you@example.com"
例:

bash

git config --global user.name "Eternal705"
git config --global user.email "your_email@example.com"
### 2. "failed to push some refs" エラー
このエラーは、リモートリポジトリの内容がローカルと異なる場合に発生します。以下のコマンドでリモートの変更をフェッチし、マージしてください。

bash

git pull origin main
その後、再度プッシュを試みます。

### 3. "ambiguous argument 'origin/master'" エラー
このエラーは、指定したブランチが存在しない場合に発生します。現在のブランチを確認するには、次のコマンドを使用します。

bash

git branch -v
ブランチが正しいことを確認し、必要に応じて新しいブランチを作成します。

### 4. "merge: origin/master - not something we can merge" エラー
このエラーは、リモートリポジトリにマージできない状態の場合に発生します。以下のコマンドでリモートリポジトリの変更をプルしてから、マージを試みます。

bash

git pull origin main
