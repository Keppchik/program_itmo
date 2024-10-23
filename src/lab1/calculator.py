class Calculator:
    def calc_add(self,first, second):
        return first + second

    def calc_minus(self,first, second):
        return first - second

    def calc_multiply(self,first, second):
        return first * second

    def calc_divide(self,first, second):
        try:
            return first / second
        except ZeroDivisionError:
            return "Error: division by zero"

    def get_function(self):
        s = input("Enter a mathematical expression(Ex. 12 + 34): ").split()
        if len(s) == 3:
            if s[1] == "+":
                return Calculator.calc_add(self,int(s[0]),int(s[2]))
            if s[1] == "-":
                return Calculator.calc_minus(self,int(s[0]),int(s[2]))
            if s[1] == "*":
                return Calculator.calc_multiply(self,int(s[0]),int(s[2]))
            if s[1] == "/":
                return Calculator.calc_divide(self,int(s[0]),int(s[2]))
        else:
            return "Wrong expression"



if __name__ == '__main__':
    print(Calculator().get_function())