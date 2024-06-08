import os



class CraftingTable:
    def Craft(self,str):
        def write_to_file(file_path, content):
            if os.path.exists(file_path):
                with open(file_path, "a") as file:
                    file.write(content)
            else:
                with open(file_path, "x") as file:
                    file.write(content)