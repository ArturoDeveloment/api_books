from app import create_app
from config import server

app = create_app()

if __name__ == "__main__":
    app.run(**server)