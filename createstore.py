def create_store():
    a = open("inventory.txt","w")
    a.write('ID,PRODUCT,PRICE,STOCK\n')
    a.close()
create_store()
