a = dict()
a = set()

class b: #클래스(붕어빵틀)
    pass

bb1 = b() #객체(붕어빵)
bb2 = b() #여러개의 개체를 만들 수 있다.
bb3 = b()

class Movie:
    title = "범죄도시4"
    score = 1

movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)
movie1.title = "파묘"

print(movie1.title)
print(movie2.title)

print(movie1.score)
print(movie2.score)
print()

class Movie:
    name = ''
    def print_msg(msg):
        print(msg)
    def modify(self,movie):
        self.name = movie
    def print_name(self):
        print(self.name)

movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print하기")
# Movie.modify(movie1, "print하기2")
movie1.modify("프린트하기3")
movie1.print_name()
movie2.modify("프린트하기4")
print("movie2.name",movie2.name)

#생성자
class Movie:
    def __init__(self):
        print("Hello I'm Movie Class.")
movie = Movie()

#매개변수가 있는 생성자
class Movie:
    count = 0
    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1 #클래스 변수는 모든 인스턴스의 값에 영향을 준다.
movie1 = Movie("bossbaby",100)
movie2 = Movie("bossbaby2",200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)

movie1.count += 1 #인스턴스 변수는 인스턴스에만 영향을 준다. 인스턴스를 생성해야 사용할 수 있다.
print(movie1.count)
print(movie2.count)
print(Movie.count)

#접근제어
class Movie:
    count = 0
    
    def __init__(self, title, audience):
        self.__title = title
        self.__audience = audience
        Movie.count += 1

    def get_title(self):
        return self.__title
    
    def set_title(self,title): 
        self.__title = title
    
    def get_audience(self):
        return self._audience

movie1=Movie("bossbaby",100)

#print(movie1.__title) #오류발생
print(movie1.get_title())
movie1.__title = "오겜"
print(movie1.get_title())
print(movie1.__title)
print(movie1.get_title())
print()
movie1.set_title("오징어")
print(movie1.get_title())
print()

class MyAdd:
    __a = 1
    __b = 2

    #######메소드 구현
    def sum(self):
        return self.__a + self.__b
    
    def set_sum(self,a):
        self.__a = a


a = MyAdd()
print(a.sum()) #3
# __a 값 3으로 변경
a.set_sum(3)
print(a.sum()) #5
