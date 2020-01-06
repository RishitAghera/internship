def square_of_sum(number):
    square=0
    for i in range(1,number+1):
        square+=i
    return square*square


def sum_of_squares(number):
    square=0
    for i in range(1,number+1):
        square+=(i*i)
    return square

def difference_of_squares(number):
    return abs(square_of_sum(number)-sum_of_squares(number))


print(difference_of_squares(10))