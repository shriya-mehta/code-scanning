import subprocess, sqlite3

def run_command(cmd):
    subprocess.run(cmd, shell=True)

def find_user(username):
    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query) 

if __name__ == "__main__":
    user_input = input("Enter any value: ")
    run_command("echo " + user_input)
    find_user(user_input)
