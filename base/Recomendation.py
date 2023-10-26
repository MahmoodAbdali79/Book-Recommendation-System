from numpy import load
import numpy as np
import pandas as pd
import os
import pdb

def recommend(book_name):
    pt = pd.read_csv('base\data-model\PivotTable.csv',  index_col=0)
    similarity_score = load('base\data-model\Re-Array.npy')

    index = np.where(pt.index==book_name)
    if len(index[0]) > 0:
        index = index[0][0]
        similarity_items = sorted(list(enumerate(similarity_score[index])), key=lambda x:x[1], reverse=True)[1:6]
    else:
        return None
    
    return "-".join([pt.index[i[0]] for i in similarity_items ])



