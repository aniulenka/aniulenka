weight = 41.5

#ground_shipping
if weight <= 2:
  cost_ground = 1.50 * weight + 20
elif weight <= 6:
  cost_ground = 3.00 * weight + 20
elif weight <= 10:
  cost_ground = 4.00 * weight + 20
else:
  cost_ground = 4.75 * weight + 20

#premium_ground_shipping
cost_premium_ground = 125.00

#drone_shipping
if weight <= 2:
  cost_drone = 4.50 * weight
elif weight <= 6:
  cost_drone = 9.00 * weight
elif weight <= 10:
  cost_drone = 12.00 * weight
else:
  cost_drone = 14.25 * weight


print("Ground Shipping $",cost_ground)
print("Ground Shipping Premimium $", cost_premium_ground)
print("Drone Shipping $", cost_drone)
