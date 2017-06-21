from app import get_app
from config import FlaskConstants
from views import Introduction
# from unittests.curses_tests import CursesTest

app = get_app()
import views

if __name__ == '__main__':
    # app.run(
    #     host=FlaskConstants.HOST,
    #     port=FlaskConstants.PORT
    # )
    ch = Introduction()
    ch.intro()


