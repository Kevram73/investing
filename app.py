from src import app, db
from utils.constants import Constants


if __name__ == "__main__":
    db.create_all()
    app.run(debug=Constants.DEBUG, port=Constants.PORT)
