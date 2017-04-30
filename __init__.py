from app import get_app
from views import CharacterCreation

app = get_app()

if __name__ == '__main__':
    ch = CharacterCreation()
    ch.__init__()