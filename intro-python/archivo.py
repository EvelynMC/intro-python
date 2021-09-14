csv = open('car data.csv')

# print(csv.read()) # Lee todo el archivo
# print(csv.readline()) # Lee una línea del archivo.

for x in csv:
    print(x)

csv.close()

# csv.write('\nAgregar nueva línea al archivo') # agrega nueva linea al archivo

