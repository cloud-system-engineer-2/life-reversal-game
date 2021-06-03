movie1 ={
    "title" : "Minarie",
    "tags" : ["korea","drama","usa","1980","country"] 

    }
movie2 ={
    "title" : "Sweethome",
    "tags" : ["korea","drama","horror","city","monster"] 

    }    

movie_list=[movie1, movie2]


#########################func#####################
def user_info_input():
    
    tag=input("what's your tag?>")
    name=input("what's your name?>")
    print("welcome {} This is Movie recommendation Program :)".format(name))

    return tag, name

def movie_search(tag):
    movie_contain=[]
    for movie in movie_list:
        if(tag in movie["tags"]):
            print("****************************")
            print(movie["title"])
            movie_contain.append(movie["title"])
            

        else:
            print("****************************")
                   
    return movie_contain 

def file_save(text):
    for movietitle in text:
        save = input("would you like to save that in a file?>(y/n)")
        if save == 'y':
            with open("movie_{}.txt".format(movietitle),"w") as file:
                file.write(movietitle)
        else:
            print("ok. This program didn't save that...")


####################### main ################################


def main():
    try:
        tag, name =user_info_input()
        moviecontain=movie_search(tag)

    finally:
        try:
            file_save(moviecontain)

        except:
            print("there are no movies relevent with your tags")
            print("program exit...")


main()