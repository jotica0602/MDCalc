from functools import cache
amount_and_prices = [(1,100),(2.5,200),(16,950),(1.4,110),(3.5,250),(8,500)]

buys = {ap:0 for ap in amount_and_prices}
best = [float('-inf')]

@cache
def getbest(actual,money,index):
    if money < 0:
        return {}, float('-inf')
    
    if index == len(amount_and_prices) or money == 0:
        if best[0] < actual:
            best[0] = actual
        return buys.copy(),actual
    
    a,p = amount_and_prices[index]
    
    # Keep buying
    buys[(a,p)] += 1
    b1 = getbest(actual + a, money - p, index)
    buys[(a,p)] -= 1
    
    # Buy and move
    buys[(a,p)] += 1
    b2 = getbest(actual + a, money - p, index + 1)
    buys[(a,p)] -= 1
    
    # Pass
    b3 = getbest(actual, money, index + 1)
    
    return max(b1,b2,b3,key=lambda b:b[1])

while True:
    try:
        money = int(input('Introduce la cantidad de dinero de la que dispones:\n>'))
        if money < 100:
            print('No hay nada que puedas comprar con esa cantidad.')
            break
        else: break
    except ValueError:
        print('Entrada inválida.')
    

seq, best = getbest(0,money,0)

def parse(gb,price,amount):
    match gb:
        case 1:
            return f'{amount} Paquete/s de 1 GB LTE x {price} CUP'
        case 2.5:
            return f'{amount} Paquete/s de 2.5 GB LTE x {price} CUP'
        case 16:
            return f'{amount} Paquete/s de 4 GB + 12 GB LTE x {price} CUP'
        case 1.4:
            return f'{amount} Plan/es 600MB + 800MB LTE x {price} CUP'
        case 3.5:
            return f'{amount} Plan/es 1.5GB + 2GB LTE x {price} CUP'
        case 8:
            return f'{amount} Plan/es 3.5GB + 4.5GB LTE x {price} CUP'

seq = [parse(*item,seq[item]) for item in seq if seq[item] != 0]
print(f'La mayor cantidad de datos móviles que puedes obtener es {best} gb')
print(f'Para ello realiza la compra de:')
print(*seq,sep='\n')
