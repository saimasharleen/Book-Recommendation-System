import time

start = time.time()
# Compute the cosine similarity between each pair of items
from sklearn.metrics.pairwise import cosine_similarity
item_sim = cosine_similarity(df.T)

# Use the cosine similarity to estimate missing ratings
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if pd.isna(df.iloc[i, j]):
            item_ratings = df.iloc[i, :]
            similar_items = item_sim[j]
            df.iloc[i, j] = (similar_items * item_ratings).sum() / similar_items.sum()
# Compute RMSE for both solution
from sklearn.metrics import mean_squared_error

df_collaborative = pd.read_csv('utility_matrix_collaborative_based.csv')
df_content = pd.read_csv('utility_matrix_content_based.csv')

# RMSE for collaborative
rmse_collaborative = mean_squared_error(df, df_collaborative, squared=False)


# RMSE for content
rmse_content = mean_squared_error(df, df_content, squared=False)

# RMSE total
rmse_tot = rmse_collaborative + rmse_content

# Weights
w1 = 1 - rmse_content / rmse_tot
w2 = 1 - rmse_collaborative / rmse_tot

# Hybrid utility matrix
Ut_hybrid = w1 * df_content + w2 * df_collaborative

# Convert the matrix to a DataFrame
df_hybrid = pd.DataFrame(Ut_hybrid)

# Save the DataFrame to a CSV file
df_hybrid.to_csv('utility_matrix_hybrid.csv', index=False)
end = time.time()

print("Time taken: ", end - start)
import pandas as pd

df = pd.read_csv("utility_matrix_hybrid.csv")
memory_usage = df.memory_usage().sum() / 1024**2

print("Memory usage of the hybrid utility matrix: {:.2f} MB".format(memory_usage))
