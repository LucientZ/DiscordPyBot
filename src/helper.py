import logging.handlers
from datetime import datetime

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

class Logger():
    # Logger setup
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    log_file_formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', '%Y-%m-%d %H:%M:%S', style='{')
    log_file_handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=4
    )
    log_file_handler.setFormatter(log_file_formatter)

    logger.addHandler(log_file_handler)

    # Logging functions
    def log_info(msg: str):
        print(f"{cl.GREY}{datetime.now()} {cl.BLUE}[INFO] {cl.END} {msg}")
        Logger.logger.info(msg)

    def log_error(msg: str):
        print(f"{cl.GREY}{datetime.now()} {cl.RED}[ERROR]{cl.END} {msg}")
        Logger.logger.error(msg)
