from flask import Flask,Response,request
import reservarecursos

app = Flask(__name__)

@app.route("/")
def hello():
    url=request.args.get('url')
    ics=reservarecursos.convertir_reserves_a_ics(url)
    return Response(ics, mimetype='text/calendar')
