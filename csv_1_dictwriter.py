from csv import DictWriter


with open('final.csv', 'w', newline='') as f:
    write= DictWriter(f, fieldnames=['name', 'age', 'roll'])

    write.writeheader()


    write.writerow({
        'name':'ravi',
        'age':24,
        'roll':63
    })
    write.writerow({
        'name':'pintu',
        'age':21,
        'roll':64
    })