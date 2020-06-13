from main import db


class Details(db.Model):
    __tablename__ = 'details'

    isbn = db.Column(db.String(13), primary_key=True)
    abstract = db.Column(db.Text)
    book_intro = db.Column(db.Text)
    author_intro = db.Column(db.Text)
    catalog = db.Column(db.Text)
    labels = db.Column(db.Text)
    url = db.Column(db.String(96))

    @staticmethod
    def by_isbn(isbn):
        return db.session.query(Details).filter(Details.isbn == isbn).one()