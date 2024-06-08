import warnings
from colorama import Fore, Style

warnings.filterwarnings("ignore")

module_description = "KeySmith is a password generation tool designed to create strong, personalized passwords by transforming user inputs like names and personal details into secure combinations."
__version__ = "1.0.1"




def info():
    print(

        '  ____  __.             _________       .__  __  .__ \n' +
        ' |    |/ _|____ ___.__./   _____/ _____ |__|/  |_|  |__   \n' +
        ' |      <_/ __ <   |  |\_____  \ /     \|  \   __\  |  \  \n' +
        ' |    |  \  ___/\___  |/        \  Y Y  \  ||  | |   Y  \ \n' +
        ' |____|__ \___  > ____/_______  /__|_|  /__||__| |___|  / \n' +
        '         \/   \/\/            \/      \/              \/  \n'

    )
    print(f"KeySmith {__version__}\n{module_description} \n\n\n")
    #print(f"{Fore.CYAN}{Fore.YELLOW}Warning : /Only designed as a project, abuse is not my problem/{Fore.YELLOW}{Fore.RESET}")