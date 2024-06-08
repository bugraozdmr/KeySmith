from colorama import Fore, Style


class GetInfo:
    def __init__(self, name=None, petname=None, city=None, team=None, county=None, birthday=None):
        self.name = name
        self.petname = petname
        self.city = city
        self.county = county
        self.team = team
        self.birthday = birthday

        self.data = {
            'name': self.name,
            'petname': self.petname,
            'city': self.city,
            'team': self.team,
            'county': self.county,
            'birthday': self.birthday
        }

    def SetInfo(self):
        # print(f"{Fore.CYAN}{Fore.YELLOW}Warning : /Only designed as a project, abuse is not my problem/{Fore.YELLOW}{Fore.RESET}")
        print(f"{Style.BRIGHT}{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}]{Fore.RESET}{Style.NORMAL}{Fore.YELLOW} Data Collecting{Fore.YELLOW}{Fore.RESET}")

        name = input("Name of the target : ")
        if(name is not None):
            self.name = name.strip()

        pet_name = input("Name of the target's pet name (if any) : ")
        if (pet_name is not None):
            self.petname = pet_name.strip()


        city_name = input("Name of the city : ")
        if (city_name is not None):
            self.city = city_name.strip()

        county_name = input("Name of the county : ")
        if (county_name is not None):
            self.county = county_name.strip()

        team_name = input("Name of the team : ")
        if (team_name is not None):
            self.team = team_name.strip()

        birthday_d = input("arget's birthday : (if it is known)")
        if (birthday_d is not None):
            self.birthday = birthday_d.strip()


        self.data['name'] = self.name
        self.data['petname'] = self.petname
        self.data['city'] = self.city
        self.data['county'] = self.county
        self.data['birthday'] = self.birthday
        self.data['team'] = self.team

        print("\n\n")