num = int(input())
is_prime = True
if num == 1:
	print('no')
else:	
	for i in range(2,int(num**0.5)+1):
		if num % i == 0:
			is_prime = False
			break
	if is_prime:
		print('yes')
	else:
		print('no')        
