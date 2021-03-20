# import main Flask class and request object
from flask import Flask, request
from logic import pred

# create the Flask app
app = Flask("SBB-backend")

@app.route('/pred')
def query_example():
    date = request.args.get('date')
    place = request.args.get('place')
    return pred(date, place)

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host='127.0.0.1', debug=True, port=5000)
