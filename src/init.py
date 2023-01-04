import os

def append_env_variable(var_name: str, var_val: str, is_string: bool = False):
    with open("./config/.env", 'a') as env_file:
        if is_string:
            var_val = f'"{var_val}"'
        env_file.write(f"{var_name}={var_val}\n")

def ask_yes_no(query: str):
    response = ""
    while not (response.lower() == 'y' or response.lower() == 'n'):
        response = input(query)
    if response == 'y':
        return "True"
    else:
        return "False"

def query_env_vars():
    if(not os.path.exists('./config/.env')):
        TOKEN = input("Please enter the bot token: ")
        STATUS = input("Please enter the bot's status: ")
        SYNC_ON_START = ask_yes_no("Should the bot sync on start? (Y/n): ")

        append_env_variable("TOKEN", TOKEN, True)
        append_env_variable("STATUS", STATUS, True)
        append_env_variable("SYNC_ON_START", SYNC_ON_START)
    else:
        print("./src/.env file found")

if __name__ == "__main__":
    query_env_vars()
