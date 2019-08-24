# 檢查檔案是否存在：
# 讀取檔案：
def read_file(filename):
		products = []
		with open(filename, 'r', encoding='utf-8' ) as f:
			for line in f:
				if '商品,價格' in line:
					continue          #continue: 跳到下一迴圈
				name, price = line.strip().split(',')
				products.append([name, price])
		return products
# 讓使用者輸入：
def user_input(products):
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
	return products
# 印出所有購買紀錄：
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])
# 寫入檔案：
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:  # 解決亂碼問題（編碼encoding)
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	import os #operating system
	filename = 'products.csv'
	if os.path.isfile(filename):  
		print('yes!found the file!')
		products = read_file(filename)  # 有return, function執行結果就可以存下來
	else:
		print('oops!no file > <')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main()	

