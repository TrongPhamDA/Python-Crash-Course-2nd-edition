#Integer: whole number
print("Integer")
print(2+3)
print(3-2)
print(2*3)
print(3/2)
#nâng lên lũy thừa (Power)
print(3**2)
print(3**3)
print(10**6)

#Floats: decimal numer
print("\nFloat")
print(0.1+0.1)
print(0.2+0.2)
print(2*0.1)
print(.2*2)
print(0.2 + 0.1)
#Cẩn thận với Float, vì số lẻ
print(0.2+0.1==0.3)
print(1+2==3)

#phép chia luôn cho ra kết quả Float
print("\nPhép chia")
print(4/2)
#dính liếu tới Float luôn cho ra kết quả Float
print(1+2.0)
print(2*3.0)
print(3.0**2)

#Viết thêm dấu _ để dể nhìn số
print("\nUnder_score_in_Number")
universe_age = 14_000_000_000
#khi được print ra, số sẽ ko hiển thị dấu _
print(universe_age)

#Gán nhiều tham số cùng lúc
print("Multiple Assignment")
x,y,z = 1,2,3
print(x)
print(y)
print(z)

#CONSTANTS (hằng số)
#Python ko có kiểu hằng số, nhưng có thể viết INHOA để tự hiểu là Hằng số không đổi
print("\nConstants")
MAX_CONNECTIONS = 5_000
print(MAX_CONNECTIONS)
