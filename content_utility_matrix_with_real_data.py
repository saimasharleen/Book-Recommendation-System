import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Read in the utility matrix
df = pd.read_csv('utility_matrix.csv')
df.fillna(0, inplace=True)  # Replace NaN values with 0

cosine_sim = cosine_similarity(df, dense_output=False)

# Define the number of closest neighbors to use
k = 10

# Next, fill in missing values with estimated values using the cosine similarity matrix
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if pd.isna(df.iloc[i, j]):
            user_ratings = df.iloc[i, :]
            item_ratings = df.iloc[:, j]
            user_ratings = user_ratings[~pd.isna(user_ratings)]
            item_ratings = item_ratings[~pd.isna(item_ratings)]
            # subtract the mean rating of each user and item
            mean_user_rating = user_ratings.mean()
            mean_item_rating = item_ratings.mean()
            user_ratings -= mean_user_rating
            item_ratings -= mean_item_rating
            similar_users = cosine_sim[i][~pd.isna(df.iloc[:, j])]
            similar_items = cosine_sim[j][~pd.isna(df.iloc[i, :])]
            # get the k closest neighbors
            top_k_users = similar_users.argsort()[-k:]
            top_k_items = similar_items.argsort()[-k:]
            similar_users = similar_users[top_k_users]
            similar_items = similar_items[top_k_items]
            item_ratings = item_ratings[top_k_items]
            df.iloc[i, j] = mean_item_rating + mean_user_rating + (sum(similar_users * similar_items * item_ratings) / sum(similar_users * similar_items))

# save the filled matrix to csv
df.to_csv('utility_matrix_content_based.csv', index=False)
