import sys
import math
print("\nProgram to demonstrate concept of command line arguments.")
if(len(sys.argv)!=2):
	print("\n Invalid argument passed, try again.")
else:
	n=int(sys.argv[1])
	print("\nFactorial of {} is {}".format(n,math.factorial(n)))
