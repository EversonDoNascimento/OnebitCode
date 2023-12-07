class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan,
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self) -> str:
        print(f"{'#'*10} Informations of movie {'#'*10}")
        print(f"The name of movie is: {self.name}\n" +
              f"The year launch is: {self.yearLaunch}\n"
              f"The plan is include? {self.includePlan}\n"
              f"The note this movie is: {self.note}\n"
              f"The duration of movie is: {self.durationMinutes}"
              )

movie_matrix = Movie("Matrix", 1999, True, 5.0, 180)
movie_matrix.__str__()

movie_mario = Movie("Mario bros", 2023, True, 4.0, 120)
movie_mario.__str__()