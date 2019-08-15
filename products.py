products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格： ')
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	#簡化1:
	#p=[name, int(price)]
	#products.append(p)
	#簡化2:
	products.append([name, int(price)])
print(products)

