import json
from pprint import pprint


def movie_info(movie, genres):

    # movie에서 원하는 요소만 추출
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    genre_info_dict = {}

    for key in key_list:
        genre_info_dict[key] = movie[key]

    # genre_ids를 genre_names로 변환한 값 새 리스트에 입력
    genre_name_list = []

    for genre in genre_info_dict['genre_ids']:
        for i in range(len(genres)):
            if genre == (genres[i])['id']:
                genre_name_list.append((genres[i])['name'])

    # names 추가 / ids 삭제
    genre_info_dict['genre_names'] = genre_name_list
    del genre_info_dict['genre_ids']

    return genre_info_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
