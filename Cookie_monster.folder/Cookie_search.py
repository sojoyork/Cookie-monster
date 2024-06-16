import os
import pyfiglet

def read_cookies_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content
    else:
        print(f"File {filename} does not exist.")
        return None

def print_welcome_message():
    result = pyfiglet.figlet_format("COOKIE_SEARCH.py")
    print(result)
    print("Welcome to Cookie Search! <3")
    print("Enter the filename of the fetched cookies to view them.")

if __name__ == "__main__":
    print_welcome_message()
    
    while True:
        filename = input("Enter the filename (e.g., example.com.Fetched.string.txt): ")
        
        cookie_content = read_cookies_from_file(filename)
        if cookie_content:
            print("Cookies retrieved from file:")
            print(cookie_content)
        else:
            print("Failed to retrieve cookies from the file.")
        
        exit_input = input("Would you like to exit the code? (type 'yes' to exit): ").strip().lower()
        if exit_input == 'yes':
            print("Goodbye!")
            break
