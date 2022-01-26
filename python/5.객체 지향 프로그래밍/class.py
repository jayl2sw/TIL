class MyClass:
    var = 100

    @classmethod
    def class_method(cls):
        return cls

print(MyClass.class_method())
print(MyClass)