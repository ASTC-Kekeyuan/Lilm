from main import app, db
from model import *
from get import get


@app.route('/add/isbn/<isbn>')
def addisbn(isbn):
    try:
        a = get(isbn)
        booklist: Booklist = Booklist()
        booklist.cover_url = a['cover_url']
        booklist.isbn = isbn
        booklist.name = a['title']
        db.session.add(booklist)
        detail: Details = Details()
        detail.isbn = isbn
        detail.abstract = a['abstract']
        detail.author_intro = a['author_intro']
        detail.book_intro = a['book_intro']
        detail.catalog = a['catalog']
        detail.labels = str(a['labels'])
        detail.url = a['url']
        db.session.add(detail)
        rating: Rating = Rating()
        rating.isbn = isbn
        rating.count = a['rating']['count']
        rating.info = a['rating']['rating_info']
        rating.star_count = a['rating']['star_count']
        rating.value = a['rating']['value']
        db.session.add(rating)
        db.session.commit()
    except:
        return "0"  # Failed
    else:
        return "1"  # Success
