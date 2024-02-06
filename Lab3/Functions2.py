#1
def is_above_5_5(movie):
    return movie["imdb"] > 5.5

movie = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}
print(is_above_5_5(movie))
#2
def above_5_5_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
]
print(above_5_5_movies(movies))

#3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
# Example usage:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
]
category_name = "Thriller"
print(f"Movies in the category '{category_name}':")
print(movies_by_category(movies, category_name))

#4
def average_imdb_score(movies):
    total_imdb_score = sum(movie["imdb"] for movie in movies)
    return total_imdb_score / len(movies) if movies else 0

# Example usage:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
]

print("Average IMDB score:", average_imdb_score(movies))

#5
def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]
    total_imdb_score = sum(movie["imdb"] for movie in category_movies)
    return total_imdb_score / len(category_movies) if category_movies else 0

# Example usage:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
]

category_name = "Thriller"
print(f"Average IMDB score for movies in the category '{category_name}':")
print(average_imdb_score_by_category(movies, category_name))

