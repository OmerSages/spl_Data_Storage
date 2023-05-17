from persistence import *


def printAll(table, order_by):
    print(table)
    dao_type = table.lower()
    for dto in repo.__dict__[dao_type].find_all(order_by):
        string_dto = [x.decode() if isinstance(x, bytes) else x for x in vars(dto).values()]
        print(tuple(string_dto))

def print_employee_report():
    join_script = 'SELECT employees.id, employees.name, employees.salary, branches.location FROM employees JOIN branches ON employees.branche = branches.id ORDER BY name'
    for row in repo.execute_command(join_script):
        select_script = 'SELECT activities.quantity, products.price FROM activities JOIN products ON activities.product_id = products.id WHERE activities.activator_id = {}'.format(row[0])
        total_sales_income = 0
        for sale in repo.execute_command(select_script):
            total_sales_income+=sale[0]*sale[1]
        string_row = [x.decode() if isinstance(x, bytes) else str(x) for x in row[1:]]
        print(' '.join(string_row)+' '+str(total_sales_income*(-1)))

def print_activities_report():
    script = 'SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name FROM activities JOIN products ON activities.product_id = products.id\
        LEFT JOIN employees ON activities.activator_id = employees.id LEFT JOIN suppliers ON activities.activator_id = suppliers.id ORDER BY activities.date ASC'
    for row in repo.execute_command(script):
        fix_row = [x.decode() if isinstance(x, bytes) else x for x in row]
        print(tuple(fix_row))

def main():
    #TODO: implement

    tables = ['Branches','Employees','Products','Suppliers']
    printAll('Activities','date')
    for table in tables:
        printAll(table,'id')
    print()
    print('Employees report')
    print_employee_report()
    print()
    print('Activities report')
    print_activities_report()
    
if __name__ == '__main__':
    main()