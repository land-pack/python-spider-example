from pymongo import Connection

conn = Connection("192.168.41.54",27017)

db = conn.crazy_bet

db.authenticate("crazy_bet_rw","crazy_bet_rw")

