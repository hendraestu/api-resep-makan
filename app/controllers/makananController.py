from app import app
from flask import request, jsonify
from flask_marshmallow import Marshmallow
from app.models.makananModel import db, Makanan
import cloudinary.uploader

ma = Marshmallow(app)

class MakananSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama_makanan', 'image', 'keterangan', 'tanggal')

makananSchema = MakananSchema()
makanansSchema = MakananSchema(many=True)

def getMakanan():
    allMakanan = Makanan.query.all()
    result = makanansSchema.dump(allMakanan)
    return jsonify({"msg": "Success Get all makanan", "status": 200, "data": result})

def getMakananById(id):
    makanan = Makanan.query.get(id)
    result = makananSchema.dump(makanan)
    return jsonify({"msg": "Success Get makanan By Id", "status": 200, "data": result})

def postMakanan():
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    nama_makanan = request.form['nama_makanan']
    keterangan = request.form['keterangan']

    if 'image' not in request.files:
        resp = jsonify({"msg": "No body image attached in request"})
        resp.status_code = 501
        return resp
    fileImage = request.files['image']
    if fileImage.filename == '':
        resp = jsonify({'msg': "No file fileImage selected"})
        resp.status_code = 505
        return resp

    print(fileImage.filename)
    error = {}

    if fileImage and allowed_file(fileImage.filename):
        upload_result = cloudinary.uploader.upload(fileImage)
        image = upload_result["secure_url"]
    else:
        error[fileImage.filename] = 'File type is not allowed'

    newMakanan = Makanan(nama_makanan, keterangan, image)
    db.session.add(newMakanan)
    db.session.commit()
    new = makananSchema.dump(newMakanan)
    return jsonify({"msg": "Success Post Makanan", "status": 200, "data": new})

def updateMakanan(id):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    makanan = Makanan.query.get(id)

    nama_makanan = request.form['nama_makanan']
    keterangan = request.form['keterangan']

    if 'image' not in request.files:
        resp = jsonify({"msg": "No body image attached in request"})
        resp.status_code = 501
        return resp
    fileImage = request.files['image']
    print(fileImage.filename)
    if fileImage.filename == '':
        resp = jsonify({'msg': "No file fileImage selected"})
        resp.status_code = 505
        return resp

    error = {}

    if fileImage and allowed_file(fileImage.filename):
        upload_result = cloudinary.uploader.upload(fileImage)
        print(upload_result["secure_url"])
        image = upload_result["secure_url"]
    else:
        error[fileImage.filename] = 'File type is not allowed'

    makanan.nama_makanan = nama_makanan
    makanan.keterangan = keterangan
    makanan.image = image

    db.session.commit()
    MakananUpdate = makananSchema.dump(makanan)
    return jsonify({"msg": "Success update makanan", "status": 200, "data": MakananUpdate})

def deleteMakanan(id):
    makanan = Makanan.query.get(id)
    db.session.delete(makanan)
    db.session.commit()
    MakananDelete = makananSchema.dump(makanan)
    return jsonify({"msg": "Success Delete makanan", "status": 200, "data": MakananDelete})
