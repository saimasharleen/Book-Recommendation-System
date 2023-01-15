import pandas as pd
from faker import Faker
import random

# create an instance of the faker generator
fake = Faker()

# create a list to store the generated data
data = []

# generate data for 80000 users
for _ in range(80000):
    user_id = fake.random_int(min=1, max=80000)
    query_id = fake.random_int(min=1, max=1000)
    rating = None if random.random() < 0.2 else fake.random_int(min=1, max=100)
    data.append({'userId': user_id, 'queryId': query_id, 'rating': rating})

# convert the list to a dataframe
df = pd.DataFrame(data)

# save the dataframe to a csv file
df.to_csv("fake_data_missing_ratings.csv", index=False)

