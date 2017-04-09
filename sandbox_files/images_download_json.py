import imdb
from BeautifulSoup import BeautifulSoup
import urllib2 
import os
import requests
import bs4
import numpy as np
import pandas as pd
from threading import Thread
import json,requests,unicodedata,urllib2
import time


# set some print options
np.set_printoptions(precision=4)
np.set_printoptions(threshold=5)
np.set_printoptions(suppress=True)
pd.set_option('precision', 3, 'notebook_repr_html', True, )

# init random gen
np.random.seed(2)



movies_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/movies.csv"
movies = pd.read_table(movies_file, sep=',')
movies.columns = ['movie_id','title','genres']
names = movies['title']

ia = imdb.IMDb()



threadlist = []

file_path2 = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/images2"
def th():
    global counter    
    bb = str(movies.ix[movies['movie_id'] == counter ]['title']).split()    
    q = bb.index('Name:')
    bb = ' '.join(bb[1:q]) 
    print("Counter value for movie " + bb + str(counter))
    try:
        print("Downloading the image :" + bb)
        item = ia.search_movie(bb)[0]
        print("Name in item is " + str(item))
        name = str(item)        
        ll = name.split()
        #ll = '+'.join(ll)
        movie_url = url + '+'.join(ll)
        print movie_url
        content = urllib2.urlopen(movie_url).read()
        jsontopython = json.loads(content)
        img = requests.get(jsontopython['Poster'])
        imgfile = open(file_path2+"/"+bb,'wb')
        for chunk in img.iter_content(100000):
            imgfile.write(chunk)
        imgfile.close()
        
    except IndexError:
        global missing_movies
        missing_movies.append(bb)
        print("counter value :"+str(counter))
        print("Error with " + bb)




missing_movies=[]

url = "http://www.omdbapi.com/?t="

file = open("counter.txt","r")
counter = int(file.read())


def thread_creator():    
    global threadlist
    global counter
    print("Counter value before starting threads is : " + str(counter))
    for u in range(10):
        t = Thread(target = th ,args=())
        
        t.start() 
        time.sleep(1)
        counter = counter + 1
        threadlist.append(t)

        

def thread_joiner():
    global threadlist
    global counter
    print("THreadList is \n\n")
    print threadlist
    for b in threadlist:
        b.join()
    with open("counter.txt", "w") as text_file:
        text_file.write("{} ".format(counter))

       



