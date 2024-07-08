def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))

def calculate(n, **kwargs):
    # for (key, value) in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model") # 위와 다른 점-> .get()은 선언하지 않아도 오류 발생 X. 즉 필수사항에서 선택사항이 된다는 것

my_car = Car(make="Nissan", model="GT-8")
print(my_car.model)