# Peer Review

### Shikhar's

#### 1. Load 

- He is using mongoimport and subprocess to load data to the file 

#### 2. Comments

- ``` query1() ``` function executes an aggregation query on the comments collection to group the comments by the commenter's name, sort them in descending order based on the count of comments, and limit the result to the top 10 commenters. The function then prints the result. This function is well-implemented and should work as expected.
- ``` query2() ``` function executes an aggregation query on the comments collection to group the comments by the movie_id field, sort them in descending order based on the count of comments, and limit the result to the top 10 movies. The function then prints the result. This function is well-implemented and should work as expected.
- ``` query3() ``` the function executes an aggregation query on the comments collection to group the comments by the month in which they were made and count the number of comments made in each month. The function then prints the result. This function is well-implemented and should work as expected.

#### 3. Movies

- ```query11(n)```: This function takes an integer n as input and returns the top n movies with highest IMDb ratings. It queries the MongoDB database myDB and sorts the movies by their imdb.rating field in descending order. This function is well-implemented and should work as expected.
- ```query12(year)```: This function takes an integer year as input and returns the highest IMDb rating for movies released in that year. It queries the MongoDB database myDB and groups the movies by their year field, then finds the maximum imdb.rating for each group. This function is well-implemented and should work as expected.
- ```query13()```: This function returns the highest IMDb rating for movies with more than 10,000 votes. It queries the MongoDB database myDB and filters the movies by their imdb.rating and imdb.votes fields, then finds the maximum imdb.rating. This function is well-implemented and should work as expected.
- ```query14(pattern)```: This function takes a string pattern as input and returns the top 10 movies whose titles match the regular expression pattern, sorted by their tomatoes.viewer.rating field in descending order. It queries the MongoDB database myDB and uses the $regex operator to match the title field with the input pattern, and then sorts the results by the tomatoes.viewer.rating field. This function is well-implemented and should work as expected.
- ```query21()```: This function returns the number of movies directed by each director in the database. It queries the MongoDB database myDB, groups the movies by their directors field using $unwind and $group operators, and sorts the results by the count of movies for each director. This function is well-implemented and should work as expected.
- ```query22(year)```: This function takes an integer year as input and returns the director who directed the most movies in that year. It queries the MongoDB database myDB, filters the movies by their year field, groups the movies by their directors field using $unwind and $group operators, and finds the director with the highest count of movies. This function is well-implemented and should work as expected.
- ```query23(genre)```: This function takes a string genre as input and returns the director who directed the most movies in that genre. It queries the MongoDB database myDB, filters the movies by their genres field, groups the movies by their directors field using $unwind and $group operators, and finds the director with the highest count of movies. This function is well-implemented and should work as expected.
- ```query31(n)```: This function takes an integer n as input and returns the top n most frequently appearing actors in the database. It queries the MongoDB database myDB, groups the movies by their cast field using $unwind and $group operators, and sorts the results by the count of movies for each actor. This function is well-implemented and should work as expected.
- ```query32(year,n)```: This function takes an integer year and an integer n as input and returns the top n most frequently appearing actors in movies released in that year. It queries the MongoDB database myDB, filters the movies by their year field, groups the movies by their cast field using $unwind and $group operators, and sorts the results by the count of movies for each actor. This function is well-implemented and should work as expected.
- ```query33(genre,n)```: This function takes a string genre and an integer n as input and returns the top n most frequently appearing actors in movies of that genre. It queries the MongoDB database myDB, filters the movies by their genres field, groups the movies by their cast field using $unwind and $group operators. This function is well-implemented and should work as expected.

#### 4. Theaters

- ```query11()```: This function performs an aggregation query on the "theaters" collection to group the data by the city field in the location.address subdocument, count the number of documents in each group, sort the result in descending order of the count, and return only the top 10 results. This function is well-implemented and should work as expected.
- ```query12()```: This function performs a geospatial aggregation query using the $geoNear operator to find the documents in the "theaters" collection that are closest to a specified location, which is represented by a longitude-latitude pair. This function is well-implemented and should work as expected.

<hr>

### Mohan's 

#### 1. Load

- ```create_collection_if_not_exits()```: This function takes a collection name as input and creates a new collection in the database if it does not already exist. It uses a try-except block to handle the case where the collection already exists. Overall, this function is a simple and useful utility that helps to avoid errors caused by trying to create a collection that already exists.
- ```import_documets_from_files()```: This function takes a database name, collection name, and file path as input and loads the data from the file into the specified collection in the database using the mongoimport command. This function is a great way to quickly load large amounts of data into a database from JSON files without having to write custom code to parse the files and insert the data.
- ```insert_record()```: This function takes a collection number as input and inserts a new record into the corresponding collection based on user input. The function prompts the user to enter data for each field in the record and then inserts the record into the collection using the insert_one() method. This function provides a simple way to insert new data into the database without having to write custom code for each collection.

