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
auto_features = ["morbius","sad","sus","trade", "mom"]
