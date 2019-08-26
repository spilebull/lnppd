# ==================================================
# Dockerfile Django 環境構築
# ==================================================
FROM python:3.7-alpine

# --------------------------------------------------
# 基本設定
# --------------------------------------------------
RUN mkdir /code
ENV APP_PATH /code
WORKDIR $APP_PATH

# --------------------------------------------------
# 環境変数を設定
# --------------------------------------------------
# Pythonがpyc filesとdiscへ書き込むことを防ぐ  
ENV PYTHONDONTWRITEBYTECODE 1  
# Pythonが標準入出力をバッファリングすることを防ぐ  
ENV PYTHONUNBUFFERED 1  

# --------------------------------------------------
# Psycopg2 インストール (PostgreSQL Driver 用)
# --------------------------------------------------
RUN apk update
RUN apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add postgresql-dev
RUN pip install psycopg2
RUN apk del build-deps

# --------------------------------------------------
# Pipenv インストール
# --------------------------------------------------
RUN pip install --upgrade pip
RUN pip install pipenv

# --------------------------------------------------
# Django 構築
# --------------------------------------------------
COPY Pipfile $APP_PATH/
RUN pipenv install --skip-lock --system --dev

# ホスト [app/src] を [/code] へコピー
COPY . $APP_PATH
