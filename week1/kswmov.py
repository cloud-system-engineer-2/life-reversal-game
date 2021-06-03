#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#사용자 이름을 입력받음
#좋아하는 영화 태그 입력박음
#좋아할만한 영화를 출력
#파일로 저장할까요? Y/N
#파일로 저장
def input_name():
    user_Name=input("사용자 이름을 입력해주세요 ")
    return user_Name
def input_tag(user_Name):
    favorite_tag=input(user_Name+"님의 좋아하는 영화 태그를 입력해주세요 ")
    return favorite_tag

def make_favorite_movie_list(movie_List,favorite_Tag,favorite_Movie_List):
    for movie in movie_List:
        if favorite_Tag in movie["tags"]:
            favorite_Movie_List.append(movie["title"])
            print(movie["title"])
    

def movielist_save(user_Name,favorite_Movie_List):        
    if len(favorite_Movie_List)!=0:
        file_save= input("좋아하는 영화 목록을 파일로 저장할까요? Y/N ")
        if file_save=="N" :
            print("다음에 다시 만나요!")
        elif file_save=="Y":
            with open( "{}movie.txt".format(user_Name),"w") as file:
                file.write(user_Name)
                file.write("님이 좋아할만한 영화목록\n")
                for favorite_movie in favorite_Movie_List:
                    file.write(favorite_movie)
                    file.write("\n")
                print("저장완료")
    else :
        print("원하시는 영화가 아직 없어요")
    
        
movie1={"title": "미나리",
       "tags": ["한국","드라마","미국","1980년대","시골","가족","감동"]}
movie2={"title": "인셉션",
       "tags": ["미국","SF","가족","추격","액션"]}
movie3={"title": "설국열차",
       "tags": ["한국","SF","미국","미래","액션","가족"]}
movie4={"title": "리미트리스",
       "tags": ["미국","SF","추격","현대"]}
movie5={"title": "원스",
       "tags": ["아일랜드","드라마","아일랜드","음악","로맨스","감동"]}
movie6={"title": "악인전",
       "tags": ["한국","액션","스릴","2000년대","조폭","경찰","잔인"]}

movie_list = [movie1, movie2,movie3,movie4,movie5,movie6]

favorite_movie_list=[]

user_name=input_name()

favorite_tag=input_tag(user_name)

make_favorite_movie_list(movie_list,favorite_tag,favorite_movie_list)

movielist_save(user_name,favorite_movie_list)

