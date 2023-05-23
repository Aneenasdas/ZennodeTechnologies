print("Here is the catalog of 3 products")
print("Product Name\tPrice")
print("Product A\t\t$20")
print("Product B\t\t$40")
print("Product C\t\t$50")

# Input quantity and gift wrap for each product
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}
quantities = {}
gift_wraps = {}
for product in products:
    quantity = int(input(f"Enter quantity for {product}: "))
    wrap = input(f"Wrap {product} as a gift? (yes/no): ")
    quantities[product] = quantity
    gift_wraps[product] = wrap.lower() == "yes"

# Calculate subtotal
subtotal = 0
for product in products:
    subtotal += quantities[product] * products[product]

# Apply discount rule
discount_rules = {
    "flat_10_discount": {"threshold": 200, "discount_amount": 10},
    "bulk_5_discount": {"threshold": 10, "discount_percent": 0.05},
    "bulk_10_discount": {"threshold": 20, "discount_percent": 0.1},
    "tiered_50_discount": {"total_threshold": 30, "individual_threshold": 15, "discount_percent": 0.5}
}
applicable_discounts = []

# Find applicable discounts
discount_applicable = {}
temp = 0
for rule in discount_rules:
    print(rule)
    if rule == "flat_10_discount" and subtotal > discount_rules[rule]["threshold"]:
        discount_applicable[rule] = discount_rules[rule]["discount_amount"]
    if rule == "bulk_5_discount":
        for i in quantities:
            if quantities[i] > discount_rules[rule]["threshold"]:
                temp += (quantities[i] * products[i]) * discount_rules[rule]["discount_percent"]
        discount_applicable[rule] = temp
        temp = 0
    if rule == "bulk_10_discount" and sum(quantities.values()) > discount_rules[rule]["threshold"]:
        discount_applicable[rule] = subtotal * discount_rules[rule]["discount_percent"]
    if rule == "tiered_50_discount" and sum(quantities.values()) > discount_rules[rule]["total_threshold"]:
        for i in quantities:
            if quantities[i] > discount_rules[rule]["individual_threshold"]:
                quantity_temp = quantities[i] - discount_rules[rule]["individual_threshold"]
                temp += (quantity_temp * products[i]) * discount_rules[rule]["discount_percent"]
        discount_applicable[rule] = temp
maximum = 0
discount = ""
for i in discount_applicable:
    if discount_applicable[i] > maximum:
        maximum = discount_applicable[i]
        discount = i

# Calculate shipping fee
shipping_fee_per_package = 5
units_per_package = 10
total_units = sum(quantities.values())
total_package = 0
shipping_fee = 0
while total_units > 0:
    total_units = total_units - units_per_package
    total_package = total_package + 1
shipping_fee = total_package * shipping_fee_per_package

# Calculate gift wrap fee
gift_wrap_fee = sum(quantities[product] for product in quantities if gift_wraps[product])

# Calculate total
total = subtotal - maximum + shipping_fee + gift_wrap_fee

# Output
for product in quantities:
    total_amount = quantities[product] * products[product]
    print(f"Product: {product}, Quantity: {quantities[product]}, Total Amount: ${total_amount}")
print(f"\nSubtotal: ${subtotal}")
print(f"Discount Applied: {discount}, Discount Amount: ${maximum}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total: ${total}")