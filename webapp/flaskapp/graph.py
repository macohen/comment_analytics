'''
Created on Nov 5, 2012

@author: cohenma
'''
from scipy import *
from scipy.signal import *
from matplotlib.pyplot import *
from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def list_data():
    csv = ""
    for line in open('../hadoop/output.txt').readlines():
        csv += line
    return csv

@app.route('/time_series/<type>')
def show_graph(type):
    data_file = url_for('static', filename='output.tsv')
    if type == 'd3':
        return render_template("time_series_d3.html", js=url_for('static', filename="d2.v2.min.js"), data_file=data_file) 
    elif type == "dygraph":
        js=url_for('static', filename="dygraph-combined.js")
        return render_template('time_series.html', data_file = data_file, js = js)
    elif type == "google":
        return render_template('time_series_google.html')

@app.route('/comments/day/<date>')
def show_day_of_comments(date):
    return date

if __name__ == '__main__':
    app.debug = True
    app.run()