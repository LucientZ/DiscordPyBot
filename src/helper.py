import os
from dotenv import load_dotenv
load_dotenv("./config/.env")

# Environment Variables
class env_vars:
    TOKEN = os.environ.get("TOKEN")
    STATUS = os.environ.get("STATUS")
    SYNC_ON_START= os.environ.get("SYNC_ON_START").lower() in ('true', '1', 't')

# Used for console formatting
class cl:
    GREY = "\033[90m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    MAGENTA = "\033[35"
    BOLD = "\033[1m"
    END = "\033[0m" # Resets output to default

# Lists of sections of features and commands
# These lists are used in datahandling.py mainly for enabling/disabling commands
features = ["morbius","sad","sus","trade", "mom"]
fun_commands = ["boowomp","copypasta","fumo"]
utility_commands = ["echo","ping"]
all_features = features + fun_commands + utility_commands
