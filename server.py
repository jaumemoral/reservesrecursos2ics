from flask import Flask,Response,request
import reservarecursos

app = Flask(__name__)

@app.route("/")
def recursosreserves2ics():
    if request.args.get('id'):
        ics=reservarecursos.convertir_reserves_a_ics_per_id_recurs(request.args.get('id'))
    elif request.args.get('url'):
        ics=reservarecursos.convertir_reserves_a_ics_per_url(request.args.get('url'))
    return Response(ics, mimetype='text/calendar')
