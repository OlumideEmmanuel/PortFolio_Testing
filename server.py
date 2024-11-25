from flask import Flask, render_template, request
import smtplib
import json
import smtplib

from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form


        form_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("Phone Number"),
            "subject": data.get("subject"),
            "message": data.get("message")
        }

        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file, indent=4)


        with open('form_data.json', 'r') as json_file:
         form_data = json.load(json_file)

        #  Extract All fileds
         
         
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        subject = form_data.get('subject')
        message = form_data.get('message')

        print(name, email, phone, subject, message)


        my_email = "olumideemmanuel17@gmail.com"
        password = "ikul bvpn ziaz bsee"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs =my_email, msg=f"subject:{subject}\n\n{message}\n\n\n\n{name}\n{email}\n{phone}.")
            connection.sendmail(from_addr=my_email, to_addrs =email, msg=f"subject:Olumide Emmanuel \n\nThanks For contacting Olumide Emmanuel\n Will get Shortly\n\n\n\nOLUMIDE EMMAUNEL\n{my_email}\n09045717598.")


        return render_template("index.html", msg_sent=True,)
    
    return render_template("index.html", msg_sent=False)


@app.route('/graphic', methods=["GET", "POST"])
def graphic():
    if request.method == "POST":
        data = request.form


        form_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("Phone Number"),
            "subject": data.get("subject"),
            "message": data.get("message")
        }

        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file, indent=4)


        with open('form_data.json', 'r') as json_file:
         form_data = json.load(json_file)

        #  Extract All fileds
         
         
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        subject = form_data.get('subject')
        message = form_data.get('message')

        print(name, email, phone, subject, message)


        my_email = "olumideemmanuel17@gmail.com"
        password = "ikul bvpn ziaz bsee"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs =my_email, msg=f"subject:{subject}\n\n{message}\n\n\n\n{name}\n{email}\n{phone}.")
            connection.sendmail(from_addr=my_email, to_addrs =email, msg=f"subject:Olumide Emmanuel \n\nThanks For contacting Olumide Emmanuel\n Will get Shortly\n\n\n\nOLUMIDE EMMAUNEL\n{my_email}\n09045717598.")


        return render_template("graphic.html", msg_sent=True,)
    
    return render_template("graphic.html", msg_sent=False)



@app.route('/logo', methods=["GET", "POST"])
def logo():
    if request.method == "POST":
        data = request.form


        form_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("Phone Number"),
            "subject": data.get("subject"),
            "message": data.get("message")
        }

        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file, indent=4)


        with open('form_data.json', 'r') as json_file:
         form_data = json.load(json_file)

        #  Extract All fileds
         
         
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        subject = form_data.get('subject')
        message = form_data.get('message')

        print(name, email, phone, subject, message)


        my_email = "olumideemmanuel17@gmail.com"
        password = "ikul bvpn ziaz bsee"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs =my_email, msg=f"subject:{subject}\n\n{message}\n\n\n\n{name}\n{email}\n{phone}.")
            connection.sendmail(from_addr=my_email, to_addrs =email, msg=f"subject:Olumide Emmanuel \n\nThanks For contacting Olumide Emmanuel\n Will get Shortly\n\n\n\nOLUMIDE EMMAUNEL\n{my_email}\n09045717598.")


        return render_template("logo.html", msg_sent=True,)
    
    return render_template("logo.html", msg_sent=False)


@app.route('/website', methods=["GET", "POST"])
def website():
    if request.method == "POST":
        data = request.form


        form_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("Phone Number"),
            "subject": data.get("subject"),
            "message": data.get("message")
        }

        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file, indent=4)


        with open('form_data.json', 'r') as json_file:
         form_data = json.load(json_file)

        #  Extract All fileds
         
         
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        subject = form_data.get('subject')
        message = form_data.get('message')

        print(name, email, phone, subject, message)


        my_email = "olumideemmanuel17@gmail.com"
        password = "ikul bvpn ziaz bsee"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs =my_email, msg=f"subject:{subject}\n\n{message}\n\n\n\n{name}\n{email}\n{phone}.")
            connection.sendmail(from_addr=my_email, to_addrs =email, msg=f"subject:Olumide Emmanuel \n\nThanks For contacting Olumide Emmanuel\n Will get Shortly\n\n\n\nOLUMIDE EMMAUNEL\n{my_email}\n09045717598.")


        return render_template("website.html", msg_sent=True,)
    
    return render_template("website.html", msg_sent=False)



