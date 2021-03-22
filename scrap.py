import requests, pprint, openpyxl
from bs4 import BeautifulSoup

''' Extracts all the Name result and details in the site and saves to a textfile'''

class Information:
    new = []
    def __init__(self, name):
        self.name = name
        self.Name_Info()
        self.set_data()
        self.Write_data()

    def Name_Info(self):
        inputted = self.name.replace(' ', '+')
        one = requests.get('https://www.anywho.com/people/'+ inputted)
        print("Status code is", one.status_code)
        swoop = BeautifulSoup(one.text, 'html.parser')
        self.get_all = swoop.find_all('div', "person-info")
        for info in self.get_all:
            self.new.append(info.text)

    def set_data(self):
        self.renew = [all.replace('\t', '') for all in self.new]
        self.final =  [ren.replace('\n', '') for ren in self.renew]
        self.data = [f.replace('View profile', '') for f in self.final]
        pprint.pprint(self.data)

    def Write_data(self):
        textfile = open ('info.csv', 'w')
        file = '\n'.join(self.data)
        textfile.write(file)
        textfile.close()

Information("Richie Alexander")