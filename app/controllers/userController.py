from os import name
from app import app
from flask import request, jsonify
from flask_marshmallow import Marshmallow
from app.models.userModel import db, Users
from flask_jwt_extended import *

import datetime

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class meta:
        fields = ('id_user', 'username', 'email', 'password')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

def getDetailUser(decodeToken):
    decode = decodeToken
    user = Users.query.get(decode.get('id'))
    result = userSchema.dump(user)
    return jsonify({"msg": "Success get user by id", "status": 200, "data": result})

def updateUser(decodeToken):
    decode = decodeToken
    user = Users.query.get(decode.get('id'))
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']

    user.username = username
    user.name = name
    user.setPassword(password)
    user.email = email
    db.session.commit()
    result = userSchema.dump(user)
    return jsonify({"msg": "Success update user", "status": 200, "data": result})

def signUp():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']

    newUser = Users(username, name, password, email)
    newUser.setPassword(password)
    db.session.add(newUser)
    db.session.commit()
    user = userSchema.dump(newUser)
    return jsonify({"msg": "Success Sign Up", "status": 200, "data": user})


def signIn():
    username = request.form['username']
    password = request.form['password']

    user = Users.query.filter_by(username=username).first()

    if not user:
        return jsonify("User not found")

    if not user.checkPassword(password):
        return jsonify({
            "status": 401,
            "msg": "Login Invalid",
            "error": "wrong password"
        })
    data = singleTransform(user)
    expires = datetime.timedelta(days=1)
    expires_refresh = datetime.timedelta(days=3)
    access_token = create_access_token(data, fresh=True, expires_delta=expires)
    refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
    newData = {**data, "token": access_token, "refresh_token": refresh_token}
    return jsonify({
        "msg": "Success Sign In",
        "status": 200,
        "data": newData,
    })


@jwt_required(refresh=True)
def refresh():
    user = get_jwt_identity()
    new_token = create_access_token(identity=user, fresh=False)

    return jsonify({
        "token_access": new_token
    }, "")


def singleTransform(users):
    return{
        'id_user': users.id,
        'username': users.username,
        'name' : users.name,
        'email': users.email
    }