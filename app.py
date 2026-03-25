
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# LOGIN PAGE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("LOGIN CLICKED")   # 👈 DEBUG LINE
        return redirect('/home')  # 👈 FORCE REDIRECT

    return render_template('login.html', show_navbar=False)
# HOME PAGE
@app.route('/home')
def home():
    return render_template('index.html', show_navbar=True)


@app.route('/scan')
def scan():
    return render_template('scan.html', show_navbar=True)


@app.route('/price')
def price():
    return render_template('price.html', show_navbar=True)


@app.route('/advisory')
def advisory():
    return render_template('advisory.html', show_navbar=True)


if __name__ == '__main__':
    if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

# LOGIN PAGE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("LOGIN CLICKED")   # 👈 DEBUG LINE
        return redirect('/home')  # 👈 FORCE REDIRECT

    return render_template('login.html', show_navbar=False)
# HOME PAGE
@app.route('/home')
def home():
    return render_template('index.html', show_navbar=True)


@app.route('/scan')
def scan():
    return render_template('scan.html', show_navbar=True)


@app.route('/price')
def price():
    return render_template('price.html', show_navbar=True)


@app.route('/advisory')
def advisory():
    return render_template('advisory.html', show_navbar=True)


if __name__ == '__main__':
    app.run(debug=True)
