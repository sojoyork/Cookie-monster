import os

def read_news_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content
    else:
        print(f"File {filename} does not exist.")
        return None

def print_welcome_message():
    print("Welcome to Cookie News! <3")
    print("Here are the latest updates and features about Cookie Monster:")

if __name__ == "__main__":
    while True:
        print_welcome_message()
        news_content = read_news_from_file('cookie_news.txt')
        if news_content:
            print(news_content)
        else:
            print("No news available at the moment.")
        
        user_input = input("Would you like to see the news again? (yes to continue, no to exit): ").strip().lower()
        if user_input != 'no':
            print("Exiting Cookie News. Have a great day!")
            break
