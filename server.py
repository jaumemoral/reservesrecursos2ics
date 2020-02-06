from flask import Flask,Response,request
import reservarecursos

app = Flask(__name__)

@app.route("/")
def recursosreserves2ics():
    ics=reservarecursos.convertir_reserves_a_ics_per_id_recurs(int(request.args.get('id')))
    return Response(ics, mimetype='text/calendar')
