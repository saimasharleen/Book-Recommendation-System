import time

start = time.time()
import csv

def calculate_utility(r_tij, r_ehj, L, K):
    R_tj = sum(r_tij) / L
    R_ej = sum(r_ehj) / K
    W_tj = L / (L + K)
    W_ej = K / (L + K)
    if L < K:
        W_tj = 1 - W_ej
    U_j = W_tj * R_tj + W_ej * R_ej
    return U_j

# Number of users and queries
num_users = 1000
num_queries = 10000

# Read the ratings from the CSV file
with open("ratings.csv", "r") as file:
    reader = csv.reader(file)
    # Skip the header
    next(reader)
    # Store the ratings in a list
    ratings = [row[1:] for row in reader]

# Initialize a list to store the utility values
utility_values = []

# Loop through the queries
for j in range(num_queries):
    # Initialize lists to store the ratings for the target users and external users
    r_tij = []
    r_ehj = []
    # Loop through the ratings for each user
    for i in range(num_users):
        if i % 2 == 0:
            # Store the rating for a target user
            r_tij.append(int(ratings[i][j]))
        else:
            # Store the rating for an external user
            r_ehj.append(int(ratings[i][j]))
    L = len(r_tij)
    K = len(r_ehj)
    # Compute the utility for the current query
    utility = calculate_utility(r_tij, r_ehj, L, K)
    utility_values.append(utility)

# Print the utility values for each query
print(utility_values)
import csv

# Define header for the CSV file
header = ["query_id", "utility_value"]

# Convert the utility_values list to a list of lists
utility_values_rows = [[i, value] for i, value in enumerate(utility_values)]

# Write the results to a CSV file
with open("utility_values.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(header)
    # Write the results
    writer.writerows(utility_values_rows)
end = time.time()

print("Time taken: ", end - start)

import pandas as pd

df = pd.read_csv("ratings.csv")
memory_usage = df.memory_usage().sum() / 1024**2

print("Memory usage of the utility of a query: {:.2f} MB".format(memory_usage))
