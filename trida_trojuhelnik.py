import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

#task a
    def istriangle(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            return False

#task b 
    def right(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False
        
#task c         
    def content(self):
        s = (self.a + self.b + self.c)/2
        S = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return S
    
#task d   
    def perimeter(self):
        o = self.a + self.b + self.c
        return o
    
#task e  
    def sides(self):
        if self.a == self.b == self.c:
            print("Triangle is equilateral.")
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.b):
            print("Triangle is isosceles.")
        else:
            print("Triangle is not equilateral or isosceles.")


#task f
    def radius_of_circumscribed(self):
        r = (self.a*self.b*self.c)/4(self.content())
        return r

#task i
    def degrees(self):
        alpha = math.degrees(math.acos(self.b**2 + self.c**2 - self.a**2)/(2*self.b*self.c))
        beta = math.degrees(math.acos(self.c**2 + self.a**2 - self.b**2)/(2*self.c*self.a))
        gama = math.degrees(math.acos(self.a**2 + self.b**2 - self.c**2)/(2*self.a*self.b))
        return alpha, beta, gama
#task 
    def sharpness(self):
        self.degrees()
        if self.a**2 + self.b**2 == self.c**2:
            print("Triangle is right.")
        elif (self.alpha > 90) or (self.beta > 90) or (self.gama > 90):
            print("Triangle is obtuse.")
        elif (self.alpha < 90) and (self.beta < 90) and (self.gama < 90):
            print("Triangle is sharp-angled.")
    
        
    
