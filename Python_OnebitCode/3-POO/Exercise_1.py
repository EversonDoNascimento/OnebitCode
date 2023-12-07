'''
    Rating and avarege score for the movies

    Development new features for complement our management of class movies.
    Folow the scope of features:

    1 - One of features request is that the user can relize a rating of a movie
        passing a score with parameter and this score be save in specify attribute
        of class.

    2 - Like this that a rating is realized, must be increment of total of reviewers
        of that movie. Obs.: Make a new attribute for the avarage of rating.
    
    3 - For each movie have a avarage rating score which consists in division of total
        of rating by the total evaluation by total reviewers.
    
'''

class Movie:
    
    def __init__(self, name, yearLaunch, includePlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan,
        self.durationMinutes = durationMinutes
        self.notes = []
        self.count_users = 0
        self.avarage_notes = 0
    
    def __str__(self) -> str:
        print(f"{'#'*10} Informations of movie {'#'*10}")
        print(f"The name of movie is: {self.name}\n" 
              f"The year launch is: {self.yearLaunch}\n"
              f"The plan is include? {self.includePlan}\n"
              f"The note this movie is: {self.notes}\n"
              f"The duration of movie is: {self.durationMinutes}\n"
              f"The rating of movie is: {self.avarage_notes}\n"
              f"The quantity of users that reviewers: {self.count_users}"
              )
    
    def raring_users(self,note):
        self.notes.append(note)
        self.count_users += 1
        sum_notes = 0
        for note in self.notes:
            sum_notes += note
        self.avarage_notes = sum_notes / self.count_users

movie_mario = Movie("Super Mario Bros", 2023, True, 130)
movie_mario.__str__()
movie_mario.raring_users(10)
movie_mario.__str__()
movie_mario.raring_users(6)
movie_mario.raring_users(7)
movie_mario.raring_users(3)
movie_mario.__str__()


movie_matrix = Movie("The matrix", 1999, True, 180)
movie_matrix.__str__()
movie_matrix.raring_users(10)
movie_matrix.__str__()
movie_matrix.raring_users(8)
movie_matrix.raring_users(8)
movie_matrix.raring_users(9)
movie_matrix.__str__()