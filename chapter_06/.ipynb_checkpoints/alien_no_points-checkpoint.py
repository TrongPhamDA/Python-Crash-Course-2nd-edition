#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
#Get trả về 0 khi không tìm thấy key 'points' trong từ điển alien_0
point_value = alien_0.get('points', 0)
print(point_value)
point_value = alien_0.get('points', "No point value assigned.")
print(point_value)
#get() trả về 'None' nếu không có option nào khác
point_value = alien_0.get('points')
print(point_value)