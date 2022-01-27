class MyClass:      #p
    var = 100

    @classmethod
    def class_method(cls):  #snake_case
        return cls

print(MyClass.class_method())
print(MyClass)
