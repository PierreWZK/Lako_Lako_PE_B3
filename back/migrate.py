# back/migrate.py

from flask_migrate import Migrate
from App import create_app, db
import click
from flask.cli import with_appcontext

app = create_app()
migrate = Migrate(app, db)

@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized the database.')


@click.group()
def cli():
    pass

cli.add_command(init_db_command)

if __name__ == '__main__':
    cli()
