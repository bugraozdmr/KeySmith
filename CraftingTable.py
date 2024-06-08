

from colorama import Fore, Style


class CraftingTable:
    def Craft(self,file_path,dict,total):
        common_numbers = [1, 12, 123, 1234, 12345, 123456]
        common_characters = ['/','@','#','$','!','?','_','-','.',',']
        birthday_d = 0

        # counter
        counter = 0

        try:
            bd = dict['birthday'].split(".")
            if len(bd) is not None:
                day_of_birthday = bd[0]
                year_of_birthday = bd[0]
                birthday_d = f"{bd[0]}{bd[1]}{bd[2]}"



                common_numbers.append(day_of_birthday)
                common_numbers.append(year_of_birthday)
                common_numbers.append(birthday_d)

        except:
            print("Could not split the birthday")


        print(f"{Style.BRIGHT}{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}]{Fore.RESET}{Style.NORMAL}{Fore.YELLOW} Generating{Fore.YELLOW}{Fore.RESET}")


        with open(file_path, "w") as file:
                # with common numbers
                first = 0
                for i in common_numbers:
                    if (first % 3 == 2):
                        print(f"{counter}/{total} done")


                    if(dict['name'] != "" and dict['name'] != None):
                        file.write(f"{dict['name']}{i}\n")
                        file.write(f"{dict['name'].capitalize()}{i}\n")
                        counter += 2

                    if (dict['team'] != "" and dict['team'] != None):
                        file.write(f"{dict['team']}{i}\n")
                        file.write(f"{dict['team'].capitalize()}{i}\n")
                        counter += 2

                    if (dict['city'] != "" and dict['city'] != None):
                        file.write(f"{dict['city']}{i}\n")
                        file.write(f"{dict['city'].capitalize()}{i}\n")
                        counter += 2


                    if (dict['petname'] != "" and dict['petname'] != None):
                        file.write(f"{dict['petname']}{i}\n")
                        file.write(f"{dict['petname'].capitalize()}{i}\n")
                        counter += 2

                    if (dict['country'] != "" and dict['country'] != None):
                        file.write(f"{dict['country']}{i}\n")
                        file.write(f"{dict['country'].capitalize()}{i}\n")
                        counter += 2

                    first += 1


                if (birthday_d != 0):
                    file.write(f"{birthday_d}\n")
                file.write(f"12345\n")
                file.write(f"123456\n")

                counter += 2

                if (counter % 86 == 83): print(f"{counter}/{total} done")

                second = 0
                for i in common_characters:
                    if (second % 3 == 2):
                        print(f"{counter}/{total} done")
                    temp = 0
                    for j in common_numbers:
                        if (dict['name'] != "" and dict['name'] != None):
                            if(temp == 0):
                                file.write(f"{i}{dict['name']}\n")
                                file.write(f"{i}{dict['name'].capitalize()}\n")
                                counter += 2

                            file.write(f"{i}{dict['name'].capitalize()}{i}\n")
                            file.write(f"{i}{dict['name']}{i}\n")
                            counter += 2

                        if (dict['city'] != "" and dict['city'] != None):
                            if(temp == 0):
                                file.write(f"{i}{dict['city']}\n")
                                file.write(f"{i}{dict['city'].capitalize()}\n")
                                counter += 2

                            file.write(f"{i}{dict['city'].capitalize()}{i}\n")
                            file.write(f"{i}{dict['city']}{i}\n")
                            counter += 2


                        if (dict['team'] != "" and dict['team'] != None):
                            if(temp == 0):
                                file.write(f"{i}{dict['team']}\n")
                                file.write(f"{i}{dict['team'].capitalize()}\n")
                                counter += 2

                            file.write(f"{i}{dict['team'].capitalize()}{i}\n")
                            file.write(f"{i}{dict['team']}{i}\n")
                            counter += 2

                        if (dict['petname'] != "" and dict['petname'] != None):
                            if (temp == 0):
                                file.write(f"{i}{dict['petname']}\n")
                                file.write(f"{i}{dict['petname'].capitalize()}\n")
                                counter += 2

                            file.write(f"{i}{dict['petname'].capitalize()}{i}\n")
                            file.write(f"{i}{dict['petname']}{i}\n")
                            counter += 2

                        if (dict['country'] != "" and dict['country'] != None):
                            if (temp == 0):
                                file.write(f"{i}{dict['country']}\n")
                                file.write(f"{i}{dict['country'].capitalize()}\n")
                                counter += 2

                            file.write(f"{i}{dict['country'].capitalize()}{i}\n")
                            file.write(f"{i}{dict['country']}{i}\n")
                            counter += 2


                        temp = 1
                    second += 1
        print("Done")

