import requests, pprint
from bs4 import BeautifulSoup

class Information:
    new = []
    def __init__(self, name):
        self.name = name

    def Name_Info(self):
        inputted = self.name.replace(' ', '+')
        one = requests.get('https://www.anywho.com/people/'+ inputted)
        print("Status code is", one.status_code)
        swoop = BeautifulSoup(one.text, 'html.parser')
        self.get_all = swoop.find_all('div', "person-info")

        for info in self.get_all:
            self.new.append(info.text)
        self.renew = [all.replace('\t', '')for all in self.new]
        self.final =  [ren.replace('\n', '')for ren in self.renew]
        self.data = [ren.replace('View profile', '')for ren in self.renew]

        textfile = open ('info.txt', 'w')
        file = ','.join(self.data)
        textfile.write(file)
        textfile.close()

Information("Maranda Curtis").Name_Info()