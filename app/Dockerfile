# ==================================================
# Python Version 3.7 Image 取得
# ==================================================
FROM python:3.7

# ==================================================
# 環境変数を設定
# ==================================================
RUN mkdir /code

# ディレクトリパス設定
ENV APP_PATH /code

# 作業ディレクトリ設定
WORKDIR $APP_PATH

# Pythonがpyc filesとdiscへ書き込むことを防ぐ  
ENV PYTHONDONTWRITEBYTECODE 1  

# Pythonが標準入出力をバッファリングすることを防ぐ  
ENV PYTHONUNBUFFERED 1  

# ==================================================
# Pipenv インストール
# ==================================================
RUN pip install --upgrade pip
RUN pip install pipenv

# ホスト`Pipfile`をコンテナ作業ディレクトリへコピー
COPY Pipfile $APP_PTH/

# `Pipfile`からパッケージをインストールしてDjango環境構築
RUN pipenv install --skip-lock --system --dev

# ホストのカレントディレクトリ[[app directory]] を作業ディレクトリへコピー
COPY . $APP_PATH
