import requests
response = requests.get('https://api.namefake.com/')
data = response.json()
print(data['name'])

'''class Students:
    def __init__(self,id,name):
        self.id = id
        self.name = name'''
        
        