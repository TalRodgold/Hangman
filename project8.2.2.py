def price(my_tuple):
    return float(my_tuple[1])

def sort_prices(list_of_tuples):
    print(sorted(list_of_tuples, key=price, reverse=True))

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)