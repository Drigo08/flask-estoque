from pathlib import Path

from flask import Flask


def existe_esquema(app: Flask) -> bool:
    nome_do_arquivo = Path(app.instance_path) / app.config.get('SQLITE_DB')
    if nome_do_arquivo.is_file():
        return True
    return False