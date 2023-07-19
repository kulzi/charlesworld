from flask import Flask, render_template, request
import smtplib
app = Flask(__name__)
password = "avdtphdawezfdrml"
user_mail = "charlesadamu.ku@yahoo.com"
sent_mail = "charliesworldofstories@gmail.com"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/stories')
def stories():
    return render_template('stories.html')


@app.route('/story1')
def story1():
    return render_template('story1.html')


@app.route('/chapters')
def chapters():
    return render_template('chapters.html')


@app.route('/chapter1')
def chapter1():
    return render_template('chapter1.html')


@app.route('/articles')
def articles():
    return render_template('articles.html')


@app.route('/article1')
def article1():
    return render_template('article1.html')


@app.route('/poems')
def poems():
    return render_template('poems.html')


@app.route('/subscribe', methods=["POST", "GET"])
def subscribe():
    if request.method == "POST":
        user_comment = request.form["comm"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=sent_mail,
                                msg=f"Subject:comment\n\ncomment:{user_comment}")
        return render_template('index.html')
    return render_template('subscribe.html')


@app.route('/poem1', methods=["POST", "GET"])
def poem1():
    if request.method == "POST":
        user_comment = request.form["comm"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=sent_mail, msg=f"Subject:subscription\n\nemail:{user_comment}")
        return render_template('poem1.html')
    return render_template('poem1.html')


@app.route('/poem2', methods=["POST", "GET"])
def poem2():
    if request.method == "POST":
        user_comment = request.form["comm"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=sent_mail, msg=f"Subject:subscription\n\nemail:{user_comment}")
        return render_template('poem2.html')
    return render_template('poem2.html')


@app.route('/poem3', methods=["POST", "GET"])
def poem3():
    if request.method == "POST":
        user_comment = request.form["comm"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=sent_mail, msg=f"Subject:subscription\n\nemail:{user_comment}")
        return render_template('poem3.html')
    return render_template('poem3.html')


@app.route('/poem4', methods=["POST", "GET"])
def poem4():
    if request.method == "POST":
        user_comment = request.form["comm"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=sent_mail, msg=f"Subject:subscription\n\nemail:{user_comment}")
        return render_template('poem4.html')
    return render_template('poem4.html')


@app.route('/poem5', methods=["POST", "GET"])
def poem5():
    if request.method == "POST":
        user_comment = request.form["comm"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=sent_mail, msg=f"Subject:subscription\n\nemail:{user_comment}")
        return render_template('poem5.html')
    return render_template('poem5.html')


@app.route('/poem6', methods=["POST", "GET"])
def poem6():
    if request.method == "POST":
        user_comment = request.form["comm"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=sent_mail, msg=f"Subject:subscription\n\nemail:{user_comment}")
        return render_template('poem6.html')
    return render_template('poem6.html')


if __name__ == "__main__":
    app.run(debug=True)