import csv


def modify_csv(input_filename, output_filename):
    """
    Modifies a CSV file to show a stronger correlation between 20-30% discounts and increased revenue.

    Args:
      input_filename: The name of the input CSV file.
      output_filename: The name of the output CSV file.
    """

    with open(input_filename, "r") as infile, open(
        output_filename, "w", newline=""
    ) as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            discount = float(row["discount"])
            revenue = float(row["revenue"])
            quantity = int(row["quantity"])
            price = float(row["product_price"])

            if 20 <= discount <= 30:
                # Choose one of the following options to increase revenue:

                # Option 1: Directly increase revenue
                revenue *= 1.2  # Increase by 20%

                # Option 2: Increase quantity
                # quantity += 1
                # revenue = (price * quantity) * (1 - discount / 100)  # Recalculate revenue

                # Option 3: Decrease price and increase quantity
                # price *= 0.9  # Decrease price by 10%
                # quantity += 1
                # revenue = (price * quantity) * (1 - discount / 100)  # Recalculate revenue

                row["revenue"] = str(revenue)
                # row['quantity'] = str(quantity)  # Uncomment if you modify quantity
                # row['product_price'] = str(price)  # Uncomment if you modify price

            # (Optional) Slightly decrease revenue for other discount levels
            # elif discount < 20 or discount > 30:
            #     revenue *= 0.9  # Decrease by 10%
            #     row['revenue'] = str(revenue)

            writer.writerow(row)


if __name__ == "__main__":
    input_csv = "ecommerce_data.csv"  # Replace with your input CSV filename
    output_csv = "modified_output.csv"  # Replace with your desired output filename
    modify_csv(input_csv, output_csv)
