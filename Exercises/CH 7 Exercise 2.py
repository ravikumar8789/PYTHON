dic={}
name= input("name :")
age=input("name : ")
fav_movie= input("fav movies seperated by comma : ").split(",")
fav_songs= input("Enter fav songs sapereted by comma : ").split(",")
dic['name']= name
dic['age']= age
dic['fav_movie']= fav_movie
dic['fav_songs']= fav_songs

for i,j in dic.items():
    print(i,j)
    