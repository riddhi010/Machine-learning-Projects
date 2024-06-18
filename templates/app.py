from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load movies and ratings data
ratings = pd.read_csv(r'C:\Users\SHRENIK\Downloads\archive (1)/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
movies = pd.read_csv(r'C:\Users\SHRENIK\Downloads\archive (1)/u.item', sep='|', encoding='latin-1', header=None, names=['movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_URL',
                                                                                                             'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film_Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci_Fi', 'Thriller', 'War', 'Western'])

# List of genres
genres = ['unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film_Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci_Fi', 'Thriller', 'War', 'Western']

# Function to recommend movies from user's favorite genre
def recommend_movies_by_genre(favorite_genre, top_n=5):
    # Filter movies by the user's favorite genre
    genre_movies = movies[movies[favorite_genre] == 1]

    if genre_movies.empty:
        return []

    # Merge with ratings to get average rating for each movie in the genre
    genre_movie_ratings = pd.merge(genre_movies, ratings, left_on='movie_id', right_on='item_id')
    genre_movie_ratings = genre_movie_ratings.groupby('movie_title')['rating'].mean().reset_index()

    # Sort movies by average rating in descending order
    genre_movie_ratings = genre_movie_ratings.sort_values(by='rating', ascending=False)

    # Get top-rated movies
    top_movies = genre_movie_ratings.head(top_n)['movie_title'].tolist()

    return top_movies

# Route for home page
@app.route('/')
def home():
    return render_template('index.html', genres=genres)

# Route for handling movie search and recommendation
@app.route('/recommendations', methods=['POST'])
def recommendations():
    try:
        favorite_genre = request.form['genre']
        num_recommendations = int(request.form['num_recommendations'])
    except KeyError as e:
        return f"Missing form parameter: {e}", 400
    except ValueError:
        return "Invalid input for number of recommendations", 400

    recommended_movies = recommend_movies_by_genre(favorite_genre, num_recommendations)
    return render_template('recommendations.html', genre=favorite_genre, recommendations=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
