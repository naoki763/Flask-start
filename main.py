# from flask_app import create_app
from flask_app.factory import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


