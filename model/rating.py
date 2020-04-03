from main import db


class Rating(db.Model):
    __tablename__ = 'rating'

    isbn = db.Column(db.String(13), primary_key=True)
    count = db.Column(db.Integer)
    info = db.Column(db.String(24))
    star_count = db.Column(db.Float)
    value = db.Column(db.Float)

    @staticmethod
    def by_isbn(isbn):
        return db.session.query(Rating).filiter(Rating.isbn == isbn).one()