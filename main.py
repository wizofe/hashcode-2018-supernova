import numpy as np
import sys

def read_file(fname):
    data = np.loadtxt(fname)
    rows, cols, fleet, n_rides, bonus, periods  = [int(n) for n in data[0, :]]

    rides = data[1:, :]
   # grid = np.zeros((rows, cols))

    return(rides, rows, cols, fleet, n_rides, bonus, periods)

def write_file(fname, data):
    np.savetxt(fname, data, fmt='%i')

def main():

    if len(sys.argv) < 3:
        sys.exit('Error! Syntax: {} <infile> <outfile>'.format(sys.argv[0]))

    rides, rows, cols, fleet, n_rides, bonus, periods = read_file(sys.argv[1])

    dummy = n_rides // fleet
    all_rides = [i for i in range(n_rides)]
    rides_taken  = dummy * fleet

    c_list = [all_rides[x:x+dummy] for x in range(0, rides_taken, dummy)]

    output = []
    for i in range(fleet):
        data = [dummy, *c_list[i]]
        output.append(data)
    write_file(sys.argv[2], output)

if __name__ == '__main__':
    main()
