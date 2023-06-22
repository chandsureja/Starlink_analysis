from skyfield.api import EarthSatellite, load
from scipy.optimize import differential_evolution
import datetime
import numpy as np
import matplotlib.pyplot as plt


plt.figure(dpi=100)



tle_lines = open('active_gp(21_06).txt').readlines()


def get_position(unix_t):
    
    
    t=load.timescale().utc(2023, 6, 21, 0, 30, unix_t)
    #print(t)
    #sat1 = EarthSatellite(line1_tle1, line2_tle1, ts=load.timescale())
    #sat2 = EarthSatellite(line1_tle2, line2_tle2, ts=load.timescale())
    position1 = sat1.at(t)
    position2 = sat2.at(t)
    return (position2 - position1).distance().km
# Extract the TLE data


# Create satellite objects

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
line0_tle1, line1_tle1, line2_tle1 = read_tle(tle_lines,1)


sat1 = EarthSatellite(line1_tle1, line2_tle1,line0_tle1,ts=load.timescale())
line0_tle2, line1_tle2, line2_tle2 = read_tle(tle_lines,2)

sat2 = EarthSatellite(line1_tle2, line2_tle2,line0_tle2, ts=load.timescale())
r_min, r_max = -5, 5
# define the bounds on the search
bounds = [[r_min, r_max], [r_min, r_max]]
# perform the differential evolution search
result = differential_evolution(objective_function, bounds,args=(criteria,))

#min_val, t = find_minimum(0,86400)
print(line1_tle2)
t=load.timescale().utc(2023, 6, 21, 0, 30, t)
#print(t.utc_strftime())
t1 = np.array([0])
pos= np.array([0])
'''for t in range(0,86000):
    t1 = np.append(t1, t)
    pos_temp=get_position(t)
    pos = np.append(pos, pos_temp)
'''

print(result)
plt.plot(t1,pos)
plt.show()
print(min_val)
if(min_val < 5):
    print(min_val,t)
    print(line0_tle2)
'''for i in range(len(tle_lines)+1):
    
    
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