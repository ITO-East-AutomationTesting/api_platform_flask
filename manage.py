# encoding: utf-8
"""
@author: pencil
@file: manage.py
@time: 2018/10/31 16:39
"""
import os

import click
from flask_migrate import Migrate

from app import create_app, db
from app.models import Role, User

# production default
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db, render_as_batch=True)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)


@app.cli.command()
def initdata():
    click.echo('Initializing the roles and permissions and admin...')
    Role.init_role()
    User.init_user()  # 初始化
    click.echo('Done.')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)
    # app.run(host='172.18.28.41', port=8090, debug=True)