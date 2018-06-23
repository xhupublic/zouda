2.26
"""
pseudo code:
(1) if t is in first range => use first equation
(2) if t is in second range => use secnd equation 
(3) if t is in third range => use third equation
(4) return error return  
"""

def height(t):
    if 0 <= t and t < 15:
        y = 38.1454 * t +  0.13743 * t ** 3 
    elif 15 <= t and t < 33:
        y = 1036 + 130.909 * (t - 15) + 6.18425 * (t - 15) ** 2 - 0.428 * (t - 15) ** 3
    elif t > 33:
        y = 2900 - 62.468 * (t - 33) - 16.9274 * (t - 33) ** 2  + 0.41796 * (t - 33) ** 3
    else:
        return 0
    return y if y >= 0 else 0

x = range(-10, 50)
y = [height(t) for t in x]
print(y)

"""
output:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 38.282830000000004, 77.39024, 118.14681000000002, 161.37712000000002, 207.90575, 258.55728000000005, 314.15629, 375.52736000000004, 443.49507, 518.884, 602.51873, 695.2238400000001, 797.8239100000001, 911.1435200000001, 1036.0, 1172.66525, 1319.131, 1472.8292499999998, 1631.192, 1791.6512500000001, 1951.639, 2108.5872499999996, 2259.928, 2403.09325, 2535.5150000000003, 2654.6252499999996, 2757.8559999999998, 2842.63925, 2906.4069999999992, 2946.5912499999995, 2960.624, 2945.93725, 0, 2821.0225600000003, 2710.6980799999997, 2571.53432, 2406.03904, 2216.72, 2006.0849600000001, 1776.6416800000002, 1530.8979199999999, 1271.3614400000001, 1000.54, 720.9413599999998, 435.07328000000007, 145.44352000000026, 0, 0, 0]
the rocket will hit ground after 46 - 47 second
"""
