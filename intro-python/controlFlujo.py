# IF Control de Flujo

# if 2 < 5:
    # print('2 es menor que 5')

# a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b

# if 2 == 2:
#     print('2 es igual a 2')

# if 2 ==3:
#     print('2 es igual a 3')

# if 2 > 5:
#     print('2 es mayor que 5')

# if 5 > 2:
#     print('5 es mayor a 2')

# if 2 != 2:
#     print('2 es distinto a 2')

# if 3 !=2:
#     print('3 es distinto a 2')

# if 3<=3:
#     print('3 es menor o igual a 3')


if 2 > 5:
    print('dos es menor a 5 en if')
elif 2 > 5:
    print('2 es menor a 5 en elif')
else: 
    print('Yo me imprimo solo si todo lo anterior evalua en falso')



if 2 > 5:
    print('dos es menor a 5 en if')
else:
    print('Yo me imprimo solo si todo lo anterior evalua en falso 2')

#----- IF Ternarios ----

if 2 < 5: print('if de una linea')

print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false')


#----- AND/OR ----

if 2 < 5 and 3 > 2:
    print ('ambas devuelven true')

if 2 > 5 and 3 > 2:
    print ('hay una falsa, esto no se mostrara')

if 1 < 0 or 1 > 0:
    print('una de las dos condiciones devolvio true')