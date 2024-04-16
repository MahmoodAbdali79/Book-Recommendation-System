from numpy import load
import numpy as np
import pandas as pd

books = pd.read_csv("data/books.csv")

def recommend(book_name):
    pt = pd.read_csv('data\PivotTable.csv',  index_col=0)
    similarity_score = load('data\Re-Array.npy')

    index = np.where(pt.index==book_name)
    if len(index[0]) > 0:
        index = index[0][0]
        similarity_items = sorted(list(enumerate(similarity_score[index])), key=lambda x:x[1], reverse=True)[1:6]

    else:
        return None, None
    
    return [(pt.index[i[0]], books[books['Book-Title']==pt.index[i[0]]].iloc[0]['Image-URL-M']) for i in similarity_items ]



print(recommend('1984'))



