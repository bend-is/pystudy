input_secs = int(input("Enter some number of second: "))

h = input_secs // 3600
m = (input_secs % 3600) // 60
s = input_secs % 60

print(f"{h:02d}:{m:02d}:{s:02d}")
