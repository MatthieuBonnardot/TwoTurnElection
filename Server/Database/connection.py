from webbrowser import get
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@twoturncluster.jej2t.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


def getMongoClient(col):
    db = client['TwoTurn']
    return db[col]
