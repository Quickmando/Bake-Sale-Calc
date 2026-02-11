# This program calculates the total sales for a bake sale.

#Sold items variables
sold_cupcakes = 12
sold_cookies = 18
sold_brownies = 8
sold_muffins = 7

#Prices of items
price_cupcake = 2.50
price_cookie = 1.75
price_brownies = 3.00
price_muffins = 2.25

#Calculate total sales for each item
total_cupcake_sales = sold_cupcakes * price_cupcake
total_cookie_sales = sold_cookies * price_cookie
total_brownie_sales = sold_brownies * price_brownies
total_muffin_sales = sold_muffins * price_muffins

#Print sales report
#Title and header
print('='*34)
print(' '*5,'BAKE SALE, Sales Report')
print('='*34)
#List of items, quantity sold, price, and total revenue for each item
print('Item       Quantity   Price   Revenue')
print('-'*34)
print(f'Cupcakes    {sold_cupcakes}       ${price_cupcake}    ${total_cupcake_sales}')
print(f'Brownies    {sold_brownies}        ${price_brownies}    ${total_brownie_sales}')
print(f'Cookies     {sold_cookies}       ${price_cookie}   ${total_cookie_sales}')
print(f'Muffin      {sold_muffins}        ${price_muffins}   ${total_muffin_sales}')
print('-'*34)
#Total sales and average price per item
print(f'TOTAL:     {sold_brownies + sold_cookies + sold_cupcakes + sold_muffins}       ${total_cupcake_sales + total_cookie_sales + total_brownie_sales + total_muffin_sales}')
print(f'Average price per item:  {round((price_brownies + price_cookie + price_cupcake + price_muffins)/4, 2)}')

