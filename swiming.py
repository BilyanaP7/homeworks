minutes = int(input())
seconds = int(input())
meters = float(input())
seconds_per_hm = int(input())

total_seconds = minutes * 60 + seconds
total_time = (meters / 100) * seconds_per_hm - (meters / 120) * 2.5

if  total_time <= total_seconds:
    print(f"Peter Mitsin won quota with time (total_seconds:.3f).")
else:
    waste_time = total_time - total_seconds
    print(f"No, Peter failed! He was {waste_time:.3f} second slower.")
    