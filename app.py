from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


DB_USER = 'dogsdream'
DB_PASS = 'group3osu'
DB_HOST = 'dogsdream.mysql.pythonanywhere-services.com'
DB_PORT = '3306'
DATABASE = 'dogsdream$dogsdream'


# Set up flask app to connect to db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql://{}:{}@{}:{}/{}'.\
    format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize database
db = SQLAlchemy(app)


# Create models
class Sitters(db.Model):
    __tablename__ = "Sitters"
    sitterId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(256), nullable=False)
    lastName = db.Column(db.String(256), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    streetAddress = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipCode = db.Column(db.Integer, nullable=False)


class Persons(db.Model):
    __tablename__ = "Persons"
    ID = db.Column(db.Integer, primary_key=True)
    LastName = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<ID %r>' % self.ID

@app.route('/')
def index():
   return 'Hello, World!'

@app.route('/testdb')
def testdb():
    person = Persons(ID=3, LastName="Gosia")
    db.session.add(person)
    db.session.commit()
    return 'Testing db connection'


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/owner/')
def owner():
    return render_template('owner/owner.html')


@app.route('/owner/view', methods=['POST', 'GET'])
def view():
    return render_template('owner/view.html')


@app.route('/owner/add-dog', methods=['POST', 'GET'])
def add_dog():
    return render_template('owner/add-dog.html')


@app.route('/sitter/')
def sitter():
    return render_template('sitter/sitter.html')


@app.route('/sitter/add-job')
def add_job():
    return render_template('sitter/add-job.html')


@app.route('/sitter/view-job')
def view_job():
    return render_template('sitter/view-job.html')


# if __name__ == '__main__':
#     app.run(debug=True)