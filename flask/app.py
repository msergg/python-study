from flask import Flask, render_template, request, redirect


app = Flask(__name__)


# @app.route('/')
# @app.route('/<name>')
# def users(name='Anonimous'):
#     return render_template('index.html', name=name)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    name = phone = ''

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        if name and phone:
            # add to db
            return redirect('/')
    return render_template('add.html', name=name, phone=phone)

if __name__=='__main__':
    app.run(debug=True)
