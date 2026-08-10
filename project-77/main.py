import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

movies_df = pd.read_csv('movies.csv')
print(movies_df.head())

"""In movies dataset we have year along with the title"""
"""So first we will extract year from the title and assign it to a new column"""

movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))', expand=True)
print(movies_df.head())

movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)', expand=True)
print(movies_df.head())

movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')  
print(movies_df.head())

movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())

movies_df['genres'] = movies_df.genres.str.split('|')
print(movies_df.head())

movies_copy = movies_df.copy()

for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1

print(movies_copy.head())

movies_copy = movies_copy.fillna(0)
movies_copy.head()

user_input = [

              {'title':'Grand Slam','rating':5.6},
              {'title':'Zero','rating':7},    
              {'title':'Jumanji','rating':8.5},
              {'title':'Toy Story','rating':4.5}

]

movies_input = pd.DataFrame(user_input)

print(movies_input)

#Add movieID to user input

#First we will filter selected movies from original dataset

input_id = movies_df[movies_df['title'].isin(movies_input['title'].tolist())]

#Merging the two datasets

movies_input = pd.merge(input_id, movies_input)

print(movies_input)

#Drop the unnecessary columns like genres and year

movies_input = movies_input.drop(['genres','year'], axis=1)

print(movies_input)

#Now we will check for same movies given in input in original dataset

movies_user = movies_copy[movies_copy['movieId'].isin(movies_input['movieId'].tolist())]

print(movies_user)

#Reset index of this dataset

movies_user = movies_user.reset_index(drop=True)

print(movies_user)

#Create a Genre Table out of this dataset

UserGenreTable = movies_user.drop(['movieId','title','genres','year'], axis=1)

print(UserGenreTable)

#dot product to get weights

UserProfile = UserGenreTable.transpose().dot(movies_input['rating'])

#User Profile for every genre

print(UserProfile)

#Create a genre table for every movie in original datset

GenreTable = movies_copy.set_index(movies_copy['movieId'])

print(GenreTable)

GenreTable = GenreTable.drop(['movieId','title','genres','year'], axis=1)

print(GenreTable.head())

#Final Recommendation value for each movie

Recommendation_df = ((GenreTable*UserProfile).sum(axis=1))/UserProfile.sum()

print(Recommendation_df.head())

#Sort the values to get movies with high recommendation values

Recommendation_df = Recommendation_df.sort_values(ascending=False)

print(Recommendation_df.head())

#Final recommendation table for movies

RecommendationTable = movies_df.loc[movies_df['movieId'].isin(Recommendation_df.head(20).keys())]

print(RecommendationTable)

