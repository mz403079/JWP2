from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Witaj w mojej aplikacji Flask!</p>"

@app.route('/about')
def contact_page():
   return 'Strona stworzona przez M. Zaborowski!!!' 

@app.route('/contact')
def show_blog():
   return 'Nr telefonu: 555-444-333<br/> Nr telefonu 2: 111-333-213<br/> Adres e-mail: mz@uni.p.lodz.pl'


if __name__ == '__main__':
   app.run(debug=True)