first_name = "ada"
last_name = "lovelace"

# sử dụng f-string format để đổi các biến bên trong {} thành giá trị
# f-string có từ Python 3.6
full_name = f"{first_name} {last_name}"
print(full_name)

# thêm "Hello!," ở phía trước
print(f"Hello, {full_name.title()}!")

# gom lại cho gọn
message = f"Hello, {full_name.title()}!"
print(message)

# Python 3.5 trở về trước
full_name2 = "Hello, {} {}!".format(first_name, last_name)
print(full_name2.title())
