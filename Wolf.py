class Wolf():
    def __init__(self,breed):
        self.breed = breed
    
    has_four_legs = True
    sound = "Aww"
wolf1 = Wolf('Indian Wolf')
wolf2 = Wolf('Grey Wolf')
wolf3 = Wolf('Red Wolf')

print(wolf1.breed)
print(wolf2.breed)
print(wolf3.breed)
print('wolf1 makes sound '+ wolf1.sound)
