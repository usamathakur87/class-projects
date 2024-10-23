# Store Checkout Program

# Step 1: Ask the user to input the number of items purchased and the price of each item
num_items = int(input("Enter the number of items purchased: "))  # Input number of items
price = 0  # Variable to store the total price of all items

# Step 2: Loop to get the price of each item and add it to the total 'price'
for i in range(num_items):
    item_price = float(input(f"Enter price for item {i+1}: "))  # Input price of each item
    price += item_price  # Add item price to total price

# Step 3: Define discount policy based on total price
if price <= 10000:
    discount_percentage = 10
elif 10001 <= price <= 25000:
    discount_percentage = 15
elif 25001 <= price <= 50000:
    discount_percentage = 20
elif price > 75000:
    discount_percentage = 30
else:
    discount_percentage = 0  # No discount for amounts between 50001 and 75000

# Step 4: Apply GST (General Sales Tax)
gst_percentage = 17  # GST is 17%
gst_amount = (price * gst_percentage) / 100  # Calculate GST amount

# Step 5: Calculate Gross Total (Total price after GST)
gross_total = price + gst_amount

# Step 6: Calculate discount amount based on total price (before tax)
discount_amount = (price * discount_percentage) / 100

# Step 7: Calculate Net Total (Price after applying discount)
net_total = gross_total - discount_amount

# Step 8: Print out the receipt with all the details
print("\n--- Checkout Receipt ---")
print(f"Number of items purchased: {num_items}")  # Print number of items
print(f"Total Amount (before GST): {price}")  # Print total price before GST
print(f"GST @ {gst_percentage}%: {gst_amount}")  # Print GST percentage and amount
print(f"Gross Total (after GST): {gross_total}")  # Print total amount after GST
print(f"Discount @ {discount_percentage}%: {discount_amount}")  # Print discount percentage and amount
print(f"Net Total (after discount): {net_total}")  # Print final total after applying discount
