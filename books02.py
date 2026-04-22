# LIBRART.PY

books=[]
issued_books=[]

#add books
def add_books():
    name=input("enter the books name:")
    books.append(name)
    print("books added")

# show books
def show_books():
    if len(books) == 0:
     print("no books available")
    else:
        print("books are available")
        for b in books:
            print(b)

 #issue books
def issue_books():
    name=input("enter the book name")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("books available")
    else:
            print("book not available")

# return books
def return_books():
    name=input("enter the books name:")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("book returned")
    else:
            print("book not issued")

            



# ! MAIN BODY
def library():
    while True:
        print("1.add books")
        print("2.show books")
        print("3.issue books")
        print("4.return books")
        print("5.exit")
        choice = int(input("enter your choice:"))
        if choice ==1:
            add_books()
        elif choice ==2:
            show_books()
        elif choice ==3:
            issue_books()
        elif choice ==4:
            return_books()
        elif choice ==5:
            print("Thank you")
        else:
            print("Invalid choice")
library()

