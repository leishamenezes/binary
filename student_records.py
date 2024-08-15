import csv

def write():
    f = open("Student.csv", "w",newline='')
    s_writer = csv.writer(f)
    s_writer.writerow(['Roll No', 'Name', 'Marks'])
    rec = []

    while True:
        r = int(input("Enter the roll number: "))
        n = input("Enter name: ")
        m = int(input("Enter marks: "))

        lst = [r, n, m]
        rec.append(lst)

        ch = input("Do you want to enter more records (Y/N): ")
        if ch.upper() == 'N':
            break

    s_writer.writerows(rec)
    f.close()

def read():
    f = open("Student.csv", "r")
    s_reader = csv.reader(f)

    for i in s_reader:
         print(i)

    f.close()
write()

read()
