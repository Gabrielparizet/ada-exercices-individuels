def create_phone_number(n):
    return "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5]) + "-" + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])


sample_arr = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]

create_phone_number(sample_arr)