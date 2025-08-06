import logging
from book_recommender.data_loader import load_books
from book_recommender.vectorstore import get_vectorstore
from book_recommender.recommender import recommend_books
from book_recommender.ui import launch_dashboard

logging.basicConfig(level=logging.INFO)

books = load_books()
db_books = get_vectorstore()

categories = ["All"] + sorted(books["simple_categories"].dropna().unique())
tones = ["All", "Happy", "Surprising", "Angry", "Suspenseful", "Sad"]

def callback(query, category, tone):
    return recommend_books(db_books, books, query, category, tone)

dashboard = launch_dashboard(callback, categories, tones)

if __name__ == "__main__":
    dashboard.launch()
