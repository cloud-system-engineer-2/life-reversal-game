#!/usr/bin/env python
# coding: utf-8

# In[2]:


number_input_a= int (input("정수를 입력>"))
print("원의반지름 : ",number_input_a)
print("원의둘레 : ",2*3.14*number_input_a)
print("원의넓이 : ",3,14*number_input_a*number_input_a)


# 예외처리의 기본 try except

# if 조건문을 써서 예외 처리 해볼 수 있긴함

# In[ ]:


print("원의둘레 : ",2*3.14*number_input_a)


# In[3]:


user_input_a= input("정수를 입력>")

if user_input_a.isdigit():
    number_input_a= int (user_input_a)
    print("원의반지름 : ",number_input_a)
    print("원의둘레 : ",2*3.14*number_input_a)
    print("원의넓이 : ",3,14*number_input_a*number_input_a)
else:
    print("정수를 입력해야합니다")


# 1. syntax error 문법 오류 >> 아예 실행이 안됨
# 
# 2. runtime error / exception 
# 
# 실행전에는 체크가 안됨 내PC에서만 되고 다른데에선 안됨
# 
# 실행중에 발생하는 에러 
# 
# 심각도에 따라 나뉨 
# 
# 심각하면 프로그램 종료됨
# 
# 덜심각한것을 예외처리해서 프로그램 종료는 안하게 함
# 
# 3. 논리 오류  아예 프로그램 잘못 짠것, 제일 찾기 어려움
# 

# In[5]:


try:
    number_input_a= int (input("정수를 입력>"))
    print("원의반지름 : ",number_input_a)
    print("원의둘레 : ",2*3.14*number_input_a)
    print("원의넓이 : ",3,14*number_input_a*number_input_a)
except :
    pass # 아무것도 하기 싫으면 pass를 써야함 빈줄 쓰면 오류남
    #    print("무언가 잘못되었습니다.")

print("다음코드")


# In[6]:


try:
    number_input_a= int (input("정수를 입력>"))

except : # 예외 발생시 실행되는 코드
    pass # 아무것도 하기 싫으면 pass를 써야함 빈줄 쓰면 오류남
    #    print("무언가 잘못되었습니다.")
else:# 예외 발생하지 않았을때 실행되는 코드
    print("원의반지름 : ",number_input_a)
    print("원의둘레 : ",2*3.14*number_input_a)
    print("원의넓이 : ",3,14*number_input_a*number_input_a)
print("다음코드")


# In[6]:


try:
    number_input_a= int (input("정수를 입력>"))
    print(정수를 입력하지 않았습니다 잘못되었습니다.")
    print("원의반지름 : ",number_input_a)
    print("원의둘레 : ",2*3.14*number_input_a)
    print("원의넓이 : ",3,14*number_input_a*number_input_a)
except : # 예외 발생시 실행되는 코드
    print("정수를 입력하지 않았습니다")
else:# 예외 발생하지 않았을때 실행되는 코드
    print("예외가 발생하지 않았습니다")
finally:#예외 발생여부와 상관없이 실행되는 코드
    print("일단 프로그램이 끝났습니다")
print("다음코드")


# In[8]:


try:
    file=open("info.txt" ,"w")
    file.close()
except Exception as e:
    pritn(e)
print("file closed : ",file.closed)


# In[12]:


try:
    file=open("info.txt" ,"w")
    예외.발생()
except Exception as e:
    print(e)
#finally:  ##finally 안써도 됨 그러나 코드도 정리되고 코드종결되도 실행
file.close()
print("file closed : ",file.closed)


# In[13]:


try:
    print(1)
    print(2)
except:
    print(3)
finally:
    print(4)
print(5)


# In[16]:


def test():    
    try:
        print(1)
        print(2)
        return        #이렇게 구현했을때  1,2,4   return은 함수의 종결의미
    except:
        print(3)
    finally:      #함수가 종결되도 실행되는 것
        print(4)
    print(5)       
test()


# 구문오류와 예외의 차이
# 
# 문법오류는 실행전에 찾아낼수있는 오류지만
# 
# 예외의 경우 실행해야만 알 수 있으며 프로그램을 종료시키지는 않는다.
# 
# 

# In[18]:


numbers=[52, 273, 32, 103,90,10,275]

print("#(1)요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다".format(52,numbers.index(52)))
print()

print("#(2)요소 내부에 없는 값 찾기 ")
number= 10000
if number in numbers:
    print("- {}는 {} 위치에 있습니다".format(number,numbers.index(number)))
else:
    print("-리스트 내부에 없는 값입니다.")
print()

print("-----------정상적으로 종료되었습니다---------------")


# In[19]:


numbers=[52, 273, 32, 103,90,10,275]

print("#(1)요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다".format(52,numbers.index(52)))
print()

print("#(2)요소 내부에 없는 값 찾기 ")
number= 10000
try:
    print("- {}는 {} 위치에 있습니다".format(number,numbers.index(number)))
except:
    print("-리스트 내부에 없는 값입니다.")
print()

print("-----------정상적으로 종료되었습니다---------------")


# In[21]:


output=10 +"개" #데이터타입이 서로 달라서 예외


# In[23]:


int("안녕하세요") #정수로 바꿀수 없어서 실행오류


# In[25]:


cursor.close) #syntax오류


# In[26]:


[1,2,3,4,5][10] #실행오류


# except Exception as exception:
# 
# 예외가 발생하면 예외 객체를 만들어냄
# 저장하려면 변수이름을 정해야함
# 

# In[30]:


list_number = [52,273,32]

try:
    number_input=int(input("정수 입력 >"))
    print("{}번째 요소 : {}".format(number_input,list_number[number_input]))
    예외. 발생해주세요()
except ValueError as exception:
    print("정수를 입력해주세요")
    print(type(exception),exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다")
    print(type(exception),exception)
except Exception as exception:
    print("미리파악하지 못한 예외")
    print(type(exception),exception)


# 영화추천 
# 
# 신작영화 시청
# 
# 태그 달기
# 
# 

# In[71]:




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


# In[ ]:





# In[ ]:




