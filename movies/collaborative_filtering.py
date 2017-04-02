#have to give ratings path and not create file everytime ,else new user and their ratings will be lost.

class collaborative_filtering():
    def __init__(self,ratings_file):#No need to pass as ,will be provided in views.py
        self.users = users
        self.movies = movies
        self.K = 100
        self.PERCENT_TRAIN = 85
        #Need to provide a default file location for ratings.csv instead of loading everytime.run below 2lines only once 
        #or just provide this file instead.
        #self.users.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index= False)
        self.ratings_file = "/home/sourabhkondapaka/Desktop/ratingsss.csv"  #Give your path to ratings.csv created from above 2 lines.
        self.data = None
        self.svd = None
        self.movie_list = None
        self.train = None
        self.test = None

        
        
    def compute_svd(self):      
        self.data = Data()
        self.data.load(self.ratings_file, sep=',', format={'col':0, 'row':1 ,'value':2, 'ids':float})
        self.train , self.test = self.data.split_train_test(percent=self.PERCENT_TRAIN)    
        self.svd = SVDNeighbourhood()
        self.svd.set_data(self.train)    
        self.svd.compute(k=self.K, min_values=1, pre_normalize=None, mean_center=True, post_normalize=True)

    def similarity_measure(self,movie1 , movie2): #gives a similarity measure value between -1 to 1
        return round(self.svd.similarity(movie1,movie2),4)
    
    def recommend_movies(self,user_id):
        l =  self.svd.recommend(user_id, n=10, only_unknowns=True, is_row=False)
        self.movie_list = []
        for p in l:
            movies.ix[movies['movie_id']== p[0]]['title']
            bb = str(movies.ix[movies['movie_id'] == p[0] ]['title']).split()    
            q = bb.index('Name:')
            bb = ' '.join(bb[1:q])
            self.movie_list.append(bb)            
        return self.movie_list
    
    
    def get_similar_movies(self,movie1):#Returns a PYTHON list for similar movies.
        l = self.svd.similar(movie1)
        movie_list = []
        l = l[2:]
        for p in l:
            movies.ix[movies['movie_id']== p[0]]['title']
            bb = str(movies.ix[movies['movie_id'] == p[0] ]['title']).split()    
            q = bb.index('Name:')
            bb = ' '.join(bb[1:q])
            movie_list.append(bb)            
        return movie_list
    