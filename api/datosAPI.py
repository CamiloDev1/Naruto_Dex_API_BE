import uuid
from flask import Blueprint,request,jsonify
from firebase_admin import firestore

db = firestore.client()
datos_ref = db.collection('datos')

datosAPI = Blueprint('datosAPI',__name__)

@datosAPI.route('/add',methods=['POST'])
def create():
    try:
        id=uuid.uuid4()
        datos_ref.document(id.hex).set(request.json)
        return jsonify({"succes":True}),200

    except Exception as e:
        return f"An Error Ocurred: {e}"

@datosAPI.route('/get_all_data',methods=['GET'])
def read():
    try:
        all_data = [doc.to_dict() for doc in datos_ref.stream()]
        return jsonify(all_data), 200
    except Exception as e:
        return f"An Error Ocurred: {e}"