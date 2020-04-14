#Ground Shipping

#Weight of Package 	                            cost per Pound 	                            Flat Charge
#2 lb or less 	                                          $1.50                                      $20.00
#Over 2 lb but less than or equal to 6 lb 	              $3.00               	                     $20.00
#Over 6 lb but less than or equal to 10 lb 	              $4.00              	                     $20.00
#Over 10 lb 	                                          $4.75                                      $20.00

#Drone Shipping

#Weight of Package 	                            cost per Pound 	                            Flat Charge
#2 lb or less  	                                          $4.50 	                                  $0.00
#Over 2 lb but less than or equal to 6 lb 	              $9.00 	                                  $0.00
#Over 6 lb but less than or equal to 10 lb 	             $12.00                                       $0.00
#Over 10 lb 	                                         $14.25 	                                  $0.00

#Premium Ground Shipping
#Flat Charge: $125.00

def ground_shipping(weight):

    if weight <= 2:
        price_per_pound = 1.5

    elif weight <= 6:
        price_per_pound = 3.0

    elif weight <= 10:
        price_per_pound = 4.0

    else:
        price_per_pound = 4.75

    return 20 + (price_per_pound * weight)

premium_ground_shipping = 125.00

print("Needed for project:")
print(ground_shipping(8.4))

print("---==Testing==---")
print(ground_shipping(1))
print(ground_shipping(5))
print(ground_shipping(7))
print(ground_shipping(11))

def drone_shipping(weight):

    if weight <= 2:
        price_per_pound = 4.50

    elif weight <= 6:
        price_per_pound = 9.00

    elif weight <= 10:
        price_per_pound = 12.00

    else:
        price_per_pound = 14.25

    return price_per_pound * weight

print("Needed for project:")
print(drone_shipping(1.5))

print("---==Testing==---")
print(drone_shipping(1))
print(drone_shipping(5))
print(drone_shipping(7))
print(drone_shipping(11))


def cheapest_method(weight):

    ground = ground_shipping(weight)
    premium = premium_ground_shipping
    drone = drone_shipping(weight)

    if ground < premium and ground < drone:
        method = "standard ground"
        cost = ground

    elif premium < ground and premium < drone:
        method = "premium ground"
        cost = premium

    else:
        method = "drone"
        cost = drone

    print(
        "The cheapest option availiable is $%.2f with %s shipping."
        % (cost, method)
        )

cheapest_method(4.8)
cheapest_method(41.5)
