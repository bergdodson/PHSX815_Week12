# Importing Packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn 
import sys


if __name__ == "__main__":
    # System initialization stuff
    p = 0.1
    ntrials = 100000
    size = 100000
    
    if '-p' in sys.argv:
	    q = sys.argv.index('-p')
	    p = float(sys.argv[q+1])
    if '-n' in sys.argv:
	    q = sys.argv.index('-n')
	    ntrials = int(sys.argv[q+1])
    if '-size' in sys.argv:
    	q = sys.argv.index('-size')
    	size = int(sys.argv[q+1])
    np.random.seed(3548)

	# Getting samples
    samples = np.random.binomial(ntrials, p, size)

	#Plotting the resutls    
    seaborn.histplot(samples, kde=True, stat = 'probability',color = 'pink', alpha = .5)
    plt.title("KDE on Binomial distribution: p={}, ntrial={}, size={}".format(p,ntrials, size))
    plt.savefig('DensityEstimation3.png')
    plt.show()
    