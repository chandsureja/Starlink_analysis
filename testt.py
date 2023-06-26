from skyfield.api import EarthSatellite, load
from scipy.optimize import differential_evolution
from scipy import optimize
import datetime
import numpy as np
import matplotlib.pyplot as plt
tle_lines = open('active_gp(21_06).txt').readlines()
def read_tle(tle_lines,i):
    if (i==1):
        start_index = 0
    if(i>1):
        start_index = (i-1)*3  # as TLE as 3 lines including name
    else: 
        print("invalid argument")
    line0_tle = tle_lines[start_index].strip()
    line1_tle = tle_lines[start_index+1].strip()
    line2_tle = tle_lines[start_index+2].strip()
    return line0_tle, line1_tle, line2_tle


plt.figure(dpi=100)

line0_tle1, line1_tle1, line2_tle1 = read_tle(tle_lines,1)


sat1 = EarthSatellite(line1_tle1, line2_tle1,line0_tle1,ts=load.timescale())
line0_tle2, line1_tle2, line2_tle2 = read_tle(tle_lines,2)

sat2 = EarthSatellite(line1_tle2, line2_tle2,line0_tle2, ts=load.timescale())



position1 = []
position2 = []
dist= []
def get_position(unix_t):
    
    for time in unix_t:
        t=load.timescale().utc(2023, 6, 21, 0, 30, time)
    #print(t)
    #sat1 = EarthSatellite(line1_tle1, line2_tle1, ts=load.timescale())
    #sat2 = EarthSatellite(line1_tle2, line2_tle2, ts=load.timescale())
       
        position1.append(sat1.at(t))
        position2.append(sat2.at(t))
        dist_temp=(sat2.at(t) - sat1.at(t)).distance().km
        dist.append(dist_temp)
    return min(dist)

rand_int3 = np.random.randint(50,1000, size=10 ,dtype='int64')
test_res=get_position(rand_int3)

print(test_res)

# Extract the TLE data


# Create satellite objects


    


#t is in julian time 
ts = load.timescale()
def objective_function(timestamp):
        return get_position(timestamp)

def find_minimum(start_timestamp, end_timestamp):
    # Define the function to be minimized
    def objective_function(timestamp):
        return get_position(timestamp)

    # Perform minimization using scipy's minimize_scalar
    result = minimize_scalar(objective_function, bounds=(start_timestamp, end_timestamp), method='bounded')

    return result.fun, result.x

r_min, r_max = -5, 5
# define the bounds on the search
bounds = [[r_min, r_max], [r_min, r_max]]
# perform the differential evolution search
result = differential_evolution(get_position, bounds)

#min_val, t = find_minimum(0,86400)
print(result)
print(get_position(7496.12550951232))
#t=load.timescale().utc(2023, 6, 21, 0, 30, t)
#print(t.utc_strftime())
t1 = np.array([0])
pos= np.array([0])
'''for t in range(0,86000):
    t1 = np.append(t1, t)
    pos_temp=get_position(t)
    pos = np.append(pos, pos_temp)
'''
#print(optimize.rosen(rand_int3))

#print(result)
plt.plot(t1,pos)
plt.show()


'''print(min_val)
if(min_val < 5):
    print(min_val,t)
    print(line0_tle2)
for i in range(len(tle_lines)+1):
    
    
    line0_tle2, line1_tle2, line2_tle2 = read_tle(tle_lines,i+1)
    sat2 = EarthSatellite(line1_tle2, line2_tle2,line0_tle2, ts=load.timescale())


    min_val, t = find_minimum(0,86400)

    t=load.timescale().utc(2023, 6, 22, 0, 30, t)
    #print(t.utc_strftime())
    if(min_val < 5):
        print(min_val,t)
        print(line0_tle2)
'''


t = ts.utc(2020, 8, 25, 5, range(3440) )  #epoch + a full orbit
geocentric = sat1.at(t)
print(geocentric)
subpoint = geocentric.subpoint()
print(f"max {max(geocentric.distance().km)}")
print(f"min {min(geocentric.distance().km)}")