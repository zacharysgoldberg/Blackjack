from .src import create_app
from .src.api.models.models import db


app = create_app()


if __name__ == "__main__":
    db.create_all()
    app.run(threaded=True, host='0.0.0.0', port=5000)
