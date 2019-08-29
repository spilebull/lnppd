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
├── Dockerfile
├── Pipfile
├── README.md
├── app
│   └── src
│       ├── config
│       │   ├── __init__.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       ├── main
│       │   ├── __init__.py
│       │   ├── python
│       │   │   ├── __init__.py
│       │   │   ├── admin.py
│       │   │   ├── apps.py
│       │   │   ├── migrations
│       │   │   │   └── __init__.py
│       │   │   ├── models
│       │   │   │   └── __init__.py
│       │   │   └── views
│       │   │       ├── __init__.py
│       │   │       └── main.py
│       │   └── static
│       │       ├── css
│       │       │   └── dummy.css
│       │       ├── img
│       │       │   └── dummy.png
│       │       └── js
│       │           └── dummy.js
│       ├── manage.py
│       ├── templates
│       │   └── dummy.html
│       └── test
│           ├── __init__.py
│           └── python
│               ├── __init__.py
│               └── tests.py
├── docker-compose.yml
└── settings
    └── nginx
        └── django.conf
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
$ docker-compose build --no-cache       # build without cache
```

See processes:
```bash
$ docker-compose ps                 # docker-compose processes
$ docker ps -a                      # docker processes (sometimes needed)
$ docker stats [container name]     # see live docker container metrics
```

See logs:
```bash
# See logs of all services
$ docker-compose logs

# See logs of a specific service
$ docker-compose logs -f [service_name]
```

Run commands in container:
```bash
# Name of service is the name you gave it in the docker-compose.yml
$ docker-compose run [service_name] /bin/bash
$ docker-compose run [service_name] python /srv/starter/manage.py shell
$ docker-compose run [service_name] env
```

Remove all docker containers:
```bash
docker rm $(docker ps -a -q)
```

Remove all docker images:
```bash
docker rmi $(docker images -q)
```

### Some commands for managing the webapp
To initiate a command in an existing running container use the `docker exec`
command.

```bash
# Find container_name by using docker-compose ps

# restart uwsgi in a running container.
$ docker exec [container_name] touch /etc/uwsgi/reload-uwsgi.ini

# create migration file for an app
$ docker exec -it [container-name] \
    python /srv/[project-name]/manage.py makemigrations scheduler

# migrate
$ docker exec -it [container-name] \
    python3 /srv/[project-name]/manage.py migrate

# get sql contents of a migration
$ docker exec -it [container-name] \
    python3 /srv/[project-name]/manage.py sqlmigrate [appname] 0001

# get to interactive console
$ docker exec -it [container-name] \
    python3 /srv/[project-name]/manage.py shell

# testing
docker exec [container-name] \
    python3 /srv/[project-name]/manage.py test
```

## Troubleshooting
Q: I get the following error message when using the docker command:

```
FATA[0000] Get http:///var/run/docker.sock/v1.16/containers/json: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS? 

```

A: Add yourself (user) to the docker group, remember to re-log after!

```bash
$ usermod -a -G docker <your_username>
$ service docker restart
```

Q: Changes in my code are not being updated despite using volumes.

A: Remember to restart uWSGI for the changes to take effect.

```bash
# Find container_name by using docker-compose ps
$ docker exec [container_name] touch /etc/uwsgi/reload-uwsgi.ini
```
