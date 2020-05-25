from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
print("het")
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://postgres:morgan@127.0.0.1:5432/ims"
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
    this=Test(name="morgan")
    db.session.add(this)
    db.session.commit()
    # q
    data = Test.query.first()
    print(data.name)
    return data.name

@app.route("/t")
def hon():
    return "hey"



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
