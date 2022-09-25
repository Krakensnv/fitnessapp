from main import create_app
from main.blueprints.page import page
from main.blueprints.page import calc

# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/flask.cfg
# Run as python run.py
# app = Flask(__name__, instance_relative_config=True)

if __name__ == '__main__':
    app = create_app('flask.cfg')
    app.register_blueprint(page)
    app.register_blueprint(calc)
    app.run(host='0.0.0.0')
