from skyfield.api import Topos, load, utc
from skyfield.sgp4lib import EarthSatellite
from datetime import timedelta
# Load the TLE files
tle1_file = 'tle1.txt'
tle2_file = 'tle2.txt'

tle1_lines = open(tle1_file).readlines()
tle2_lines = open(tle2_file).readlines()

# Extract the TLE data
line1_tle1 = tle1_lines[0].strip()
line2_tle1 = tle1_lines[1].strip()

line1_tle2 = tle2_lines[0].strip()
line2_tle2 = tle2_lines[1].strip()

# Create satellite objects
satellite1 = EarthSatellite(line1_tle1, line2_tle1, ts=load.timescale())
satellite2 = EarthSatellite(line1_tle2, line2_tle2, ts=load.timescale())

# Define the time range for close approach detection
timescale = load.timescale()
start_time = timescale.now()
end_time = start_time.utc_datetime() + timedelta(hours=48)

# Generate a time range for calculations
step_size = 60  # Step size in seconds
times = []
current_time = start_time
while current_time < end_time:
    times.append(timescale.utc(current_time))
    current_time += timedelta(seconds=step_size)

# Calculate positions for the time range
positions1 = satellite1.at(times).position.km
positions2 = satellite2.at(times).position.km

# Check for close approaches
for i, time in enumerate(times):
    distance = positions1[i] - positions2[i]
    if distance.magnitude() < 1000:  # Close approach threshold in kilometers
        print(f"Close approach detected at {time.utc_strftime('%Y-%m-%d %H:%M:%S')}")