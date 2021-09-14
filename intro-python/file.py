# Importar modulos necesarios
import csv
from os import read, write

# csv = open('car data.csv')
# print(csv.read()) # Lee todo el archivo
# print(csv.readline()) # Lee una línea del archivo.
# csv.write('\nAgregar nueva línea al archivo') # agrega nueva linea al archivo

# Lectura de CSV

cars_array = []

with open('car data.csv', encoding = 'UTF8', newline='') as csv_file:
    data = csv.DictReader(csv_file)          # Lee y convierte en diccionario
    # car_data = csv.reader(csv_file)        # Lee como CSV normal

    for row in data:
        # print(row['Car_Name'],row['Year'],row['Selling_Price'])
        car_name = row['Car_Name']
        car_year = row['Year']
        car_price = row['Selling_Price']
        
        cars_array.append({
            'name' : car_name,
            'year': car_year,
            'price': car_price
        })
# print(cars_array) 


# Writing CSV

fieldnames = ['name', 'year', 'price' ]

with open('new car data.csv', 'w', encoding = 'UTF8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cars_array)

