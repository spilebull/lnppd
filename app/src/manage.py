#!/usr/bin/env python
# ==================================================
# 管理タスク用 Djangoコマンドラインユーティリティ
# ==================================================
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Djangoをインポートできませんでした。"
            "{PYTHONPATH}環境変数にインストールされており、利用可能かどうか確認して下さい。"
            "また、仮想環境を有効にするのも確認してください。"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
