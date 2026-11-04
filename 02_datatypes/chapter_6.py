chai_type = " Ginger wala"
customer_name = "Priya"
print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"first word: {chai_description[:8]}")
print(f"last word: {chai_description[12:]}")
print(f"last word: {chai_description[::-1]}") # Reverse String

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded Label: {label_text}")
print(f"Encoded Label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")