Per instalar les dependències
-----------------------------

pip install -r requirements

Per executar el servei
-----------------------------

FLASK_APP=server.py flask run

Per provar
-----------------------------

Ens connectem al port 5000 i li passem una URL del tipus 

https://reservarecursos.upc.edu/utgcntic/bookingliveview/json?nid=8194&start=1534291200000&end=1565827200000

Com a paràmetre

http://127.0.0.1:5000/?url=https%3A%2F%2Freservarecursos.upc.edu%2Futgcntic%2Fbookingliveview%2Fjson%3F%26nid%3D8194%26start%3D1541977200000%26end%3D1542582000000

