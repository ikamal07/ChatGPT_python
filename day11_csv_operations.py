import csv

with open('employee_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Age','Department'])
    writer.writerow(['John',33,'IT'])
    writer.writerow(['Victor',23,'Finance'])
    writer.writerow(['Chris',31,'IT'])
    writer.writerow(['Jonathan',43,'IT'])
    writer.writerow(['Raj',37,'Payroll'])

with open('employee_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if 'IT' in row:
            print(row)
        
        









                    



