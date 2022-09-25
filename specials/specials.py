myList = [1,2,3]
# myString = 'my string'

# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))

class Movie():
    def __init__(self, title, director, time):
      self.title = title
      self.director = director
      self.time = time
      print ('movie objesi oluşturuldu.')

    def __str__(self):
        return f"{self.title}, by {self.director}"

    def __len__(self):
        return self.time

    def __del__(self):
        print('movie has been deleted.')

m = Movie('movie name', 'directors name', 120)

# print(str(myList))
print(str(m))


# print(len(myList))
# print(len(m))

