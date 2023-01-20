import json


def max_revenue(movies):
        
    # movies의 id 추출
    id_list = []

    for i in range(len(movies)):
        id_list.append((movies[i])['id'])


    # id로 json파일 열고 revenue 추출
    rv_list = []

    for j in range(len(movies)):
        movie_open = open("data/movies/" + str(id_list[j]) + ".json", encoding='utf-8')
        movie_detail = json.load(movie_open)

        rv_list.append((movie_detail)['revenue'])


    # max_revenue에 해당하는 id 찾고 title 출력
    for k in range(len(movies)):
        if rv_list[k] == max(rv_list):
            id_max = k
        else:
            pass


    movies_max_rv = open("data/movies/" + str(id_list[id_max]) + ".json", encoding='utf-8')
    movies_max = json.load(movies_max_rv)

    return movies_max['title']
    
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
