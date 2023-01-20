import json


def dec_movies(movies):


    # movies의 id 추출
    id_list = []

    for i in range(len(movies)):
        id_list.append((movies[i])['id'])


    # id로 json파일 열고 release_date 추출
    rd_list = []

    for j in range(len(movies)):
        movie_open = open("data/movies/" + str(id_list[j]) + ".json", encoding='utf-8')
        movie_detail = json.load(movie_open)

        rd_list.append([(movie_detail)['release_date'], (movie_detail)['title']])


    # 12에 해당하는 값 찾고 title 출력
    dec_list = []

    for k in range(len(movies)):
        if (rd_list[k][0])[5:7] == '12':
            dec_list.append((rd_list[k][1]))
        else:
            pass

    return dec_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
