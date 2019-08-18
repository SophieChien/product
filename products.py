# 檢查檔案是否存在：
# 讀取檔案：
import os #operating system
products = []
if os.path.isfile('products.csv'):  
	print('yes!found the file!')
	with open('products.csv', 'r', encoding='utf-8' ) as f:
		for line in f:
			if '商品,價格' in line:
				continue          #continue: 跳到下一迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('oops!no file > <')

# 讓使用者輸入：
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

# 印出所有購買紀錄：
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案：
with open('products.csv', 'w', encoding='utf-8') as f:  # 解決亂碼問題（編碼encoding)
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
	

