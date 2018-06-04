from flask import *
from mongoengine import *
import mlab
from models.user import User

app = Flask(__name__)

mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        fullname = form['fullname']
        yob = form['yob']
        email = form['email']
        gender = form['gender']

        user = User(username=username,
                    password=password,
                    fullname=fullname,
                    yob=yob,
                    email=email,
                    gender=gender)
        user.save()

        return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
