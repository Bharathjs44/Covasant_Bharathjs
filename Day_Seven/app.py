from flask import Flask, render_template, request
from flask import jsonify
import os

app = Flask(__name__)

    
@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")
    
    
@app.route("/")
def index():
    return render_template("notepad.html", page="update")
    
    
@app.route("/updatefortoday", methods=["GET","POST"])
def update_for_today():
    if request.method =='POST':
        content = request.form.get("content", "ALL")
        with open("notepad.txt","a") as f:
            f.write(content+"\n")
        return render_template("notepad.html", page="success")
    return render_template("notepad.html",page="update")
 
 
@app.route("/share", methods = ["GET"])
def share():
    with open("notepad.txt","r") as f:
        content = f.readlines()
    if content:
        return render_template("notepad.html", page="show", content=content) 
    else:
        return render_template("notepad.html", page="empty")


@app.route("/clearnotepad", methods=['GET'])
def clearnotepad():
    with open("notepad.txt","wt") as f:
        f.writelines("")
    return render_template("notepad.html", page="cleared")
       
    
if __name__ == '__main__':
    app.run()