def total(weight):
  # calculates ground shipping total
  if (weight<=2):
    ppp1 = 1.50
  elif (6>=weight>2):
    ppp1 = 3.00
  elif (10>=weight>6):
    ppp1 = 4.00
  else:
    ppp1 = 4.75
  ground_total = ppp1*weight + 20.00

  # calculates drone shipping total
  if (weight<=2):
    ppp2 = 4.50
  elif (6>=weight>2):
    ppp2 = 9.00
  elif (10>=weight>6):
    ppp2 = 12.00
  else:
    ppp2 = 14.25
  drone_total = ppp2*weight + 20.00

  return ground_total, drone_total

def cheapest():
  # returns the chippest method
  weight = float(input("Please enter the weight:\n"))
  gt , dt = total(weight)
  pt = 125.00
  if (gt<dt):
    if (dt<pt):
      return "Ground Shipping is your best option!"
    else:
      if (gt<pt):
        return "Ground Shipping is your best option!"
      else:
        return "Premium Shipping is your best option!"
      
  else:
    if (dt<pt):
      return "Drone Shipping is your best option!"
    else:
      return "Premium Shipping is your best option!"
  


def main():
  # prints out your best option
  best_option = cheapest()
  print(best_option)

if __name__=="__main__":
  main()


