import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:aipenpass123@localhost:5432/africaapigeo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "dev-key-africa-geo"