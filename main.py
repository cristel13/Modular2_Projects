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

