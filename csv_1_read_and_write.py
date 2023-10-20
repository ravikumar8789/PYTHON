from csv import reader, writer


with open('file.csv','r') as fr:
    with open('read_write.csv', 'w', newline='') as fw:

        read= reader(fr)
        write=writer(fw)
        for i in read:
            write.writerow(i)
        # write.writerow(read)
