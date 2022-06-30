from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'

class event(db.Model) :
    event_id=db.Column(db.Integer(),primary_key=True)
    event_name=db.Column(db.String(length=30),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False)
    college_name=db.Column(db.String(length=20),nullable=False)
    description=db.Column(db.String(length=1024),nullable=False)

@app.route("/")
def home_page():
    return render_template('home.html')
@app.route('/Upcomming_Events')
def Upcomming_Events():
    items=event.query.all()
    return render_template('UpcommingEvents.html',items=items)
@app.route('/Past_Events')
def Past_Events():
    return render_template('PastEvents.html')
@app.route('/ADD_Event')
def ADD_Event():
    return render_template('AddEvent.html')
@app.route('/EventAdded',methods=["GET","POST"])
def EventAdded():
    event_name=request.form["eventname"]
    price=request.form["entryfee"]
    college_name=request.form["collegename"]
    desc=request.form["description"]
    e=event(event_name=event_name,price=price,college_name=college_name,description=desc)
    db.session.add(e)
    db.session.commit()
    return render_template("yo.html")
    
app.run(debug=True)