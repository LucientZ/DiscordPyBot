# Used for console formatting
class cl:
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m" # Resets output to default

class fumo_images:
    cirno = {
        0: "https://cdn.discordapp.com/attachments/390692666897203211/970373406979674152/Cirnofumo.webp",
        1: "https://cdn.discordapp.com/attachments/390692666897203211/970373407160016926/phpL2mdaC.webp",
        2: "https://cdn.discordapp.com/attachments/390692666897203211/970373407520743434/9a664b1fbd274c0b83a308315e975ec6.jpg",
        3: "https://cdn.discordapp.com/attachments/390692666897203211/970373408032423977/cirno-fumo.gif",
        4: "https://cdn.discordapp.com/attachments/390692666897203211/970373408367972462/41af2d3c2bf95a66718d354d438d432d.gif"
    }
    reimu = {
        0: "https://cdn.discordapp.com/attachments/390692666897203211/970374374429450302/s-l400.jpg",
        1: "https://cdn.discordapp.com/attachments/390692666897203211/970374374660132934/touhou-reimu.gif",
        2: "https://cdn.discordapp.com/attachments/390692666897203211/970374375171821669/images.jpg"
    }
    flandre = {
        0: "https://cdn.discordapp.com/attachments/390692666897203211/970374980611227758/2a9a8ebba16c4f47b281a6c27a1f5d8c.jpg",
        1: "https://cdn.discordapp.com/attachments/390692666897203211/970374980955172864/s-l640.jpg",
        2: "https://cdn.discordapp.com/attachments/390692666897203211/970374981202616320/fumo-fumo-touhou.gif",
        3: "https://cdn.discordapp.com/attachments/390692666897203211/970374981617864714/flandre-scarlet-fumo-touhou.gif"
    }
    hayasaka = {
        0: "https://cdn.discordapp.com/attachments/390692666897203211/990389626676060210/Hayasaka_Fumo.jpg",
        1: "https://cdn.discordapp.com/attachments/390692666897203211/990390507542839296/download.jpg",
        2: "https://cdn.discordapp.com/attachments/390692666897203211/990390507807068210/51YMmkWR7yL._AC_SL1000_.jpg"
    }
    aqua = {
        0: "https://cdn.discordapp.com/attachments/390692666897203211/990389626877382696/de7jvlp-7b5e7187-c26a-48e4-897f-c2755b2d85b4.jpg"
    }

def binary_search(array, x):
    """
    Returns index of a value in a sorted array

    Parameters:
    array (int/float/str): sorted array to be searched
    x (int/float/str): value to find (must be of same type as array)

    Returns:
    int: index of value or -1 which means not found
    """
    left = 0
    right = len(array) - 1
    X = float(x)

    while left <= right:
        mid = (left + right) // 2

        # If x is less, search left-half
        if X < float(array[mid]):
            right = mid - 1
        # If x is greater, search right-half
        elif X > float(array[mid]):
            left = mid + 1
        # If neither, mid is where x is
        else:
            return mid

    # -1 means not in array
    return -1


# Lists of sections of features and commands
# These lists are used in datahandling.py mainly for enabling/disabling commands
features = ["morbius","sad","sus","trade", "mom"]
fun_commands = ["boowomp","copypasta","fumo", "gacha"]
utility_commands = ["echo","ping"]
all_features = features + fun_commands + utility_commands

print(f"{cl.BOLD}{cl.GREEN}helper.py{cl.END}{cl.GREEN} initialized{cl.END}")