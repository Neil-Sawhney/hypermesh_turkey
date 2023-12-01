# return the first timestep where every value is above 160 F or 344.26 K. If no such timestep exists, return -1
def cook_time(r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12, r_13, r_14, r_15, r_16, r_17, r_18, r_19, r_20, r_21, r_22, r_23, r_24, r_25, r_26, r_27, r_28, r_29, r_30, r_31, r_32, r_33, r_34, r_35, r_36, r_37, r_38, r_39, r_40, r_41, r_42, r_43, r_44, r_45, r_46):
    # find the first timestep where min_ds is above 160 F or 344.26 K
    if r_1 > 344.26:
        return 1
    elif r_2 > 344.26:
        return 2
    elif r_3 > 344.26:
        return 3
    elif r_4 > 344.26:
        return 4
    elif r_4 > 344.26:
        return 4
    elif r_5 > 344.26:
        return 5
    elif r_6 > 344.26:
        return 6
    elif r_7 > 344.26:
        return 7
    elif r_8 > 344.26:
        return 8
    elif r_9 > 344.26:
        return 9
    elif r_10 > 344.26:
        return 10
    elif r_11 > 344.26:
        return 11
    elif r_12 > 344.26:
        return 12
    elif r_13 > 344.26:
        return 13
    elif r_14 > 344.26:
        return 14
    elif r_15 > 344.26:
        return 15
    elif r_16 > 344.26:
        return 16
    elif r_17 > 344.26:
        return 17
    elif r_18 > 344.26:
        return 18
    elif r_19 > 344.26:
        return 19
    elif r_20 > 344.26:
        return 20
    elif r_21 > 344.26:
        return 21
    elif r_22 > 344.26:
        return 22
    elif r_23 > 344.26:
        return 23
    elif r_24 > 344.26:
        return 24
    elif r_25 > 344.26:
        return 25
    elif r_26 > 344.26:
        return 26
    elif r_27 > 344.26:
        return 27
    elif r_28 > 344.26:
        return 28
    elif r_29 > 344.26:
        return 29
    elif r_30 > 344.26:
        return 30
    elif r_31 > 344.26:
        return 31
    elif r_32 > 344.26:
        return 32
    elif r_33 > 344.26:
        return 33
    elif r_34 > 344.26:
        return 34
    elif r_35 > 344.26:
        return 35
    elif r_36 > 344.26:
        return 36
    elif r_37 > 344.26:
        return 37
    elif r_38 > 344.26:
        return 38
    elif r_39 > 344.26:
        return 39
    elif r_40 > 344.26:
        return 40
    elif r_41 > 344.26:
        return 41
    elif r_42 > 344.26:
        return 42
    elif r_43 > 344.26:
        return 43
    elif r_44 > 344.26:
        return 44
    elif r_45 > 344.26:
        return 45
    elif r_46 > 344.26:
        return 46
    else:
        return -1

#at time timestep t, count how many nodes are above 280 F, or 410.93 K and calculate the percentage, if timestep t is -1, return the percentage at the last timestep
def percent_burned(ds):
    # count how many nodes are above 280 F, or 410.93 K
    count = 0
    for i in range(len(ds)):
        if ds[i] > 410.93:
            count += 1

    # count how many nodes are zero
    count_zero = 0
    for i in range(len(ds)):
        if ds[i] == 0:
            count_zero += 1

    # calculate the percentage
    if count_zero == len(ds):
        return 0
    else:
        return (count / (len(ds) - count_zero)) * 100


def pick_from_t(s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_11, s_12, s_13, s_14, s_15, s_16, s_17, s_18, s_19, s_20, s_21, s_22, s_23, s_24, s_25, s_26, s_27, s_28, s_29, s_30, s_31, s_32, s_33, s_34, s_35, s_36, s_37, s_38, s_39, s_40, s_41, s_42, s_43, s_44, s_45, s_46, t):
    if t == 1:
        return s_1
    elif t == 2:
        return s_2
    elif t == 3:
        return s_3
    elif t == 4:
        return s_4
    elif t == 5:
        return s_5
    elif t == 6:
        return s_6
    elif t == 7:
        return s_7
    elif t == 8:
        return s_8
    elif t == 9:
        return s_9
    elif t == 10:
        return s_10
    elif t == 11:
        return s_11
    elif t == 12:
        return s_12
    elif t == 13:
        return s_13
    elif t == 14:
        return s_14
    elif t == 15:
        return s_15
    elif t == 16:
        return s_16
    elif t == 17:
        return s_17
    elif t == 18:
        return s_18
    elif t == 19:
        return s_19
    elif t == 20:
        return s_20
    elif t == 21:
        return s_21
    elif t == 22:
        return s_22
    elif t == 23:
        return s_23
    elif t == 24:
        return s_24
    elif t == 25:
        return s_25
    elif t == 26:
        return s_26
    elif t == 27:
        return s_27
    elif t == 28:
        return s_28
    elif t == 29:
        return s_29
    elif t == 30:
        return s_30
    elif t == 31:
        return s_31
    elif t == 32:
        return s_32
    elif t == 33:
        return s_33
    elif t == 34:
        return s_34
    elif t == 35:
        return s_35
    elif t == 36:
        return s_36
    elif t == 37:
        return s_37
    elif t == 38:
        return s_38
    elif t == 39:
        return s_39
    elif t == 40:
        return s_40
    elif t == 41:
        return s_41
    elif t == 42:
        return s_42
    elif t == 43:
        return s_43
    elif t == 44:
        return s_44
    elif t == 45:
        return s_45
    return s_46