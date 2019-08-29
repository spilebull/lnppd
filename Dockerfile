# ==================================================
# Dockerfile Django 環境構築
# ==================================================
FROM python:3.7-alpine

# --------------------------------------------------
# 基本設定
# --------------------------------------------------
RUN mkdir -p /django/app/src

ENV PROJECT_PATH /django
ENV APP_PATH $PROJECT_PATH/app
ENV SRC_PATH $APP_PATH/src

WORKDIR $SRC_PATH

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
COPY Pipfile $PROJECT_PATH/
RUN pipenv install --skip-lock --system --dev # --dev 開発環境用パッケージもインストール

# ホスト [app/src] を [/app/src] へコピー
COPY ./app/src $SRC_PATH

CMD ["python", "manage.py", "collectstatic", "--no-input"]
CMD ["python", "manage.py", "migrate"]
CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:8000"]
#CMD ["celery", "worker", "--app=myapp.tasks"]
