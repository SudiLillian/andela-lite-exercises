def fizzbuzz(n):
    if type(n) != int:
        return 'pass in a integer.'
    else:
        if n % 15 == 0:
            return 'fizzbuzz'
        elif n % 5 == 0:
            return 'buzz'
        elif n % 3 == 0:
            return 'fizz'
        else:
            return n