class MyCode:
    def add(x, y):
        result = x + y
        MyCode.publish(result)
        return result

    def subtract(x, y):
        result = x - y
        MyCode.publish(result)
        return result

    def multiply(x, y):
        result = x * y
        MyCode.publish(result)
        return result

    def divide(x, y):
        result = x / y
        MyCode.publish(result)
        return result
    
    @staticmethod
    def publish(result):
        print(result)


# calc = MyCode
# calc.add(2, 1)
# calc.subtract(2, 1)
# calc.multiply(2, 1)
# calc.divide(2, 1)
