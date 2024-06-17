import os
import time

HOTPOT_FILENAME = "cookie_HotPot.txt"

def log_cookie_fetch(url):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"{timestamp}: Fetched cookies from {url}\n"
    try:
        with open(HOTPOT_FILENAME, 'a') as file:
            file.write(log_entry)
        print("Log entry added successfully.")
    except Exception as e:
        print(f"Error logging cookie fetch: {e}")

def read_log():
    if os.path.isfile(HOTPOT_FILENAME):
        try:
            with open(HOTPOT_FILENAME, 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error reading log file: {e}")
            return None
    else:
        return "No log entries found."

if __name__ == "__main__":
    print("Welcome to Cookie HotPot! <3")
    while True:
        command = input("Enter 'view' to see log entries or 'exit' to quit: ").strip().lower()
        if command == 'exit':
            break
        elif command == 'view':
            log_content = read_log()
            if log_content:
                print("Log Entries:")
                print(log_content)
            else:
                print("No log entries found.")
        else:
            print("Invalid command. Please try again.")
