from flask import Flask, render_template
import firebase_admin 
from firebase_admin import credentials,db
app= Flask (__name__)
cred=credentials.Certificate("C:/Users/ASUS/Downloads/python.1/project1-86249-firebase-adminsdk-fbsvc-b1bf4a3ab5.json")
if not firebase_admin._apps:
     firebase_admin.initialize_app(cred,{"databaseURL":"https://project1-86249-default-rtdb.firebaseio.com/"})

@app.route('/')
def Home():
    ref=db.reference("/visits")
    ref.push({'page':'home'})
    return render_template("index.html")
@app.route('/contact')
def contact():
   ref=db.reference("/visits")
   ref.push({'page':'contact'})
   return render_template("contact.html")
@app.route('/about')
def about():
 ref=db.reference("/visits")
 ref.push({'page':'about'})
 return render_template("about.html")
if __name__=='__main__':
 app.run(debug=True)