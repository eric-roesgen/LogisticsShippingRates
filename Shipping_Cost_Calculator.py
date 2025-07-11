#Shipping Cost Calculator

##Input package weight and shipping rate
weight=float("Enter the package weight in kilogram: ")
rate=float(input("Enter the shipping rate per kilogram: "))

shipping_cost=weight*rate

print(f"Shipping cost: {shipping_cost} USD")
