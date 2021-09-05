#Chạy vòng For để tạo ra List các Bình phương của dãy số [1..10]
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#Cách viết gọn lại
squares2 = [value2**2 for value2 in range(1, 11)]
print(squares2)
