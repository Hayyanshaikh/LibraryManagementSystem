import os
import shutil
import time
import subprocess


def issued_book():
  print("\n===== Issue Book =====\n")

  books = os.listdir("books/")

  if len(books) != 0:
    print("Available books:")
    for book in books:
      print(book.replace(".html", ""))

    book_name = input("\nEnter the book name: ")

    if f"{book_name}.html" in books:

      if not os.path.exists("issued"):
        os.makedirs("issued")

      deadline = int(input("Enter the deadline (days): "))

      # Calculate return date
      convert_seconds = deadline * 24 * 60 * 60

      print(f"convert seconds: {convert_seconds}")

      shutil.move(f"books/{book_name}.html", f"issued/{book_name}.html")
      print("✅ Book issued successfully!")

      # Schedule file move after 3 seconds using Windows Task Scheduler
      script = f"powershell.exe -Command \"Start-Sleep -Seconds {convert_seconds}; Move-Item 'issued/{book_name}.html' 'books/{book_name}.html'\""
      subprocess.Popen(script, shell=True)
    else:
      print("❌ Book not found!")
  else:
    print("⚠️ No books found!")
