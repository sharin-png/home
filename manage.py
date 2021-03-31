from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 选择开发模式
app = create_app('develop')
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
