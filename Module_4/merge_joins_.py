import pandas as pd

movie_cols = ['movie_id','title']

movies = pd.read_table('u.item', sep='|' , header = None, names = movie_cols)