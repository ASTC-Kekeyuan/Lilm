from main import app, db
from model import *

@app.route('/query/all')
def queryall():
    rlt = Booklist.query_all()
    a = []
    for i in rlt :
        a.append(i.isbn)
    return str(a)
