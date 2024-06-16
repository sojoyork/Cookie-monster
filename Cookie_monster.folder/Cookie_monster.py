import requests
import os
import pyfiglet
from http.cookies import SimpleCookie

def fetch_cookies(url):
    try:
        session = requests.Session()
        response = session.get(url, timeout=10)
        # Attempt to fetch cookies from common paths
        common_paths = ['/', '/login', '/dashboard']
        for path in common_paths:
            session.get(f"{url.rstrip('/')}{path}", timeout=10)
        cookies = session.cookies
        return cookies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cookies: {e}")
        return None

def get_cookie_details(cookie):
    details = (
        f"Name: {cookie.name}\n"
        f"Value: {cookie.value}\n"
        f"Domain: {cookie.domain}\n"
        f"Path: {cookie.path}\n"
        f"Secure: {cookie.secure}\n"
        f"HttpOnly: {'HttpOnly' in cookie._rest.keys()}\n"
        f"HostOnly: {not cookie.domain_initial_dot}\n"
        f"Expiry Time: {cookie.expires}\n"
    )
    return details

def save_cookies_to_file(url, cookies):
    filename = f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}.Fetched.string.txt"
    with open(filename, 'w') as file:
        for cookie in cookies:
            file.write(get_cookie_details(cookie))
            file.write("\n" + "="*50 + "\n")
    print(f"Cookies saved to {filename}")

def print_welcome_message():
    result = pyfiglet.figlet_format("COOKIE_MONSTER.PY")
    print(result)
    print("Welcome to Cookie Monster! <3")
    print("Let's fetch cookies! Enter the website URL and the tool will fetch cookies for you.")
    print("Check Cookie_monster_command_easter_eggs.txt to check out cookie monster commands")
    print("")
    print("")

def play_cookie_clicker():
    print("\n🎉 You activated the Cookie Clicker Easter egg! 🎉")
    print("Click the cookie as fast as you can to gain cookies!")
    cookies = 0
    click_rate = 1
    try:
        while True:
            input("Press Enter to click the cookie...")
            cookies += click_rate
            print(f"Cookie count: {cookies} 🍪")
            if cookies >= 100:
                print("You won! You have 100 cookies! 🏆")
                break
    except KeyboardInterrupt:
        print("\nGame interrupted. You ended with {} cookies. 🍪".format(cookies))

if __name__ == "__main__":
    print_welcome_message()
    
    while True:
        target_url = input("Enter the website URL: ")

        user_input = input("Would you like to fetch cookies (Type 'fetch' to confirm): ").strip().lower()
        
        if user_input == 'fetch':
            website_cookies = fetch_cookies(target_url)
            if website_cookies:
                if len(website_cookies) > 0:
                    save_cookies_to_file(target_url, website_cookies)
                else:
                    print("No cookies found for this website.")
            else:
                print("Failed to fetch cookies :(")
        elif user_input == 'play' or 'i want to play cookie clicker! :)' in target_url.lower():
            play_cookie_clicker()
        else:
            print("Invalid input. Please enter 'fetch' to retrieve cookies.")

        exit_input = input("Would you like to exit the code? (type 'yes' to exit): ").strip().lower()
        if exit_input == 'yes':
            print("Goodbye!")
            break
