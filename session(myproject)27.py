from flask import *
import datetime
import hashlib
from session22C import MongoDBHelper
from bson import ObjectId  # Import ObjectId from bson

web_app = Flask("SMART HOME AUTOMATION SYSTEM")
db_helper = MongoDBHelper()

@web_app.route("/")  # Decorator
def index():
    # either you can return plain text
    # message = "Welcome to Patient Management System. Its {}".format(datetime.datetime.now())
    # OR you can return HTML
    # return message
    # render_template is used to return web pages (html pages)
    return render_template("login(project).html")

@web_app.route("/register(project)")
def register():
    return render_template("register(project).html")
@web_app.route("/logout(project)")
def logout():
    # Reset the Data in Session Object
    session["username"] = ""
    session["name"] = ""
    return redirect("/")

@web_app.route("/add-user", methods=["POST"])
def add_user_in_db():
    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "name": request.form["name"],
        "username": request.form["username"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "user_username": session['username'],
        
    }

    db_helper.collection = db_helper.db["appuser"]
    # Save user in DataBase i.e. MongoDB
    result = db_helper.insert(user_data)
    # message = "Welcome to Home Page. User ID is: {}".format(result.inserted_id)
    # return message

    # Write the data in the Session Object
    # This data can now be used anywhere in the project
    session['name'] = user_data["name"]
    session['username'] = user_data["username"]

    # return render_template("home.html", name=session['name'], email=session['email'])
    return render_template("home(project).html",name=session['name'], username=session['username'])
@web_app.route("/fetch-user", methods=["POST"])
def feth_user_from_db():

    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "username": request.form["username"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    db_helper.collection = db_helper.db["appuser"]
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=user_data)

    print("result:", result)
    
    if len(result)>0:
        user_data = result[0] # Get the dictionary from List 
        session['username'] = user_data["username"]
        session['name'] = user_data["name"]
        return render_template("home(project).html", name=session['name'], username=session['username'])
    else:
        return render_template("error(project).html", message="User Not Found. Please Try Again",
                               name=session["name"], username=session["username"])
@web_app.route("/devices")
def view_devices():
    if 'username' in session:
        db_helper.collection = db_helper.db["devices"]
        devices = db_helper.fetch({"user_username": session['username']})
        return render_template("device.html", devices=devices, name=session['name'],username=session['username'])
    else:
        return redirect('/')
@web_app.route("/add-device", methods=["GET", "POST"])
def add_device():
    if 'username' in session:
        if request.method == "POST":
            device_data = {
                "device_name": request.form["device_name"],
                "device_type": request.form["device_type"],
                "status": request.form["status"],
                "user_username": session['username']
            }
            db_helper.collection = db_helper.db["devices"]
            db_helper.insert(device_data)
        return render_template("add_device.html",name=session['name'], username=session['username'])
    else:
        return redirect('/')
@web_app.route("/control-device/<string:device_id>/<string:action>")
def control_device(device_id, action):
    if 'username' in session:
        db_helper.collection = db_helper.db["devices"]
        new_status = "On" if action == "turn_on" else "Off"
        db_helper.collection.update_one({"_id": ObjectId(device_id)}, {"$set": {"status": new_status}})
        return redirect('/devices')
    else:
        return redirect('/login(project)')

@web_app.route("/update-device/<string:device_id>", methods=["GET", "POST"])
def update_device(device_id):
    if 'username' in session:
        db_helper.collection = db_helper.db["devices"]
        device = db_helper.fetch({"_id": ObjectId(device_id), "user_username": session['username']})[0]
        if request.method == "POST":
            updated_data = {
                "device_name": request.form["device_name"],
                "device_type": request.form["device_type"],
                "status": request.form["status"]
            }
            db_helper.collection.update_one({"_id": ObjectId(device_id)}, {"$set": updated_data})
            return redirect('/devices')
        return render_template("update_device.html", device=device, name=session['name'],username=session['username'])
    else:
        return redirect('/login(project)')

@web_app.route("/select-device-update")
def select_device_update():
    if 'username' in session:
        db_helper.collection = db_helper.db["devices"]
        devices = db_helper.fetch({"user_username": session['username']})
        return render_template("select_device_update.html", devices=devices,name=session['name'], username=session['username'])
    else:
        return redirect('/')
@web_app.route("/home")
def homepage():
    return render_template("home(project).html", name=session['name'],username=session['username'])
@web_app.route("/automation-rules", methods=["GET", "POST"])
def automation_rules():
    if 'username' in session:
        db_helper.collection = db_helper.db["automation_rules"]
        if request.method == "POST":
            rule_data = {
                "rule_name": request.form["rule_name"],
                "trigger": request.form["trigger"],
                "action": request.form["action"],
                "schedule": request.form["schedule"],
                "user_username": session['username']
            }
            db_helper.insert(rule_data)
            return redirect('/automation-rules')
        
        rules = db_helper.fetch({"user_username": session['username']})
        return render_template("automation_rules.html", rules=rules, username=session['username'])
    else:
        return redirect('/login(project)')

def main():
    # In order to use Session Tracking, create a Secret Key
    web_app.secret_key = "automation-app-key-v2"

    # Run the App infinitely, till user wont quit
    web_app.run()
    # web_app.run(port=5001) # optionally you can give the port number

if __name__ == "__main__":
    main()
