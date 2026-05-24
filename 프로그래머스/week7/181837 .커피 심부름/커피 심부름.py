def solution(order):
    price = 0
    for i in order:
        if ('americano' in i) or i == 'anything':
            price += 4500
        else:
            price += 5000
    return price