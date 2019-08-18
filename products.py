products = []
with open('products.csv', 'r', encoding='utf-8' ) as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)




while True:
	name = input('請輸入商品名稱： ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格： ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	#簡化1:
	#p=[name, int(price)]
	#products.append(p)
	#簡化2:
	products.append([name, price])
print(products)
for p in products:
	print(p[0], '的價格是', p[1])
#解決亂碼問題（編碼encoding)
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
	

