from app import app
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers import userController, makananController


@app.route('/signup', methods=['POST'])
def signUp():
    return userController.signUp()


@app.route('/signin', methods=['POST'])
def signIn():
    return userController.signIn()


@app.route('/user', methods=['PUT', 'GET'])
@jwt_required()
def userDetails():
    payload = get_jwt_identity()
    if(request.method == 'GET'):
        return userController.getDetailUser(payload)
    elif(request.method == 'PUT'):
        return userController.updateUser(payload)


@app.route('/makanan', methods=["GET", "POST"])
@jwt_required()
def makanan():
    if(request.method == 'GET'):
        return makananController.getMakanan()
    if(request.method == 'POST'):
        return makananController.postMakanan()


@app.route('/makanan/<id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
def actionMakanan(id):
    if(request.method == "GET"):
        return makananController.getMakananById(id)
    elif(request.method == "PUT"):
        return makananController.updateMakanan(id)
    elif(request.method == "DELETE"):
        return makananController.deleteMakanan(id)

