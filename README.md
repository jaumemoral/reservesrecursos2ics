Per instalar les dependències
-----------------------------

pip install -r requirements.txt

Per executar el servei
-----------------------------

FLASK_APP=server.py flask run

Funcionament
-----------------------------

Ens connectem al port 5000 i li passem una URL del tipus 

http://127.0.0.1:5000/?id=8194

on 8194 es l'identificador de recurs, que podem veure a la URL d'un recurs com per exemple

https://reservarecursos.upc.edu/utgcntic/node/8194