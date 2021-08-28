from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')
@app.route('/confirm',methods=['POST','GET'])
def register():
      if request.method == 'POST':
          n = request.form.get('name')
          a = request.form.get('address')
          r = request.form.get('reservationquota')
          g = request.form.get('age')
          t = request.form.get('trainname')
          j = request.form.get('journeyfrom')
          o = request.form.get('journeyto')
          c = request.form.get('classs')
          s = request.form.get('journeydate')
          return render_template('confirm.html',name=n, address=a,reservationquota=r,age=g,trainname=t,journeyfrom=j,journeyto=o,classs=c,journeydate=s)






if __name__ == "__main__":
      app.run(debug=True)