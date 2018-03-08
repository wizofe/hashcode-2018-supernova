# Copyright (c) 2018 Team Supernova
# Licensed under the GNU GPL v3.0

# Later additions by M. Loening @mloning
# Achieving double score!

import numpy as np
import sys

def read_file(file):
    data = np.loadtxt(file, dtype=int)
    rows, cols, n_vehicles, n_rides, bonus, n_periods  = [int(i) for i in data[0,:]]
    
    rides_data = data[1:,:]
    rides_id = np.array([i for i in range(rides_data.shape[0])])
    rides = np.c_[rides_id, rides_data]
    return rides, rows, cols, n_vehicles, n_rides, bonus, n_periods

def write_file(file, data):
    np.savetxt(file, data, fmt='%i')
    
def assign_rides(rides, n_vehicles):
    n_rides = rides.shape[0]

    rides_per_vehicle = int(n_rides / n_vehicles) 
    rides_taken = int(rides_per_vehicle * n_vehicles)

    output_list = []
    for i in range(0, rides_taken, rides_per_vehicle):
        assigned_rides = rides[i:i+rides_per_vehicle]
        sorted_rides = assigned_rides[assigned_rides[:,5].argsort()]
        rides_id = sorted_rides[:,0]

        output = [rides_per_vehicle, *rides_id]
        output_list.append(output)
    
    return output_list

def main():
    if len(sys.argv) < 3:
        sys.exit('Error! Syntax: {} <infile> <outfile>'.format(sys.argv[0]))

    rides, rows, cols, n_vehicles, n_rides, bonus, periods = read_file(sys.argv[1])

    output = assign_rides(rides, n_vehicles)

    write_file(sys.argv[2], output)

if __name__ == '__main__':
    main()
