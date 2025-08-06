from book_recommender.data_loader import load_books

def test_load_books():
    books = load_books()
    assert not books.empty, "Book's DataFrame should not be empty"
    assert "title" in books.columns, "Missing 'title' column"
    assert "large_thumbnail" in books.columns, "Missing 'large_thumbnail' column"