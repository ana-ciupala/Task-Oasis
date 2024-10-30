import numpy as np
from numpy import random
from scipy.stats import poisson
from scipy.stats import lognorm
import sys

num_samples = 10000  # Number of simulation years

if len(sys.argv) != 7:
    print("Not suitable input")
    sys.exit(1)
else:
    # Read each argument from the comand line
    florida_landfall_rate = float(sys.argv[1])
    florida_mean = float(sys.argv[2])
    florida_stddev = float(sys.argv[3])
    gulf_landfall_rate =  float(sys.argv[4])
    gulf_mean =  float(sys.argv[5])
    gulf_stddev =  float(sys.argv[6])


#find the number of hurricanes in a year by taking a random number from the exponential distribution
def florida_rate(florida_landfall_rate):
    num_florida_events = poisson.rvs(florida_landfall_rate)
    return num_florida_events


# To set the scale (exp(mu)), we use np.exp(florida_mean)
#scale represents the median loss
florida_scale = np.exp(florida_mean)

#this function is returning the losses in a year for the hurricanes in Florida
#s = standard deviation
def florida_loss(s, scale):
    #find the number of events from the florida_rate function
    num = florida_rate(florida_landfall_rate)
    
    #generate the expected loss for each of the events
    losses = lognorm.rvs(s, scale, num)
    
    #find the total loss per year by summing the losses up
    yearly_losses = np.sum(losses)
    
    return yearly_losses


def gulf_rate(gulf_landfall_rate):
    num_gulf_events = poisson.rvs(gulf_landfall_rate)
    
    return num_gulf_events


#we do the similar procedure for the gulf states:
#Note this could have been done by using the same functions as before, but with different parameters when calling them

# To set the scale (exp(mu)), we use np.exp(florida_mean)
#scale represents the median loss
gulf_scale = np.exp(gulf_mean)

def gulf_loss(s, scale):
    #find the number of events from the florida_rate function
    num= gulf_rate(gulf_landfall_rate)
    
    #generate the expected loss for each of the events
    losses = lognorm.rvs(s, scale, num)
    
    #find the total loss per year by summing them up
    yearly_losses = np.sum(losses)
    
    return yearly_losses


#this function returns the average loss
def calculate_hurricane_loss(florida_rate, florida_mean, florida_stddev, 
                             gulf_rate, gulf_mean, gulf_stddev, 
                             nr):
    total_loss = 0

    for _ in range(nr):
        yearly_loss = 0
        
        # Florida losses
        #num_florida_events = poisson.rvs(florida_rate)
        
        florida_losses = florida_loss(florida_stddev, florida_scale)
        yearly_loss += florida_losses

        # Gulf losses
        #num_gulf_events = poisson.rvs(gulf_rate)
        gulf_losses = gulf_loss(gulf_stddev, gulf_scale)
        yearly_loss += np.sum(gulf_losses)
        
        #print(yearly_loss)
        
        total_loss += yearly_loss

    mean_loss = total_loss /nr
    
    return mean_loss  #value in billions

print(calculate_hurricane_loss(florida_landfall_rate, florida_mean, florida_stddev, gulf_landfall_rate, gulf_mean, gulf_stddev, num_samples))


