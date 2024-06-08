import random
from CraftingTable import *
import Main
from GetInfo import *
from datetime import datetime


class KeySmith:
    def __init__(self,dict=None):
        self.dict = dict

    def Collect(self):
        getInfo = GetInfo()
        getInfo.SetInfo()

        self.dict = getInfo.data


    def Generate(self):
        # we have our dict

        flag = 0

        with open("Results/MostPopulerPasswordsList.txt", "r") as file:
            line_count = sum(1 for line in file)

        quer = input(f"Would you want to add {line_count} lines of most used password to your result (Y/N)")
        if quer == 'Y' or quer == 'y' : flag = 1



        current_date_t = datetime.now().strftime("%d.%m.%Y")
        if (self.dict['name'] is not None):
            file_name =  f"{self.dict['name']}-{current_date_t}"
        else :
            file_name = f"{current_date_t}-{random.randint(1, 100)}"

        CT = CraftingTable()

        # coming ...
        CT.Craft(f"Results/{file_name}",)




if __name__ == "__main__":
    main = KeySmith()

    Main.info()

    # Collecting Data
    main.Collect()

    # Generating
    main.Generate()