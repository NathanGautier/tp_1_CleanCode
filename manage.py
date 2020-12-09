# coding=utf-8
import os
import unittest

# Import Manager command
from flask_script import Manager

from app.main import create_app
from app import blueprint


# Call create_app (fichier main/__init__.py) to select right env - could be prod / dev / test
app = create_app(os.getenv('CLIENT_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

# Create executables commands
@manager.command
def run():
    app.run(host="0.0.0.0", port=int("5000"), debug=True)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
