from skyfield.api import EarthSatellite, load
from scipy.optimize import minimize_scalar
import datetime



tle_lines = open('starlink_tle.txt').readlines()



# Extract the TLE data
line1_tle1 = tle1_lines[0].strip()
line2_tle1 = tle1_lines[1].strip()

line1_tle2 = tle2_lines[0].strip()
line2_tle2 = tle2_lines[1].strip()

# Create satellite objects

def read_tle(tle_lines,i):
    
    


#t is in julian time 
ts = load.timescale()

def find_minimum(start_timestamp, end_timestamp):
    # Define the function to be minimized
    def objective_function(timestamp):
        return get_position(timestamp)

    # Perform minimization using scipy's minimize_scalar
    result = minimize_scalar(objective_function, bounds=(start_timestamp, end_timestamp), method='bounded')

    return result.fun, result.x
sat1 = EarthSatellite(line1_tle1, line2_tle1,line0_tle1,ts=load.timescale())
sat2 = EarthSatellite(line1_tle2, line2_tle2,line0_tle1, ts=load.timescale())

def get_position(unix_t):
    
    t=load.timescale().utc(2023, 5, 25, 5, 30, unix_t)
    #print(t)
    #sat1 = EarthSatellite(line1_tle1, line2_tle1, ts=load.timescale())
    #sat2 = EarthSatellite(line1_tle2, line2_tle2, ts=load.timescale())
    position1 = sat1.at(t)
    position2 = sat2.at(t)
    return (position2 - position1).distance().km

min_val, t = find_minimum(0,86400)

t=load.timescale().utc(2023, 5, 25, 5, 30, t)
print(t.utc_strftime())

print(min_val,t)



t = ts.utc(2020, 8, 25, 5, range(3440) )  #epoch + a full orbit
geocentric = sat1.at(t)
print(geocentric)
subpoint = geocentric.subpoint()
print(f"max {max(geocentric.distance().km)}")
print(f"min {min(geocentric.distance().km)}")