Docker Django
=============

## 起動方法
```bash
$ git clone git@github.com:spilebull/lnppd.git
$ docker-compose up -d
```

これで、 `https://localhost` および 管理サイト `https://localhost/admin` でアプリケーションにアクセスできます

使用されるスタック番号とバージョン番号：

| Name           | Version  |
|----------------|----------|
| Django         | 2.2.4    |
| Nginx          | 1.15     |
| Postgresql     | 11.1     |
| uWSGI          | 2.0.17.1 |

## ディレクトリ構造

```
├── lnppd
│   ├── Dockerfile
│   ├── Pipfile
│   ├── README.md
│   ├── app
│   │   └── src
│   │       ├── config
│   │       │   ├── __init__.py
│   │       │   ├── settings.py
│   │       │   ├── urls.py
│   │       │   └── wsgi.py
│   │       ├── main
│   │       │   ├── __init__.py
│   │       │   └── python
│   │       │       ├── __init__.py
│   │       │       ├── admin.py
│   │       │       ├── apps.py
│   │       │       ├── migrations
│   │       │       │   └── __init__.py
│   │       │       ├── models
│   │       │       │   └── __init__.py
│   │       │       ├── urls.py
│   │       │       └── views
│   │       │           ├── __init__.py
│   │       │           └── main.py
│   │       ├── manage.py
│   │       └── templates
│   │           └── dummy.html
│   ├── docker-compose.yml
│   └── settings
│       └── nginx
│           └── django.conf
```

## 設定方法

### Docker
インストール手順: [docker documentation](https://docs.docker.com/install/)
### Docker Compose
インストール手順: [docker compose](https://github.com/docker/compose), [ドキュメント](https://docs.docker.com/compose/install/)

### Django

```bash
# システムにDjangoがインストールされていることを確認
$ docker exec {コンテナ名} django-admin startproject {プロジェクト名}
```

`config/settings.py` ファイルを編集し、プロジェクト名を追加
`DJANGO_PROJECT_NAME` でプロジェクトを作成するか、そのままにしてデフォルトで開始。

データベース認証情報と静的な設定で `settings.py` ファイルを編集

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

STATIC_ROOT = '/app/src/static'
```

### 環境変数
ファイル `config/settings.py` は環境変数の設定に使用。
これらがこのプロジェクトが使用するデフォルト値です。
このファイルをバージョン外にする必要があることに注意してください。

## 起動方法
次のコマンドを実行するとコンテナが起動します:
```bash
$ docker-compose up             # フォアグラウンド起動
$ docker-compose up -d          # バックグラウンド起動
```

## その他
ビルドイメージ:
```bash
$ docker-compose build
$ docker-compose build --no-cache   # キャッシュなしでビルド
```

動作確認:
```bash
$ docker-compose ps                 # 動作確認
$ docker ps -a                      # 動作確認（全部）
$ docker stats [container name]     # 動作中のDockerコンテナ状態確認
```

ログ:
```bash
$ docker-compose logs                   # 全サービスログ確認
$ docker-compose logs -f [service_name] # 特定のサービスログ確認
```

コンテナ上でコマンド実行:
```bash
$ docker-compose run [service_name] /bin/bash
$ docker-compose run [service_name] python manage.py shell
$ docker-compose run [service_name] env
```

全コンテナ削除:
```bash
docker rm $(docker ps -a -q)
```

全コンテナイメージ削除:
```bash
docker rmi $(docker images -q)
```

### コマンド実行処理
実行中の既存のコンテナでコマンドを開始するには、 `docker exec` コマンドを実行する。

```bash
# docker-compose ps を 使用して container_name を見つける

# 実行中のコンテナでuwsgiを再起動
$ docker exec [container_name] touch /etc/uwsgi/reload-uwsgi.ini

# アプリ移行ファイルを作成
$ docker exec -it [container-name] \
    python [project-name]/manage.py makemigrations scheduler

# マイグレーション
$ docker exec -it [container-name] \
    python3 [project-name]/manage.py migrate

# 移行のSQLコンテンツを取得
$ docker exec -it [container-name] \
    python3 [project-name]/manage.py sqlmigrate [appname] 0001

# 対話型コンソールにアクセス
$ docker exec -it [container-name] \
    python3 [project-name]/manage.py shell

# テスト実行
docker exec [container-name] \
    python3 [project-name]/manage.py test
```
