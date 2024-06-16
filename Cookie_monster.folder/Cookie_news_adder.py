def add_news_to_file(news, filename='cookie_news.txt'):
    with open(filename, 'a') as file:
        file.write(news + "\n" + "="*50 + "\n")
    print("News added successfully.")

def print_welcome_message():
    print("Welcome to Cookie News Adder! <3")
    print("Only developers can use this tool to add news and updates about Cookie Monster.")

if __name__ == "__main__":
    print_welcome_message()
    news_entry = input("Enter the news or feature update: ")
    add_news_to_file(news_entry)
