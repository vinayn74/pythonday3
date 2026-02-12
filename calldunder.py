class calculater:
    def __call__(self, a, b):
        return a+b
obj = calculater()
print(obj(20, 30))