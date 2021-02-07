def fizzbuzz(n):
    if (n % 3 == 0 and n % 5 != 0):
        return "Fizz"
        pass
    elif (n % 3 != 0 and n % 5 == 0):
        return "Buzz"
        pass
    elif (n % 3 != 0 and n % 5 != 0):
        return n
        pass
    else:
        return "FizzBuzz"
        pass

n = int(input("Digite um número inteiro: "))
print(fizzbuzz(n))