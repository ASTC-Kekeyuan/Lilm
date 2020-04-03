from main import db


class Booklist(db.Model):
    __tablename__ = "booklist"
    isbn = db.Column(db.String(13), primary_key=True)
    # ISBN
    name = db.Column(db.String(128))
    # 书名
    cover_url = db.Column(db.String(96))
    # 封面URL

    @staticmethod
    def query_all():
        return db.session.query(Booklist).all()