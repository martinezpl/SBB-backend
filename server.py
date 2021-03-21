# import main Flask class and request object
from flask import Flask, request
from logic import Logic

# create the Flask app
app = Flask("SBB-backend")
log = Logic()

@app.route('/detail')
def detail():
    facility = request.args.get('facility')
    date = request.args.get('date')
    return log.detail(facility, date)

@app.route('/rafcik')
def rafcik():
    return log.rafcik()

@app.route('/home')
def home():
    return log.home()

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host='192.168.43.232', debug=True, port=5000)

