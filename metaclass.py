class Time(object):
    pass

print(type(Time))

print(Time.__bases__)


class MyMeta(type):

    def __str__(cls):
        return "hello"
    

class A(metaclass = MyMeta):
    pass

print(str(A))
