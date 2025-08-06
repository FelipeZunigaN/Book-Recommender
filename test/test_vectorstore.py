from book_recommender.vectorstore import get_vectorstore

def test_vectorstore_load():
    db = get_vectorstore()
    assert db is not None
    assert hasattr(db, "similarity_search")
