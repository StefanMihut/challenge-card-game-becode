class Symbol:
    color = ("Red", "Black")
    icon = ["♥", "♦", "♣", "♠"] # "♥" 
    #Class representing the symbol
    def __init__(self,color,icon):
            self.color = color
            self.icon = icon

    def __str__(self):
        return f"{self.color} {self.icon}"
        #def __str__(self):
            #return f"{Symbol.icon[self.icon]} {Symbol.color[self.color]}"

class Card(Symbol):
        #value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, color, icon, value):
        Symbol.__init__(self,color,icon)
        self.value = value
        #value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __str__(self) -> str:
        return f"{self.value} {self.color}{self.icon}"

#c1 = Card("Red"," ♣ ", "4")
#c2 = Symbol("Black", "♣")
#c1.icon
#c2.icon

#print(c1)