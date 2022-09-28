# Implentation of black-sholes option pricing model using python

import numpy as np
from scipy.stats import norm

#variable definition and input
r = float(input("Enter interst rate [format 0.XX]: "))
S = int(input("Enter underlying value: "))
K = int(input("Enter strike price: "))
T = int(input("Enter time in days: "))/365
sigma = float(input("Enter volatility/sigma [format 0.XX]: "))
type = input("Enter type; C for call, P for put: ")

#re-useable BlackSholes funtion
def BlackSholes(r, S, K, T, sigma, type):
    "Calculate black Sholes option price for a call or put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "C":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0 ,1)
        elif type == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1,0 , 1)
        return price
    except:
        print("Please confirm all option paramaters - E01: Execption caught")

print("\nOption Price is: ", round(BlackSholes(r, S, K, T, sigma, type), 2))
