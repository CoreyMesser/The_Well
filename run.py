from app import get_app
from config import FlaskConstants

app = get_app()

if __name__ == '__main__':
    app.run(
        host=FlaskConstants.HOST,
        port=FlaskConstants.PORT
    )
