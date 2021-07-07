import logging

class Library:
    def __init__(self,Books):
        self.Books=Books
        self.lend_book_d={}
    # this method displays all the available books.  
    def display_books(self):
        logging.info("Available books in library: ")
        for b,c in self.Books.items():
            print(b,c)
            
    # this method is used for lending a book  from the library by user
    def lend_book(self,username,bookname):
        if bookname not in self.Books.keys():
            logging.error("Book is not present!! it might be due to invalid bookname or book is currently not available")
        elif not self.Books[bookname]:
            logging.error("Book is not present!! it might be due to currently not available")
        else:
            self.lend_book_d.update({bookname:username})
            print("Hi {}, Book is available in library, you can lend {} book now".format(username,bookname))
            print("Updated lend data: {}".format(self.lend_book_d))
            self.Books[bookname]=self.Books[bookname]-1
        
    
    # this method is used to add a book to library by librarian
    def add_book(self,bookname,copies):
        self.Books.update({bookname:copies})
        logging.info("Book is added to library.Updated book list: {}".format(self.Books))
    
    # this method is used to return a book by user.
    def return_book(self,username,bookname):
        if bookname not in self.lend_book_d.keys():
            logging.error("Please enter a valid bookname or check the spelling")
        else:
            self.lend_book_d.pop(bookname)
            self.Books[bookname]=self.Books[bookname]+1
            logging.info("Book {} is successfully returned by {}".format(bookname,username))
    
    # this method is used to remove a book from the library by librarian
    def remove_book(self,bookname):
        #print("Available booklist - {} : {}".format(bookname,self.Books))
        self.Books.pop(bookname)
        logging.info("Book: {} is removed by Librarian".format(bookname))
        logging.info("Updated booklist after the deletion of book {} : {}".format(bookname,self.Books))

Books={'OS by Galvin':2,'Data Strctures':3,'Unix':2,'Shell Scripting':1,'5 am club':5,'C':2,'Java':0,'Web technologies':4,'M1':1,'Drawing':1}
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
        # the below are options available for the user.
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
        # below are options available for the librarian.
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
        copies=input("Enter number of copies to be added: ")
        Lib.add_book(bookname,copies)
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

