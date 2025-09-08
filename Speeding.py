average_speed = float(input("What is your average speed (mph): "))
speed_limit = float(input("What is the speed limit (mph): "))
distance = float(input("How many miles did you travel (miles): "))

speed_lim_time = distance / speed_limit   
avg_speed_time = distance / average_speed   

saved_time = (speed_lim_time - avg_speed_time) * 60

if saved_time > 0:
    print(f"\nYou are an unsafe driver and you saved: {saved_time:.0f} minutes")
elif saved_time == 0:
    print("\nYou are a good driver but you didn't save any time")
    