from methods.add_new_book import add_new_book
from methods.read_book import read_book
from methods.issued_book import issued_book


def menu():
  print("\n===== Library Management System =====\n")
  print("1. Add New Book")
  print("2. Issue Book")
  print("3. Return Book")
  print("4. Display Books")
  print("5. Exit")


menu()

choice = int(input("Enter your choice: "))
if choice == 1:
  add_new_book()
elif choice == 2:
  issued_book()
elif choice == 3:
  print("return book")
elif choice == 4:
  read_book()
elif choice == 5:
  exit()
else:
  print("Invalid choice! Please try again.")
