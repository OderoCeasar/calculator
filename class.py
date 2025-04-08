#Assignment Week5 Designing your own class

class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

         

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}"

    def take_photo(self):
        return f"Taking a photo with {self.brand} {self.model}"



# **Inheriting from Smartphone**

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, gpu):
        super().__init__(brand, model)
        self.gpu = gpu  

    def play_game(self, game_title):
        return f"Playing {game_title} on {self.brand} {self.model} with {self.gpu} GPU"



# Regular Smartphone
iphone = Smartphone("Apple", "iPhone 14")
print(iphone.make_call("0703382631")) 


# Gaming Smartphone
asus_rog = GamingSmartphone("ASUS", "ROG Phone 6","Adreno 730")
print(asus_rog.play_game("Fortnite")) 
