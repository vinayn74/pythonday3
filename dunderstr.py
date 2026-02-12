class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"{self.title} by {self.author} cost ₹{self.price}"
    def __repr__(self):
        return f"Book ({self.title} author = {self.author}, price = {self.price})"
book1 = Book("python oops","bhaskar", 299)
book2 = Book("basic java","bhaskar", 399)
print("__str method:")
print(book1)
print(book2)
print("__repr__ method")
print([book1 , book2])

