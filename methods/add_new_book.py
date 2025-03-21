import time
import webbrowser
import os


def add_new_book():

  file_title = input("Enter the book name: ")
  content = input("Enter the book content: ")

  # Ensure the books folder exists
  if not os.path.exists("books"):
    os.makedirs("books")

  file_name = f"books/{file_title}.html"

  # Using context manager to handle file
  with open(file_name, "w") as file:
    html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{file_title}</title>
            <style>
                body {{
                    font-family: "Georgia", serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .book-container {{
                    width: 60%;
                    max-width: 800px;
                    text-align: center;
                    margin: 20px auto;
                    background-color: #fff;
                    border: 2px solid #ddd;
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                    padding: 30px;
                    border-radius: 10px;
                }}
                .title {{
                    font-size: 2.5rem;
                    text-align: center;
                    font-weight: bold;
                    color: #333;
                    margin-bottom: 20px;
                    border-bottom: 2px solid #ddd;
                    padding-bottom: 10px;
                }}
                .content {{
                    font-size: 1.2rem;
                    text-align: center;
                    line-height: 1.6;
                    color: #555;
                    text-align: justify;
                    margin: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="book-container">
                <h1 class="title">{file_title}</h1>
                <div class="content">
                    <p>{content}</p>
                </div>
            </div>
        </body>
        </html>
        """

    # Write the HTML content to file
    file.write(html_template)

  file_path = os.path.abspath(file_name)

  print(f"✅ Successfully added new book: '{file_title}'")
  print("🚀 Opening book...")

  # Open the file in the default browser
  webbrowser.open(f"file://{file_path}")

  time.sleep(3)
