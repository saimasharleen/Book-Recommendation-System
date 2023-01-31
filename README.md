# Book Recommendation System based on query logs

**UniTn Data Mining Course Project 2023**

At the center of the problem is a relational table of books, a user set, a query set, and a User-Query utility matrix should be required inputs for our approach.
- A relational table that contains tuples. The first row is composed of the names of the main book attributes (’bookID’, ’title’, ’authors’, ’average_rating’, ’isbn’, ’isbn13’, ’language_code’, ’num_pages’, ’ratings_count’, ’text_reviews_count’, ’publication_date’, ’publisher’ in our case), while the following ones enclose a tuple that contain specific realizations of each attribute
- A query set as a union of tuples. In this dataset the first column contains the query identifier (a number in our case). Instead each following column contain the tuples that compose the query. Here, a generic query, 𝑞𝑗 could be as follows: 𝑞189 =< 𝑙𝑎𝑛𝑔𝑢𝑎𝑔𝑒 = 𝐸𝑛𝑔𝑙𝑖𝑠ℎ, 𝑡𝑖𝑡𝑙𝑒 = 𝑇ℎ𝑒_𝐴𝑙𝑐ℎ𝑒𝑚𝑖𝑠𝑡 >. As can be seen, each condition consists of an attribute and the attribute’s manifestation. Notice that in this paper, we are going to consider queries with one to four criteria.
- A set of users 𝑢1, ...𝑢𝑛 as an identifier vectors.
- A rating ranging from 1 to 100, where 1 indicates that the user dislikes the condition fully and 100 indicates that the user likes the query completely. In other words, this indicates the amount of pleasure each user has with the query’s results
- The utility matrix as a matrix with users as rows and queries as columns. The entries consist of ratings from users. In our datasets, items may be null, indicating that the user did not perform the specified query.
#

**Implementations:**
  - [Hybrid Filtering For Real Dataset](https://github.com/saimasharleen/Book-Recommendation-System/blob/main/hybrid_utility_matrix_real.py)
  - [Recommended Queries For Real Dataset](https://github.com/saimasharleen/Book-Recommendation-System/blob/main/recommended_queries_for_real_dataset)
  - [Utility of a Query For Real Dataset](https://github.com/saimasharleen/Book-Recommendation-System/blob/main/utility_of_a_query_real.py)
  - [Hybrid Filtering, Recommended Queries and Utility of a Query For Real Dataset](https://github.com/saimasharleen/Book-Recommendation-System/blob/main/lastdatamining_withrandomdataset.ipynb)
# 
**Dataset sources**: 
- [Created a random data generator using **Python**](https://github.com/saimasharleen/Random_Generated_Data_Book)
- [Web Scrapping using Python](https://github.com/saimasharleen/Book-Data-Generator)
#

**Detailed Report**: 
- [Link]()
### Built With
* [Python][ https://www.python.org/ ][ Python-url]
* [Google Colab Pro] [https://colab.research.google.com/] [Colab-url]
