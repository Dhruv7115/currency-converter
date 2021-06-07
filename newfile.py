# 1 us dollar = 72.82 rupees
# 1 pound = 103.25 rupees
#1 pound = 1.42 dollars
print('welcome to currency converter')
option = '''1. Rupees to US Dollars
2. US Dollars to Rupees
3. Rupees to Pounds
4. Pounds to Rupees
5. Pound to US Dollar 
6. US Dollar to pound'''
print(option)

choice = int(input('Enter your choice here: '))
if choice==1:
	v1 = int(input('Enter the value here: '))
	print(f'₹{v1} = ${v1/72.82}')
	
elif choice==2:
	v2 = int(input('Enter the value here: '))
	print(f'${v2} = ₹{v2*72.82}')
	
elif choice==3:
	v3 = int(input('Enter the value here: '))
	print(f'₹{v3} = {v3/103.25} Pounds')
	
elif choice==4:
	v4 = int(input('Enter the value here: '))
	print(f'{v4} Pounds = ₹{v4*103.25}')
	
elif choice==5:
	v5 = int(input('Enter the value here: '))
	print(f'{v5} Pounds = ${v5*1.42}')
	
elif choice==6:
	v6 = int(input('Enter the value here: '))
	print(f'${v6} = {v6/1.42} Pounds')