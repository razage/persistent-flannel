from flask_migrate import MigrateCommand

from pf import manager

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
