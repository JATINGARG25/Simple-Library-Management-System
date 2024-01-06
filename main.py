class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print("\nBooks present in this library are:\n")
        for book in self.books:
            print("* " + book)

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"\nYou issued book {bookname}. Please keep it safe and return within 30 days.")
            self.books.remove(bookname)
            return True
        else:
            print("\nThis book is either not available or has been already issued to someone else. Please wait until the book is available.")
            return False
        
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("\nThanks for returning the book.")
    
    def addbook(self,bookname):
        self.books.append(bookname)
        print("\nThanks for adding the book.")

class Student:
    def requestbook(self):
        self.book = input("\nEnter the name of the book you want to borrow: ")
        return self.book
    def returnbook(self):
        self.book = input("\nEnter the name of the book you want to return: ")
        return self.book
    def addbook(self):
        self.book = input("\nEnter the name of the book you want to add: ")
        return self.book

if __name__ == "__main__":
    student = Student()
    central_library = Library(["Algorithms","Django","Full stack","Python notes","C notes"])
    print("\n           ****Welcome to central library****")
    while(True):

        wlcmsg = '''
    Please choose an option:
    1. Listing all the books
    2. Request a book
    3. Return a book
    4. Add a book
    5. Exit the library
    '''
        print(wlcmsg)

        a = int(input("Enter a choice: "))
        if a==1:
            central_library.displayavailablebooks()
        elif a==2:
            central_library.borrowbook(student.requestbook())
        elif a==3:
            central_library.returnbook(student.returnbook())
        elif a==4:
            central_library.addbook(student.addbook())
        elif a==5:
            print("\nThanks for choosing central library.")
            exit()
        else:
            print("\nInvalid choice")
