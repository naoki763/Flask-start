# ユーザー登録および検索アプリ

このアプリは、Flask を使用して構築されたシンプルなウェブアプリケーションです。ユーザー名とメールアドレスを登録し、既存のユーザーをユーザー名で検索できる機能を提供します。このアプリは PostgreSQL をデータベースとして使用し、`docker-compose` によるデータベースコンテナの管理が可能です。また、`uv` を使用してパッケージ管理と仮想環境の構築を簡略化しています。

---

## 主な機能

- **ユーザー登録**: ユーザー名とメールアドレスを入力して新しいユーザーを登録できます。
- **ユーザー検索**: 登録済みのユーザーをユーザー名で検索できます。

---

## 必要な環境

- Python 3.7 以上
- `uv` (パッケージ管理と仮想環境構築用)
- Docker および Docker Compose

---

## インストール手順

1. **リポジトリをクローン**:
   ```command
   git clone https://github.com/yourusername/user-registration-app.git
   cd user-registration-app
   ```

2. **uv を使用して環境を構築**:
   - `uv` がインストールされていない場合、まずインストールします。
     ```command
     pip install uv
     ```
   - 仮想環境を構築し、依存関係をインストールします。
     ```command
     uv init
     uv install
     ```

3. **Docker で PostgreSQL を起動**:
　　- docker-compose.yamlがあるディレクトリに移動してください。
     ```command
     cd Docker
     ```
   - Docker Compose を使用して PostgreSQL コンテナを立ち上げます。
    ```command
     docker-compose up -d
    ```

4. **アプリケーションを起動**:
   ```command
   uv run python run.py
   ```
   
5. **アプリケーションを起動**:
   ```command
   uv run flask --app main run
   ```

6. ブラウザでアクセス: http://127.0.0.1:5000/ にアクセスしてください。
