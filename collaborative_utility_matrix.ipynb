import pandas as pd
import numpy as np

# Read in the utility matrix
df = pd.read_csv('utility_matrix.csv')
df = df.fillna(df.mean())

# Compute the Pearson correlation coefficient between each pair of users
user_corr = df.corr(method='pearson')

# Define the number of closest neighbors to use for filling in missing values
k = 5  # for example

# Fill in missing values with estimated values using collaborative filtering with Pearson correlation
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if pd.isna(df.iloc[i, j]):
            user_ratings = df.iloc[i, :]
            item_ratings = df.iloc[:, j]
            user_ratings = user_ratings[~pd.isna(user_ratings)]
            item_ratings = item_ratings[~pd.isna(item_ratings)]
            similar_users = user_corr[i][~pd.isna(df.iloc[:, j])]
            # Sort the similar users by Pearson correlation coefficient
            similar_users = similar_users.sort_values(ascending=False)
            # Use only the top k similar users
            similar_users = similar_users[:k]
            df.iloc[i, j] = (similar_users * item_ratings).sum() / similar_users.abs().sum()

# save the filled matrix to csv
df.to_csv('utility_matrix_collaborative_based.csv', index=False)
