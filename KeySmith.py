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

        current_date_t = datetime.now().strftime("%d.%m.%Y")
        if (self.dict['name'] is not None and self.dict['name'] != ""):
            file_name =  f"{self.dict['name']}-{current_date_t}.txt"
        else :
            file_name = f"{current_date_t}-{random.randint(1, 100)}.txt"



        # Steps
        # Ask about would like to continue
        # Continue
        input_count=0
        if(self.dict['name'] != None and self.dict['name'] != ""):
            input_count += 1
        if (self.dict['petname'] != None and self.dict['petname'] != ""):
            input_count += 1
        if (self.dict['city'] != None and self.dict['city'] != ""):
            input_count += 1
        if (self.dict['country'] != None and self.dict['country'] != ""):
            input_count += 1
        if (self.dict['team'] != None and self.dict['team'] != ""):
            input_count += 1

        # birthday exist (?)
        b_exist = 0
        if(self.dict['birthday'] != None and self.dict['birthday'] != ""):
            b_exist = 1
            if(len(self.dict['birthday'].split('.')) != 3):
                b_exist = 0

        if(b_exist == 1):
            mult = 3
        else:
            mult = 0

        total_comb = (input_count*2*(6+mult))+(input_count*2*(6+mult))+((6+mult)*10*input_count*2)+2 + 16

        # 16 -- (?)
        check = input(f"Are you sure want to go on ? (There will "
                      f"be {total_comb}"
                      f" passwords generated)")

        CT = CraftingTable()
        CT.Craft(f"Results/{file_name}",self.dict,total_comb)




if __name__ == "__main__":
    main = KeySmith()

    Main.info()

    # Collecting Data
    main.Collect()

    # Generating
    main.Generate()