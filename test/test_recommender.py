import pandas as pd
from book_recommender.recommender import retrieve_semantic_recommendations
from book_recommender.data_loader import load_books
from book_recommender.vectorstore import get_vectorstore

books = load_books()
db = get_vectorstore()

def test_recommendation_returns_dataframe():
    query = "a story about adventure and friendship"
    results = retrieve_semantic_recommendations(db, books, query)
    assert isinstance(results, pd.DataFrame)
    assert not results.empty
    assert "title" in results.columns
