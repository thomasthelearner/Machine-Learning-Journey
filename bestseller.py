import csv

max_sale = 0
best_seller_book = None

with open('Bestseller.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        current_sale = float(row[4])  # Assuming the sales column is at index 4

        if current_sale > max_sale:
            max_sale = current_sale
            best_seller_book = row

with open('bestseller_info.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(best_seller_book)

