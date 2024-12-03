
class Calculate:
    def sum(self,num1, num2):
        result = num1 + num2
        return result
    def mul(self,num1, num2):
        result = num1 * num2
        return result
    def sub(self,num1, num2):
        result = num1 - num2
        return result
    def div(self,num1, num2):
        result = num1/num2
        return result
    
    

call_calculate = Calculate()

print(call_calculate.sum(10, 40))
print(call_calculate.sub(40, 20))
print(call_calculate.mul(10, 5))
print(call_calculate.div(50, 5))

