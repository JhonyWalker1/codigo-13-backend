import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

### PARA CONECTARSE A FIRESTORE
from firebase_admin import firestore

db = firestore.client()

colProyectos = db.collectiolsn('proyectos')
docProyectos = colProyectos.get()

for doc in docProyectos: 
    print(doc.to_dict())


