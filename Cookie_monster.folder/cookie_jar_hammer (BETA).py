import os
import http.cookies
import pyfiglet

def read_cookies_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content
    else:
        print(f"File {filename} does not exist.")
        return None

def get_cookie_info(cookie_string, cookie_name):
    cookie = http.cookies.SimpleCookie()
    cookie.load(cookie_string)
    if cookie_name in cookie:
        c = cookie[cookie_name]
        details = (
            f"Name: {c.key}\n"
            f"Value: {c.value}\n"
            f"Domain: {c['domain']}\n"
            f"Path: {c['path']}\n"
            f"Secure: {c.get('secure', '')}\n"
            f"HttpOnly: {'HttpOnly' in c._rest.keys()}\n"
            f"HostOnly: {'HostOnly' in c._rest.keys()}\n"
            f"Expiry Time: {c['expires']}\n"
        )
        return details
    else:
        return f"Cookie with name '{cookie_name}' not found."

def print_welcome_message():
    result = pyfiglet.figlet_format("COOKIE_JAR_HA-MMER.py")
    print(result)
    print("Welcome to Cookie Jar Hammer! <3")
    print("This tool helps you decrypt and show the information inside a cookie.")

if __name__ == "__main__":
    while True:
        print_welcome_message()
        filename = input("Enter the filename of the fetched cookies (e.g., example.com.Fetched.string.txt): ")
        
        cookie_content = read_cookies_from_file(filename)
        if cookie_content:
            cookie_name = input("Enter the name of the cookie you want to inspect: ")
            cookie_info = get_cookie_info(cookie_content, cookie_name)
            print("Cookie information:")
            print(cookie_info)
        else:
            print("Failed to retrieve cookies from the file.")
        
        continue_running = input("Do you want to inspect another cookie? (yes to continue, no to exit): ").strip().lower()
        if continue_running != 'yes':
            print("Exiting Cookie Jar Hammer. Goodbye!")
            break
