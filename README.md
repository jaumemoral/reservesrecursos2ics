Per instalar les dependències
-----------------------------

pip install -r requirements.txt

Per executar el servei
-----------------------------

FLASK_APP=server.py flask run

Funcionament
-----------------------------

Ens connectem al port 5000 i li passem una URL del tipus 

https://reservarecursos.upc.edu/utgcntic/bookingliveview/json?nid=8194&start=1534291200000&end=1565827200000

Com a paràmetre

http://127.0.0.1:5000/?url=https%3A%2F%2Freservarecursos.upc.edu%2Futgcntic%2Fbookingliveview%2Fjson%3F%26nid%3D8194%26start%3D1541977200000%26end%3D1542582000000

Aquesta URL la podem fabricar a partir del calendari d'un recurs

https://reservarecursos.upc.edu/utgcntic/node/8194

Si mirem les peticions que fa amb F12, veurem que demana una url d'aquest estil, que inidica el recurs i la data inici i fi en que volem veure esdeveniments.

O bé directament només el ID del recurs i ens tornarà els events desde 6 mesos enrera fins 6 mesos endavant

http://127.0.0.1:5000/?id=8194
