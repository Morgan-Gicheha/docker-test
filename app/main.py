from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# the port , use the name of the service from docker-compose file
# app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://postgres:password@db:5432/ims" 
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///ims.db" 
app.config["SECRET_KEY"]= 'knkn'


db =SQLAlchemy(app)
@app.before_first_request
def create():
    db.create_all()

class Test(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


@app.route("/")
def hone():
    this=Test(name="test datase")
    db.session.add(this)
    db.session.commit()

    data = Test.query.first()
    x= Test.query.all()
    for r in x:
        print(r.name)
    return data.name

@app.route("/t")
def greet():
    return "hey"



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
