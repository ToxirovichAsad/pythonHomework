import requests
import random
import os

# Set your TMDB API Key here (or use an environment variable)
API_KEY = os.getenv("TMDB_API_KEY", "28104f570ce35e4530355e5a12525435")
BASE_URL = "https://api.themoviedb.org/3"

def get_genres():
    """Fetch available movie genres from TMDB."""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json().get("genres", [])
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Error fetching genres.")
        return {}

def get_movies_by_genre(genre_id):
    """Fetch movies for a given genre ID from TMDB."""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get("results", [])
        return movies
    else:
        print("Error fetching movies.")
        return []

def main():
    genres = get_genres()
    if not genres:
        return

    print("\nAvailable Genres:")
    for genre in genres.keys():
        print(f"- {genre.capitalize()}")

    while True:
        user_genre = input("\nEnter a genre (or type 'exit' to quit): ").strip().lower()
        if user_genre == "exit":
            print("Goodbye!")
            break
        
        if user_genre not in genres:
            print("Invalid genre. Please enter a valid genre from the list.")
            continue
        
        genre_id = genres[user_genre]
        movies = get_movies_by_genre(genre_id)
        
        if not movies:
            print("No movies found for this genre. Try another genre.")
            continue
        
        recommended_movies = random.sample(movies, min(10, len(movies)))  
        print(f"\nRecommended Movies in {user_genre.capitalize()} Genre:")
        for idx, movie in enumerate(recommended_movies, start=1):
            print(f"{idx}. {movie['title']} ({movie.get('release_date', 'Unknown')})")

if __name__ == "__main__":
    main()
