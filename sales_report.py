"""Generate sales report showing total melons each salesperson sold."""

#Empty lists to put broken up string into
salespeople = []
melons_sold = []
#Calling the txt file so it can be accessed within py file
sales_report = open('sales-report.txt')
#Starting loop to go through and break apart strings in txt file
for line in sales_report:
    line = line.rstrip()
    entries = line.split('|')
    #Assiening indexes from broken up txt into empty lists
    salesperson = entries[0]
    melons = int(entries[2])
    #Checking for if the salesperson exists
    if salesperson in salespeople:
        #Assiening new variable as individual salespeople
        position = salespeople.index(salesperson)
        #Adding melons sold for salesperson
        melons_sold[position] += melons
    #If not in salespeople then add to salespeople and add there sold melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#For the index within the range of salepeople
for i in range(len(salespeople)):
    #Print there name and melons they've sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')