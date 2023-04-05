# Peer Review
<hr>

### Shikhar's

#### 1. Load 

- He is using mongoimport and subprocess to load data to the file 

#### 2. Comments

- ``` query1 ``` function executes an aggregation query on the comments collection to group the comments by the commenter's name, sort them in descending order based on the count of comments, and limit the result to the top 10 commenters. The function then prints the result.
- ``` query2 ``` function executes an aggregation query on the comments collection to group the comments by the movie_id field, sort them in descending order based on the count of comments, and limit the result to the top 10 movies. The function then prints the result.
- ``` query3 ``` the function executes an aggregation query on the comments collection to group the comments by the month in which they were made and count the number of comments made in each month. The function then prints the result.

### 3. Movies

- ```query11(n)```: This function takes an integer n as input and returns the top n movies with highest IMDb ratings. It queries the MongoDB database myDB and sorts the movies by their imdb.rating field in descending order.
- ```query12(year)```: This function takes an integer year as input and returns the highest IMDb rating for movies released in that year. It queries the MongoDB database myDB and groups the movies by their year field, then finds the maximum imdb.rating for each group.
​- ```query13()```: This function returns the highest IMDb rating for movies with more than 10,000 votes. It queries the MongoDB database myDB and filters the movies by their imdb.rating and imdb.votes fields, then finds the maximum imdb.rating.
- ```query14(pattern)```: This function takes a string pattern as input and returns the top 10 movies whose titles match the regular expression pattern, sorted by their tomatoes.viewer.rating field in descending order. It queries the MongoDB database myDB and uses the $regex operator to match the title field with the input pattern, and then sorts the results by the tomatoes.viewer.rating field.
- ```query21()```: This function returns the number of movies directed by each director in the database. It queries the MongoDB database myDB, groups the movies by their directors field using $unwind and $group operators, and sorts the results by the count of movies for each director.
- ```query22(year)```: This function takes an integer year as input and returns the director who directed the most movies in that year. It queries the MongoDB database myDB, filters the movies by their year field, groups the movies by their directors field using $unwind and $group operators, and finds the director with the highest count of movies.
- ```query23(genre)```: This function takes a string genre as input and returns the director who directed the most movies in that genre. It queries the MongoDB database myDB, filters the movies by their genres field, groups the movies by their directors field using $unwind and $group operators, and finds the director with the highest count of movies.
- ```query31(n)```: This function takes an integer n as input and returns the top n most frequently appearing actors in the database. It queries the MongoDB database myDB, groups the movies by their cast field using $unwind and $group operators, and sorts the results by the count of movies for each actor.
- ```query32(year,n)```: This function takes an integer year and an integer n as input and returns the top n most frequently appearing actors in movies released in that year. It queries the MongoDB database myDB, filters the movies by their year field, groups the movies by their cast field using $unwind and $group operators, and sorts the results by the count of movies for each actor.
- ```query33(genre,n)```: This function takes a string genre and an integer n as input and returns the top n most frequently appearing actors in movies of that genre. It queries the MongoDB database myDB, filters the movies by their genres field, groups the movies by their cast field using $unwind and $group operators.

### Comments

- ```query11()```: This function performs an aggregation query on the "theaters" collection to group the data by the city field in the location.address subdocument, count the number of documents in each group, sort the result in descending order of the count, and return only the top 10 results.
- ```query12()```: This function performs a geospatial aggregation query using the $geoNear operator to find the documents in the "theaters" collection that are closest to a specified location, which is represented by a longitude-latitude pair.