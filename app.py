from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['imdb']
collection = db['all_imdb_data']

def get_genres_list():
    
    # Get distinct genres from the collection
    genres = collection.distinct('genres')
    
    # Split the comma-separated genres and flatten the list
    all_genres = []
    for genre_list in genres:
        all_genres.extend(genre_list.split(','))
    
    # Remove duplicates and sort the genres
    unique_genres = sorted(set(all_genres))
    unique_genres = [g for g in unique_genres if g != 'Adult']
    print(unique_genres)
    return unique_genres

@app.route('/api/genres', methods=['GET'])
def get_genres():
    unique_genres = get_genres_list()
    return jsonify({'genres': unique_genres})

@app.route('/api/movies', methods=['GET'])
def get_movies():
    genre = request.args.get('genre')
    movies = collection.find({'genres': {'$regex': genre}, 'titleType': 'movie'}, {'_id': 1, 'title': 1}).limit(10000).sort('title', 1)
    movies_list = [{'id': str(movie['_id']), 'title': movie['title']} for movie in movies]
    return jsonify({'movies': movies_list})

@app.route('/api/movie/<movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = collection.find_one({'_id': ObjectId(movie_id)})
    if movie:
        movie_details = {
            'title': movie['title'],
            'genres': movie['genres'],
            'startYear': movie['startYear'],
            'averageRating': movie['averageRating'],
            'numVotes': movie['numVotes']
        }
        return jsonify({'movie': movie_details})
    else:
        return jsonify({'error': 'Movie not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)