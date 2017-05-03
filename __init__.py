from app import get_app
from views import Introduction

app = get_app()

if __name__ == '__main__':
    ch = Introduction()
    ch.intro()
