import pandas as pd

def retrieve_semantic_recommendations(db_books, books, query, category="All", tone="All",
                                      initial_top_k=50, final_top_k=16):
    recs = db_books.similarity_search(query, k=initial_top_k)
    books_list = [int(rec.page_content.strip('"').split()[0]) for rec in recs]
    book_recs = books[books["isbn13"].isin(books_list)].head(initial_top_k)

    if category != "All":
        book_recs = book_recs[book_recs["simple_categories"] == category].head(final_top_k)
    else:
        book_recs = book_recs.head(final_top_k)

    tone_map = {
        "Happy": "joy",
        "Surprising": "surprise",
        "Angry": "anger",
        "Suspenseful": "fear",
        "Sad": "sadness"
    }

    if tone in tone_map:
        book_recs = book_recs.sort_values(by=tone_map[tone], ascending=False)

    return book_recs

def recommend_books(db_books, books, query, category, tone):
    recs = retrieve_semantic_recommendations(db_books, books, query, category, tone)
    results = []

    for _, row in recs.iterrows():
        description = row["description"]
        desc = " ".join(description.split()[:30]) + "..."

        authors = row["authors"].split(";")
        authors_str = (
            f"{authors[0]} and {authors[1]}" if len(authors) == 2 else
            f"{', '.join(authors[:-1])}, and {authors[-1]}" if len(authors) > 2 else
            row["authors"]
        )

        caption = f"{row['title']} by {authors_str}: {desc}"
        results.append((row["large_thumbnail"], caption))

    return results
