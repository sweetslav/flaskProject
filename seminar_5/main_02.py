# Задание №2.
# Создать API для получения списка фильмов по жанру.
# Приложение должно иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

from typing import Optional, List

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Optional[str] = None


movies = [
    Movie(id=1, title="Taxi", description="Description 1", genre='comedy'),
    Movie(id=2, title="Matrix", description="Description 2", genre='fantasy'),
    Movie(id=3, title="Five Element", description="Description 3", genre='fantasy'),
    Movie(id=4, title="Qwerty", description="Description 4", genre='love'),
    Movie(id=5, title="Asdfghjkl", description="Description 5", genre='comedy'),
    Movie(id=6, title="Zxcvbn", description="Description 6", genre='love')
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie API!"}


@app.get("/movies/", response_model=List[Movie], tags=["movies"])
def read_movies():
    return movies


@app.get("/movies/{genre}", response_model=List[Movie], tags=["movies"])
def read_movies_by_genre(genre: str):
    filtered_movies = [movie for movie in movies if movie.genre == genre]
    if not filtered_movies:
        raise HTTPException(status_code=404, detail=f"No movies found with genre {genre}")
    return filtered_movies


@app.post("/movies/", response_model=Movie, tags=["movies"])
def create_movie(movie: Movie = Depends()):
    movies.append(movie)
    return movie


@app.put("/movies/{movie_id}", response_model=Movie, tags=["movies"])
def update_movie(movie_id: int, movie: Movie = Depends()):
    for index, m in enumerate(movies):
        if m.id == movie_id:
            movies[index] = movie
            return movie
    raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")


@app.delete("/movies/{movie_id}", tags=["movies"])
def delete_movie(movie_id: int):
    for index, m in enumerate(movies):
        if m.id == movie_id:
            del movies[index]
            return {"message": f"Movie with id {movie_id} deleted"}
    raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")
