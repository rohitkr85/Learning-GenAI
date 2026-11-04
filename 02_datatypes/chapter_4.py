is_boiling = True
stir_count = 5
total_action = stir_count + is_boiling # Upcasting
print(f"Total Action : {total_action}")

is_milk_present =0 # no milk
print(f"Is there milk ? {bool(is_milk_present)}")
is_milk_present = 1 # Yes milk
if is_milk_present:
    is_milk_present = "yes"
    print(f"Is there milk rohit ? {is_milk_present}")
print(f"Is there milk ? {bool(is_milk_present)}")


hot_water = True
team_added = False

can_serve = hot_water and team_added

print(f"Can serve chai ? {can_serve}")