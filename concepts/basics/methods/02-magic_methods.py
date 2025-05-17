# magic methods

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    # returns the fstring and print it rather than printing the address
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # check if equal (==)
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # check if self < other
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    # check if self > other
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"
        
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book1copy = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book2)
print(book3)


print("Exact copy" if book1 == book1copy else "Not the exact copy")

print("Less than" if book3 < book1 else "More than")
print("More than" if book1 > book3 else "Less than")

print(book1 + book3)

print("Present" if "Lion" in book1 else "Not Present")

print(book3['title'])
print(book3['author'])
print(book3['num_pages'])
print(book3['audio'])