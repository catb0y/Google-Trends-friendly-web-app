#! /usr/bin/python
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from pytrends.request import TrendReq


app = Flask(__name__)
app.secret_key = "whatever floats your boat"

# Connect to Google with pytrends
pytrend = TrendReq(hl='en-US', tz=360)

# Views
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/trends', methods=["GET", "POST"])
def trends():
    # reading the GET argument with the request
    keyword = request.args.get('keyword')

    # use pytrends to retrieve data & change df index to string
    pytrend.build_payload(kw_list=[keyword], timeframe='today 5-y')
    results = pytrend.interest_over_time()
    results.index = results.index.astype(str)

    # jsonify data for usage in chart
    results = results.to_json(orient='index')
    results = jsonify(results)
    return results # results is Google Trends data 


if __name__== '__main__':
    app.run(debug=True)
