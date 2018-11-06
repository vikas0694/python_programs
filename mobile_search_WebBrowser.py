
import webbrowser
class Mobile():
    def __init__(self ,brand_name,model_name,mobile_price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.mobile_price = mobile_price
    def search_online(self):
        webbrowser.open("https://www.google.co.in/search?q="+str(self.model_name))
mobile1 = Mobile("samsung","galaxy A5 (2017)",23000)
mobile2 = Mobile("motorola", "moto G4",1400)
mobile1.search_online()
mobile2.search_online()
print(mobile1.model_name)
print(mobile2.mobile_price)
help(list)
print("model name is: "+ mobile2.model_name)