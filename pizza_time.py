p1 = int(input("Slices for Person 1: "))
p2 = int(input("Slices for Person 2: "))
p3 = int(input("Slices for Person 3: "))
p4 = int(input("Slices for Person 4: "))

total_slices = p1 + p2 + p3 + p4
pizzas_needed = total_slices // 8
if total_slices % 8 != 0:
    pizzas_needed += 1

leftover_slices = (8 - (total_slices % 8)) % 8

print("\nOrder")
print(f"Total slices wanted: {total_slices}")
print(f"Whole pizzas to order: {pizzas_needed}")
print(f"Slices left over after eating: {leftover_slices}")
