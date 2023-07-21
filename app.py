from flask import Flask, request, render_template
 
app = Flask(__name__)  

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/contact', methods = ["GET", "POST"])
def contact():
    if request.method == "POST":
        first_name = request.form.get("first name")
        last_name = request.form.get("last name")
        email = request.form.get("email")
        reference = request.form.get("reference")
        message = request.form.get("message")
        
        return "Your name is " + first_name + last_name
    return render_template("contact.html")

if __name__=='__main__':
   app.run()