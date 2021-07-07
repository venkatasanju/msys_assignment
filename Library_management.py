class Library:
    def __init__(self,Books):
        self.Books=Books
        self.lend_book_d={}
    
    def display_books(self):
        print("Available books in library: ")
        for b in self.Books:
            print(b)
    def lend_book(self,username,bookname):
        if bookname not in Books:
            print("Book is not present!! Please enter a valid bookname or check the spelling")
        else:
            if bookname not in self.lend_book_d.keys():
                self.lend_book_d.update({bookname:username})
                print("Hi {}, Book is available in library, you can lend {} book now".format(username,bookname))
                print("Updated lend data: {}".format(self.lend_book_d))
                self.Books.remove(bookname)
            else:
                print("Book is not available, its being used by the user {}:".format(self.lend_book_d[bookname]))
            
    def add_book(self,bookname):
        self.Books.append(bookname)
        print("Book is added to library.Updated book list: {}".format(self.Books))
    def return_book(self,username,bookname):
        if bookname not in self.lend_book_d.keys():
            print("Book is not present!! Please enter a valid bookname or check the spelling")
        else:
            self.lend_book_d.pop(bookname)
            self.Books.append(bookname)
            print("Book {} is successfully returned by {}".format(bookname,username))
    def remove_book(self,bookname):
        #print("Available booklist - {} : {}".format(bookname,self.Books))
        self.Books.remove(bookname)
        print("Book: {} is removed by Librarian".format(bookname))
        print("Updated booklist after the deletion of book {} : {}".format(bookname,self.Books))
        
Books=['OS by Galvin','Data Strctures','Unix','Shell Scripting','5 am club','C','Java','Web technologies','M1','Drawing']
Lib=Library(Books)

 
count=0
profile=''

while(True):
    if count==0:
        print("Welcome to the Library!!")
        #print("Please enter the below details: 1) Librarian 2) User")
        user = input("Please mention if you are User or Librarian: ")
        count=count+1
    profile=user
    if profile == "user":
        print("Please enter your choice:")
        print("1. Display available books ")
        print("2. Lend a book")
        print("3. Return a book")
        choice=input()
        print("User selected choice: {}".format(choice))
        if choice not in ["1","2","3"]:
            print("User selected choice is not present, please enter valid option")
            continue
    elif profile=="librarian":
        print("Please enter your choice:")
        print("1. Display available books")
        print("4. Add a book")
        print("5. Remove a book")
        choice=input()
        if choice not in ["1","4","5"]:
            print("Selected choice is not present, please enter valid option")
            continue
        
    choice=int(choice)
    if choice==1:
        Lib.display_books()
    elif choice==2:
        print("Please enter the below details:")
        username=input("Enter your name: ")
        bookname=input("Enter name of the book: ")
        Lib.lend_book(username,bookname)
    elif choice==3:
        bookname=input("Enter the name of the book you would like to return: ")
        username=input("Enter your name:")
        Lib.return_book(username,bookname)
    elif choice==4:
        bookname=input("Enter the name of the book to be added: ")
        Lib.add_book(bookname)
    elif choice ==5:
        bookname=input("Enter the name of the book to be deleted from library: ")
        Lib.remove_book(bookname)
    else:
        print("Not a valid choice")
    print("Please enter the Q/q to quit and c/C for continue:")
    continue_choice=input()
    if continue_choice=='q' or continue_choice=='Q':
        print("Exiting")
        exit()
    elif continue_choice=='c' or continue_choice=='C':
        continue