#### 2. Movies 

- ```find_top_n_movies_with_the_highest_IMDB_rating()```: This function finds the top N movies with the highest IMDB rating by using an aggregation pipeline that matches movies with a non-empty IMDB rating, sorts them in descending order of rating, limits the results to the top N, and projects the title and IMDB rating fields. This function is a useful utility for quickly finding the top rated movies in the database.
- ```find_top_n_movies_with_the_highest_IMDB_rating_in_year()```: This function finds the top N movies with the highest IMDB rating in a given year by using a similar aggregation pipeline to the previous function, but also adds a match stage that filters the movies by the specified year. This function is a great way to find the top rated movies in a particular year.
- ```find_top_n_movies_with_the_highest_IMDB_rating_and_votes_greater_than_1000()```: This function is designed to find the top N movies based on their IMDB ratings, while also filtering out movies with less than 1000 votes. It works well and provides accurate results. The use of the aggregation pipeline makes it easy to understand and modify if needed.
- ```find_top_n_movies_with_title_matching_pattern_sorted_by_highest_tomatoes_ratings()```: This function is designed to find the top N movies whose titles match a given pattern, sorted by their highest Tomatoes ratings. It is a useful function for those who are looking for movies that fit a specific theme or genre. The function works well and provides accurate results. The use of the aggregation pipeline with regular expressions makes it easy to customize the search criteria.
- ```find_top_n_directors_with_maximum_no_of_movies()```: This function is designed to find the top N directors who created the maximum number of movies. It works well and provides accurate results. The use of the aggregation pipeline with the $unwind and $group stages makes it easy to understand and modify if needed. Overall, this function is a useful tool for those who want to know more about the most prolific directors in the film industry.
- ```find_top_n_directors_who_created_maximum_no_of_movies_in_an_year(year)```:
This function takes a year as input and finds the top N directors who created the maximum number of movies in that year. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N. Overall, this function seems to be well-implemented and should work as expected.
- ```find_top_n_directors_who_created_maximum_no_of_movies_in_given_genre(genre)```:
This function takes a genre as input and finds the top N directors who created the maximum number of movies in that genre. It also uses MongoDB's aggregation pipeline to perform the required queries. Similar to the previous function, the user is prompted to enter the value of N. This function seems to be a good implementation and should work as expected.
- ```find_top_n_actors_with_maximum_no_of_movies()```:
This function finds the top N actors who starred in the maximum number of movies. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N. This function is well-implemented and should work as expected.
- ```find_top_n_actors_with_maximum_no_of_movies_in_given_year(year)```:
This function takes a year as input and finds the top N actors who starred in the maximum number of movies in that year. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N. This function also seems to be well-implemented and should work as expected.
- ```find_top_n_actors_with_maximum_no_of_movies_in_give_genre(genre)```:
This function takes a genre as input and finds the top N actors who starred in the maximum number of movies in that genre. It also uses MongoDB's aggregation pipeline to perform the required queries. The user is prompted to enter the value of N. This function is also well-implemented and should work as expected.
- ```top_n_movies_for__every_genre()```:
This function finds the top N movies for each genre with the highest IMDB rating. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N for each genre. This function seems to be well-implemented and should work as expected.

#### 3. Comments

- ```top10_users_with_max_number_of_comments()```:
This function finds the top 10 users who made the maximum number of comments. It uses MongoDB's aggregation pipeline to perform the required queries. The function returns the results in the form of an iterator. This function is well-implemented and should work as expected.
- ```top10_movies_With_most_comment()```:
This function finds the top 10 movies with the most comments. It uses MongoDB's aggregation pipeline to perform the required queries. The function returns the results by printing the title and number of comments for each movie. This function seems to be well-implemented and should work as expected.
- ```month_wise_comment(year)```:
This function retrieves the count of comments made in each month of a given year from a MongoDB database using an aggregation pipeline. The pipeline projects the year and month from the date field, filters the documents by the given year, groups the comments by month and counts the number of comments in each group. The function then prints the results as a list. Overall, the function seems well-written and efficient.

#### 4. Theaters

- ```top10_cities_most_theaters()```:
This function retrieves the top 10 cities with the highest number of theaters from a MongoDB database using an aggregation pipeline. The pipeline groups the theaters by city, counts the number of theaters in each group, sorts the groups in descending order by the count, and limits the results to the top 10. The function then prints the results as a list. This function also seems well-written and efficient.
- ```top10_theaters_near(coordinates)```:
This function retrieves the top 10 theaters that are nearest to a given set of coordinates from a MongoDB database using a geospatial query. The function first creates a 2dsphere index on the location.geo field of the theaters collection to optimize the query. Then it constructs a query using the $near operator and the given coordinates to find the theaters closest to the coordinates. Finally, it limits the results to the top 10 and prints them as a list. This function also seems well-written and efficient.
