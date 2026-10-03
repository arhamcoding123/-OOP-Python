class Book:
    title=""
    author=""
    price=""

    def set_book_info(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        print(f"Title:{self.title},Author: {self.author},Price={self.price}")
        


Book1=Book()
Book1.set_book_info(1984,"George Orwell","150")
Book1.display_info()


Book2=Book()
Book2.set_book_info("Harry Potter","J.K Rowling",450)
Book2.display_info()
