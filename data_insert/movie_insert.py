## 1. insert jsonfile
import json

# # 2. insert csvfile  
# import csv   
# import os                         
# import django  
# import sys

genre_list = ["미스터리", "공포", "멜로·로맨스", "뮤지컬", "드라마", "액션", "블록버스터", "범죄", "스릴러", "어드벤처",
              "공포", "SF", "가족", "다큐멘터리", "서부", "실화", "애니메이션", "느와르", "판타지", "코미디", "전쟁"]


with open('movie_data.json', 'r', encoding='utf-8') as f:
    movies = json.load(f)

new_list = []
for movie in movies:
    new_data = {"model":"movie.moviemodel"}  
    if movie["genre"]: 
        genres = movie["genre"].strip("[]").split(',')
        genre_int_list = []
        for genre in genres:
            genre_int = genre_list.index(genre.strip()) + 1
            genre_int_list.append(genre_int)
            print(genre_int_list)
        movie['genre'] = genre_int_list
    else:
        movie["genre"] = []
    new_data["fields"] = movie
    new_list.append(new_data)
            
    
with open('movie_data.json', 'w', encoding='utf-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
    
  
  

  





