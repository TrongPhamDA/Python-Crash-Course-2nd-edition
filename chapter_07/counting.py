# # The while Loop in Action
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    # Nếu là số chẵn thì quay lại while (continue)
    if current_number % 2 == 0:
        continue
    # Nếu bỏ qua continue thì in ra các con số
    print(current_number)