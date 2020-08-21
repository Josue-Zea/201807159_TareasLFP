import csv

with open("archivocsv.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print("id: {0}, nombre: {1}, apellido: {2}, telefono: {3}, email: {4}".format(row[0],row[1],row[2],row[3],row[4]))
        print(type(reader))
        print()