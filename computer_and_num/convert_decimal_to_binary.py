def dec2bin(target):
    amari = []

    while target != 0:
        amari.append(target % 2)
        target = target // 2
    
    amari.reverse()
    return amari

answer = dec2bin(5)
print(answer)