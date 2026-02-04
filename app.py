from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_email():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    msg = EmailMessage()
    msg["Subject"] = "New Website Enquiry"
    msg["From"] = "majindevil164@gmail.com"
    msg["To"] = "mohiisfar@gmail.com"
    msg["Reply-To"] = email

    msg.set_content(f"""
New Contact Form Submission

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
    """)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("majindevil164@gmail.com", "htdw sgyv oeig eobs")
        smtp.send_message(msg)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
