
import datetime
import unittest
#------------------------------------------
# The code is organized into a class named LibrarySystem. 
# It includes methods for adding books, removing books, marking books as borrowed or returned, 
# checking book availability, and printing available titles.

# To ensure the code's correctness, we've implemented test cases using the unittest module.
# Each test case focuses on a specific method or functionality of the LibrarySystem class.
#------------------------------------------

class LibrarySystem:
    # attribut
    def __init__(self, name):   
        self.name = name
        self.books = []
# metoder
    def add_book(self, title, author):
        book = {"title": title, "author": author, "available": True}
        self.books.append(book)
        print(f"Book {title} by {author} has been added to the library.")
    
    def remove_book(self, title, author):
        find_book = False
        for book in self.books:
            if book.get("title") == title and book.get("author")== author:
                self.books.remove(book)
                print(f"Book {title} by {author} has been removed from the library.")
                find_book = True
                break
        if  not find_book :
            print(f"Book {title} by {author} is not available to remove.")  

    # def mark_as_borrowed(self, title):
    #  for book in self.books :
    #         if book.get("title") == title and book.get("available") :           
    #             print(f"Book '{title}' has been marked as borrowed.in {book["borrow_date"]}") 
    #             book["available"] = False  
    #             book["borrow_date"] = datetime.datetime.now() 
    #         elif book.get("title") == title and not book.get("available"):
    #             print(f"Book '{title}' is already on loan.")
    #         else:
    #             print(f"There is no '{title}' in the library.")
                
    # def mark_as_returned (self,title):
    #    for book in self.books:
    #         if book.get("title") == title and not book.get("available"):
    #             print(f"Book '{title}' has been marked as returned.")
    #             book['available'] = True
    #         elif book.get("title") == title == title and book.get("available"):
    #             print(f"Book '{title}' is already available.")
    #         else:
    #             print(f"Book '{title}' is not found in this library")  
            

    def mark_as_borrowed(self, title):
        found = False
        for book in self.books:
            if book.get("title") == title and book.get("available"):
            
                print(f"Book '{title}' has been marked as borrowed on {book['borrow_date']}.")
                book["available"] = False
                book["borrow_date"] = datetime.datetime.now()
                found = True
                break
            elif book.get("title") == title and not book.get("available"):
                print(f"Book '{title}' is already on loan.")
                found = True
                break

        if not found:
            print(f"There is no '{title}' in the library.")       

    def mark_as_returned(self, title):
        found = False
        for book in self.books:
            if book.get("title") == title and not book.get("available"):
                borrow_date = book.get("borrow_date")
                if borrow_date is not None:
                    days_borrowed = (datetime.datetime.now() - borrow_date).days
                    print(f"Book '{title}' has been marked as returned.")
                    if days_borrowed > 14:
                        overdue_days = days_borrowed - 14
                        print(f"The book is {overdue_days} days overdue.")
                book['available'] = True
                found = True
                break
            elif book.get("title") == title and book.get("available"):
                print(f"Book '{title}' is already available.")
                found = True
                break

        if not found:
            print(f"Book '{title}' is not found in this library.")



    def is_available(self, title):
        for book in self.books:
            if book.get("title") == title and book.get("available") == True:
                print(f"Book '{title}' is avaivble in the library.")
                return True
        print(f"Book '{title}' not found in the library.")
        return False 

    def print_available_titles(self):
        self.available_books =[]
        for book in self.books:
          if book.get("available")==True:
            self.available_books.append(book.get("title"))
        print(f"Available books: {self.available_books}")
        return self.available_books


# Example:
my_library = LibrarySystem("My Local Library")

my_library.add_book("Elon Musk", "Ashlee Vance")
my_library.add_book("Steve Jobs", "Walter Isaecson")
my_library.print_available_titles()
print("----------------------")
my_library.remove_book("Steve Jobs" , "Walter Isaecson")
my_library.print_available_titles()
my_library.mark_as_borrowed("Steve Jobs")
my_library.mark_as_borrowed("Elon Musk")
my_library.is_available("1984")
print("----------------------")
# my_library.mark_as_returned("Steve Jobs")
my_library.mark_as_returned("Elon Musk")
return_date = datetime.datetime.now() + datetime.timedelta(days=20)
print(return_date)
my_library.print_available_titles()
my_library.is_available("Steve Jobs")
print("----------------------")

# TestClass

# class TestLibrarySystem(unittest.TestCase):
  
#     def setUp(self):  
#       self.my_library = LibrarySystem("my local Library")

#     def test_add_book(self):
        
#         self.my_library.add_book("Elon Musk", "Ashlee Vance")
#         self.assertEqual(len(self.my_library.books), 1)
  
#     def test_remove_book(self):
#         self.my_library.add_book("1984", "George Orwell")
#         self.my_library.add_book("Elon Musk", "Ashlee Vance")
#         self.my_library.add_book("Steve Jobs" , "Walter Isaecson")

#         self.my_library.remove_book("Steve Jobs" , "Walter Isaecson")
#         # Use assertNotIn to check if the book is not in the library after removal
#         self.assertNotIn("Steve Jobs", my_library.print_available_titles())

#     def test_mark_as_borrowed(self):       
#         self.my_library.mark_as_borrowed("Elon Musk")
#         # After marking as borrowed, the book should not be available
#         self.assertFalse(self.my_library.is_available("Elon Musk"))

#     def test_mark_as_returned(self):
#         self.my_library.add_book("1984", "George Orwell")
       
#         self.my_library.mark_as_returned("1984")
#         # After marking as returned, the book should be available again
#         self.assertTrue(self.my_library.is_available("1984"))

#     def test_is_available(self):
#         self.my_library.add_book("Elon Musk", "Ashlee Vance")
#         self.assertTrue(self.my_library.is_available("Elon Musk"))
#         self.my_library.mark_as_borrowed("Elon Musk")
#         self.assertFalse(self.my_library.is_available("Elon Musk"))

#     def test_print_available_titles(self):
#         self.my_library.add_book("Elon Musk", "Ashlee Vance")
#         self.my_library.add_book("Steve Jobs", "Walter Isaecson")
#         # After adding two books, both should be available
#         self.assertEqual(self.my_library.print_available_titles(), ["Elon Musk", "Steve Jobs"])


# if __name__ == "__main__":
#     unittest.main()




