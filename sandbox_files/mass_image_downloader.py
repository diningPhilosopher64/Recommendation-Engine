import imdb
from BeautifulSoup import BeautifulSoup
import urllib2 
import os
import requests
import bs4
import numpy as np
import pandas as pd
from threading import Thread

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

file_path = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/images/"

threadlist = []


counter = 0

missing_movies=[]

def th():
    global counter
    counter = counter + 1
    bb = str(movies.ix[movies['movie_id'] == counter ]['title']).split()
    q = bb.index('Name:')
    bb = ' '.join(bb[1:q])
    try:
        print("Downloading the image :" + bb)
        item = ia.search_movie(bb)[0]
        req = requests.get(ia.get_imdbURL(item))
        soup = bs4.BeautifulSoup(req.text,"lxml")        
        img = requests.get(soup.find(itemprop="image")['src'])
        imgfile = open(file_path+"/"+bb,'wb')
        for chunk in img.iter_content(100000):
            imgfile.write(chunk)
        imgfile.close()
        
    except IndexError:
        global missing_movies
        missing_movies.append(bb)
        print("counter value :"+str(counter))
        print("Error with " + bb)

def thread_creator():
    global threadlist
    global counter
    file = open("counter.txt","r")
    counter = int(file.read()) + 1
    for u in range(100):
        t = Thread(target = th ,args=())
        t.start()       
        #global threadlist
        threadlist.append(t)

def thread_joiner():
    global threadlist
    global counter
    for b in threadlist:
        b.join()
    with open("counter.txt", "w") as text_file:
        text_file.write("{} ".format(counter))





#Need to call these two functions:
#thread_creator()
#thread_joiner()
    
    
