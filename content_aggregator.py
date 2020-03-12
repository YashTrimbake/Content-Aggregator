import time
from Categories import main

def get_part_details(part_name, part_cat):
    part_name = part_name.strip().lower()
    start_time = time.time()
    part_list = main.get_part_list(part_name, part_cat)
    if(part_list == []):
        print(f"No part named '{part_name}' was found!")
    for part in part_list:
        print("\n")
        print(part)
    print("\n")
    print("Time Taken", time.time()-start_time)
    return part_list
