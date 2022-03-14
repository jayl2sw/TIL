from unittest import result


class MyList:

    def __init__(self, *args):
        self.value = [*args] # 언패킹해서 리스트로 감싸서 집어넣자.

    def __len__(self):          # 이게 없으면 len함수 사용 할 수 없다.
        result = 0
        for i in self.value:
            result += 1
        return result
       
    def __str__(self):
        return str(a.value)

    def __repr__(self):
        return print(str(a.value))
a = MyList(1, 2, 3, 4)
print(a.value)
print(a)
a
print(len(a))
print(dir(MyList))

