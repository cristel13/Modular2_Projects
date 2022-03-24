def volatile(prices):
  cheated_days = 0
  next_number = 0
    
  for i in range(0,len(prices)):
    print(next_number == len(prices) - 1)
    if prices[i] >= prices[next_number + 1]:
      cheated_days += 1
      next_number += 1
    if next_number == len(prices) - 1:
        if prices[i] == prices[next_number] and cheated_days > 0:
            cheated_days = 0
            break   
        elif prices[i] == prices[next_number]:
            cheated_days-= 1
            break
    return cheated_days

print(volatile([7,7,7,7]))
# def nature_lover(up_speed, down_speed, target_height):
#     height = 0
#     is_growing = True
#     days = 0
#     while is_growing:
#       height += up_speed
#       height -= down_speed
#       days += 1
#       print(height)
#       if height >= target_height:
#         is_growing = False
#         if height > target_height:
#             days-=1
       

#     return days

# print(nature_lover(8,7,23))

