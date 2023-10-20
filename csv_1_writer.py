from csv import writer, reader

with open('csv_writer.csv','w',newline='') as f:
    writer_csv= writer(f)
    writer_csv.writerow(['name', 'country'])
    writer_csv.writerow(['Ravi', 'INDIA'])
    writer_csv.writerow(['Pintu', 'INDIA'])
    writer_csv.writerow(['Loki', 'INDIA'])



with open('csv_writer.csv' ,'r') as f1:
    read=reader(f1)
    for i in read:
        print(i)