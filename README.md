# Task-Oasis
Please find here my code for the task.

Running instructions:
- download the file
- run the file from the control comand:
    - arrive in the directory where the file is saved
    - run it by using python Task-Oasis.py arg1 arg2 arg3 arg4 arg5 arg6
    - all the arguments are parameters of the distributions that evaluate the loss of the hurricans in Florida and Gulf states
    - arg1 = florida_landfall_rate -> annual rate of hurricanes in Florida simulated by an exponential distribution
    - arg2 = florida_mean
    - arg3 = florida_stddev ->these are parameters for the LogNormal distribution which simulated the economic loss
    - arg4 = annual rate of hurricanes in the Gulf states simulated by an exponential distribution
    - arg2 = gulf_mean
    - arg3 = gulf_stddev ->these are parameters for the LogNormal distribution which simulated the economic loss

The program returns the average loss in Billions of dollars. The number of simulations is set to 10000 in the variable 
