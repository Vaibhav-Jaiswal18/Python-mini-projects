import re

class LibraryItem:
    def __init__(self,t,a): self.title,self.author=t,a
    def display(self):
        print("Title :",self.title); print("Author:",self.author)

class Book(LibraryItem):
    def __init__(self,i,t,a,p):
        super().__init__(t,a); self.__isbn,self.__price,self.__issued=i,p,False

    def get_isbn(self): return self.__isbn
    def get_price(self): return self.__price
    def is_issued(self): return self.__issued
    def set_price(self,p): self.__price=p

    def display(self):
        print("-"*45)
        print("ISBN      :",self.__isbn)
        print("Title     :",self.title)
        print("Author    :",self.author)
        print("Price     :",self.__price)
        print("Status    :","Issued" if self.__issued else "Available")
        print("-"*45)

    def issue_book(self):
        if self.__issued: print("Book is already issued.")
        else: self.__issued=True; print("Book issued successfully.")

    def return_book(self):
        if self.__issued: self.__issued=False; print("Book returned successfully.")
        else: print("Book was not issued.")

class Library:
    def __init__(self): self.books=[]

    def add_book(self):
        try:
            i=input("ISBN (13 digits): ")
            if not re.fullmatch(r"\d{13}",i): raise ValueError("ISBN must contain exactly 13 digits.")
            t=input("Book Title: "); a=input("Author Name: "); p=float(input("Price: "))
            self.books.append(Book(i,t,a,p)); print("Book Added Successfully.")
        except ValueError as e: print("Error:",e)
        except Exception: print("Invalid Input!")

    def display_books(self):
        if not self.books: print("Library is Empty."); return
        for b in self.books: b.display()

    def search_book(self):
        i=input("ISBN: ")
        for b in self.books:
            if b.get_isbn()==i: print("Book Found"); b.display(); return
        print("Book Not Found.")

    def issue_book(self): self.action("issue_book")
    def return_book(self): self.action("return_book")

    def action(self,method):
        i=input("ISBN: ")
        for b in self.books:
            if b.get_isbn()==i: getattr(b,method)(); return
        print("Book Not Found.")

    def delete_book(self):
        i=input("ISBN: ")
        for b in self.books:
            if b.get_isbn()==i:
                self.books.remove(b); print("Book Deleted Successfully."); return
        print("Book Not Found.")

library=Library()

while True:
    print("\n"+"="*45)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*45)
    print("1.Add  2.Display  3.Search  4.Issue")
    print("5.Return  6.Delete  7.Exit")

    try:
        c=int(input("Choice: "))
        if c==1: library.add_book()
        elif c==2: library.display_books()
        elif c==3: library.search_book()
        elif c==4: library.issue_book()
        elif c==5: library.return_book()
        elif c==6: library.delete_book()
        elif c==7: print("Thank You!"); break
        else: print("Invalid Choice.")
    except ValueError: print("Enter numeric choice only.")
    except Exception as e: print("Unexpected Error:",e)