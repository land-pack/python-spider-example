import sys
sys.path.append("..")
from pymongo import MongoClient
from config import config

mc = MongoClient(config.get('MONGO_HOST'),config.get('MONGO_PORT'))
