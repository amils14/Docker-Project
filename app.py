from flask import Flask, render_template, request
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


app = Flask(__name__)

os.chdir('/root/Flask_app')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphoutput',methods = ['GET','POST'])
def gout():
    if request.method == 'POST':
        a=request.form['featurea']
        b=request.form['featureb']
        irisdf = pd.read_csv('iris.csv')

        snsplot = sns.lmplot(x=a, y=b, data=irisdf)
        pair_plot = sns.pairplot(irisdf,hue='species',palette='rainbow')

        snsplot.savefig("static/output.png")
        pair_plot.savefig("static/outputpair.png")
    return render_template('gout.html')


if __name__=="__main__":
    app.run(host='0.0.0.0')
