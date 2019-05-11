from app import app
import requests
import json
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='ALERT! SHIT IS ON FIRE!')

@app.route('/potato')
def get_prometheus():
    data = requests.get('http://g.cmaker.studio:9090/api/v1/alerts')
    json_data = json.loads(data.content)
    number_of_alerts = len(json_data['data']['alerts'])
    if number_of_alerts > 0:
      return render_template('NOT-OK.html')
    else:
      return render_template('OK.html')
  