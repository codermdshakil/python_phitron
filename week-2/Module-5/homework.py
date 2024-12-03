class Pen:
    
    def __init__(self, brand,color ,price):
        self.brand = brand
        self.color = color
        self.price = price


pinpoint_pen = Pen('PinPoint', 'Green', 5)
matador_pen = Pen('Metador', 'Blue', 10)
goodLuck_pen = Pen('Good Luck', 'Red', 10)

print(pinpoint_pen.brand, pinpoint_pen.color, pinpoint_pen.price)
print(matador_pen.brand, matador_pen.color, matador_pen.price)
print(goodLuck_pen.brand, goodLuck_pen.color, goodLuck_pen.price)
