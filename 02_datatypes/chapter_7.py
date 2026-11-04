masala_spices = ("cardamom","cloves","cinnamon")
(spice1,spice2,spice3) = masala_spices
print(f"Main masala spices : {spice1},{spice2},{spice3}")

ginger_ration, cardramom_ration = 2,1
print(f"Ratio is G : {ginger_ration} and C : {cardramom_ration}")
ginger_ration, cardramom_ration = cardramom_ration, ginger_ration
print(f"Ratio is G : {ginger_ration} and C : {cardramom_ration}")

# Membership testing

print(f"Is cinnamon in masala spices ? {'cinnamon'in masala_spices}")