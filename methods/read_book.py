import time
import webbrowser
import os
from methods.add_new_book import add_new_book


def read_book():
  # Ensure the books folder exists
  if not os.path.exists("books"):
    os.makedirs("books")
  books = os.listdir("books/")
  print("\n===== LIST OF BOOKS =====\n")
  books_count = len(books)

  if books_count != 0:
    # Display available books
    for book in books:
      print(book.replace(".html", ""))

    book = input("\nEnter the book name: ").strip()

    # Case-insensitive book search
    if f"{book}.html" in books:
      file_path = os.path.abspath(f"books/{book}.html")
      print("📖 Opening the book...")
      time.sleep(1)
      webbrowser.open(f"file://{file_path}")
    else:
      print("❌ Book not found! Please try again.")
      user_input = input(
          "Do you want to add a new book? (yes/no): ").strip().lower()

      if user_input == "yes":
        add_new_book()
      else:
        print("Returning to the main menu...")
  else:
    print("⚠️ No books found!")
    user_input = input(
        "Do you want to add a new book? (yes/no): ").strip().lower()
    if user_input == "yes":
      add_new_book()
    else:
      print("No book to read. Exiting...")
