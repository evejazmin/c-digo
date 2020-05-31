# devices=['R1',"R2",'R3','S1','S2']
# for item in devices:
#     print(item)
# switches=[]
# for item in devices:
#     if 'S' in item:
#         switches.append(item)
# print(switches)
while True:
    x=input('Ingrese el numero para contar: ')
    if x=='q' or x== 'quit':
        break
    x=int(x)
    y=1
# while y<=x:
#     print(y)
#     y+=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break