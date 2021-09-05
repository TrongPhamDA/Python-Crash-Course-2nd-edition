cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    #nếu car là bmw thì in hoa thành BMW và in ra
    if car == 'bmw':
        print(car.upper())
    #nếu không phải bmw thì in title rồi in ra
    else:
        print(car.title())