from flask import Flask,render_template, url_for, request
from requests import post
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('hello.html')
@app.route('/movie', methods=['GET', 'POST'])
def movie():
  if request.method == 'POST':
    return redirect(url_for('index'))
# show the form, it wasn't submitted
  return render_template('movie.html')
@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST':
    result = request.form
    url='http://www.omdbapi.com/?apikey='
    key='a1d89815'
    r=post(url+key+'&t='+result['Name'])
    print (url+key+'&t='+result['Name'])
    jsonToPython = json.loads(r.text)
    print(r.text)
    return render_template("result.html",result=jsonToPython)

if __name__ == '__main__':
  app.run()