@app.route('/flyer', methods=["GET", "POST"])
def flyer():
    if request.method == "POST":
        data = request.form


        form_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("Phone Number"),
            "subject": data.get("subject"),
            "message": data.get("message")
        }

        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file, indent=4)


        with open('form_data.json', 'r') as json_file:
         form_data = json.load(json_file)

        #  Extract All fileds
         
         
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        subject = form_data.get('subject')
        message = form_data.get('message')

        print(name, email, phone, subject, message)


        my_email = "olumideemmanuel17@gmail.com"
        password = "ikul bvpn ziaz bsee"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs =my_email, msg=f"subject:{subject}\n\n{message}\n\n\n\n{name}\n{email}\n{phone}.")
            connection.sendmail(from_addr=my_email, to_addrs =email, msg=f"subject:Olumide Emmanuel \n\nThanks For contacting Olumide Emmanuel\n Will get Shortly\n\n\n\nOLUMIDE EMMAUNEL\n{my_email}\n09045717598.")


        return render_template("flyer.html", msg_sent=True,)
    
    return render_template("flyer.html", msg_sent=False)

@app.route('/frontend', methods=["GET", "POST"])
def frontend():
    if request.method == "POST":
        data = request.form


        form_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("Phone Number"),
            "subject": data.get("subject"),
            "message": data.get("message")
        }

        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file, indent=4)


        with open('form_data.json', 'r') as json_file:
         form_data = json.load(json_file)

        #  Extract All fileds
         
         
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        subject = form_data.get('subject')
        message = form_data.get('message')

        print(name, email, phone, subject, message)


        my_email = "olumideemmanuel17@gmail.com"
        password = "ikul bvpn ziaz bsee"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs =my_email, msg=f"subject:{subject}\n\n{message}\n\n\n\n{name}\n{email}\n{phone}.")
            connection.sendmail(from_addr=my_email, to_addrs =email, msg=f"subject:Olumide Emmanuel \n\nThanks For contacting Olumide Emmanuel\n Will get Shortly\n\n\n\nOLUMIDE EMMAUNEL\n{my_email}\n09045717598.")


        return render_template("frontend.html", msg_sent=True,)
    
    return render_template("frontend.html", msg_sent=False)


@app.route('/backend', methods=["GET", "POST"])
def backend():
    if request.method == "POST":
        data = request.form


        form_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("Phone Number"),
            "subject": data.get("subject"),
            "message": data.get("message")
        }

        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file, indent=4)


        with open('form_data.json', 'r') as json_file:
         form_data = json.load(json_file)

        #  Extract All fileds
         
         
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        subject = form_data.get('subject')
        message = form_data.get('message')

        print(name, email, phone, subject, message)


        my_email = "olumideemmanuel17@gmail.com"
        password = "ikul bvpn ziaz bsee"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs =my_email, msg=f"subject:{subject}\n\n{message}\n\n\n\n{name}\n{email}\n{phone}.")
            connection.sendmail(from_addr=my_email, to_addrs =email, msg=f"subject:Olumide Emmanuel \n\nThanks For contacting Olumide Emmanuel\n Will get Shortly\n\n\n\nOLUMIDE EMMAUNEL\n{my_email}\n09045717598.")


        return render_template("backend.html", msg_sent=True,)
    
    return render_template("backend.html", msg_sent=False)






    


if __name__ == "__main__":
    app.run(debug=True)






    # # Extract the email field
    #     email = form_data.get('email')
    
    #     print (email)


    # current_year= datetime.now().year
    # return render_template("index.html", year = current_year)

