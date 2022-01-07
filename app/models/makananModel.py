from app import db
from sqlalchemy.sql import func


class Makanan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_makanan = db.Column(db.String(100))
    image = db.Column(db.String(200))
    keterangan = db.Column(db.Text)
    tanggal = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, nama_makanan, image, keterangan, tanggal):
        self.nama_makanan = nama_makanan
        self.image = image
        self.keterangan = keterangan
        self.tanggal = tanggal

