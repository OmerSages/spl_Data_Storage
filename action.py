from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            product_id = int(splittedline[0])
            input_quantity = int(splittedline[1])
            product = repo.products.find(id = product_id)[0]
            prev_quantity = product.quantity

            if(input_quantity!=0 and prev_quantity+input_quantity >= 0):
                repo.products.update(quantity = prev_quantity+input_quantity ,id=product_id)
                repo.activities.insert(Activitie(*splittedline))

if __name__ == '__main__':
    main(sys.argv)