def fizzBuzz(upTo):
    i = 1
    while i <= upTo:
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz', end=' ')
            i+=1
        elif i%3 == 0:
            print('Fizz', end=' ')
            i+=1
        elif i%5 == 0:
            print('Buzz', end=' ')
            i+=1
        else:
            print(i, end=' ')
            i+=1

fizzBuzz(55)
