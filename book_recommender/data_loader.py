import pandas as pd
import numpy as np
from .config import DATA_PATH

def load_books():
    books = pd.read_csv(DATA_PATH)
    books["large_thumbnail"] = books['thumbnail'] + "&fife=w800"
    books["large_thumbnail"] = np.where(
        books['large_thumbnail'].isna(),
        "cover-not-found.jpg",
        books["large_thumbnail"]
    )
    return books
