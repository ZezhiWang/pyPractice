class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.denom = d
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        elif self.denom == 0:
            raise ZeroDivisionError

    def Add(self, other): # add fractions
        return Fraction (self.num*other.denom+self.denom*other.num, self.denom*other.denom)
    
    def Subtract(self, other): # subtract fractions
        return Fraction (self.num*other.denom-self.denom*other.num, self.denom*other.denom)

    def Multiply(self, other): # mult fractions 
        return Fraction (self.num*other.num, self.denom*other.denom)

    def Divide(self, other): # divide fractions 
        return Fraction (self.num*other.denom, self.denom*other.num)
      
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else:
            return '%s/%s' %(self.num, self.denom)

    def reduceFrac (self ):
       temp = 1
       for i in range(self.num+1,1,-1):
          if self.num % i == 0 and self.denom % i == 0:
             temp = i
             break
       self.num /= temp
       self.denom /= temp
       return Fraction (self.num , self.denom)
       
    def __cmp__(self, arg):
       temp = self.num*arg.denom - self.denom*arg.num
       if temp > 0:
           return 1
       elif temp == 0:
           return 0
       else:
           return -1
    
def main():
    f1 = Fraction(3,4)
    f2 = Fraction(1,2)
    print "F1: " , f1
    print "F2: " , f2
    f3 = Fraction.Add(f1,f2)
    print "Result of addition: ", Fraction.reduceFrac(f3)
    f4 = Fraction.Subtract(f1,f2)
    print "Result of substraction: ", Fraction.reduceFrac(f4)
    f5 = Fraction.Multiply(f1,f2)
    print "Result of multiplication: ", Fraction.reduceFrac(f5)
    f6 = Fraction.Divide(f1,f2)
    print "Result of dividision: ", Fraction.reduceFrac(f6)
    f7 = Fraction.__cmp__(f1,f2)
    print "Result of compare:%s,%s: " %(f1,f2), f7
    f8 = Fraction.__cmp__(f2,f1)
    print "Result of compare:%s,%s: " %(f2,f1), f8
    f9 = Fraction.__cmp__(f1,f1)
    print "Result of compare:%s,%s: " %(f1,f1), f9
   
if __name__ == '__main__':
    main()