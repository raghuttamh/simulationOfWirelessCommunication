import numpy as np
import matplotlib.pyplot as plt
from math import erfc
import os
# References : Scipy cookbook, Commtheory

#SNRdb = [3,6,9,12] # signal to noise-ratio in dB at the receiver

# F = 1.8C + 32; If C = 37, F = 98.6 --> Approach 1 --> erfc --> Analytical
# Relation between F and C not known, measure using 2 thermometers and see --> Simulation --> Empirical

#Verify empirical stuff using simulation -- crucial pointbhere

 # Expt 1 : Run code as is and observe the final plot.Verify with standard #plots : BER performance of BPSK in AWGN channel
#Expt 2 : Code Walk Through 
 #   1) Tx : Line 37,38
 #   2) Noise Addition : Line 46
 #   3) Receiver : Line 42 to 46
 #   4) Performance
 # One loop of 14 values of SNR, for 1e6 bits
 
#Expt 2 : Sum up and motivate the differences between AWGN channel and Multipath/Rayleigh channel for next session on OFDM  
 
 

os.system('clear')
loop = 0

Pe = [0,0,0,0,0,0,0,0,0,0,0,0,0]
ber_sim = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SNRdb = [-2,-1,0,1,2,3,4,5,6,7,8,9,10]
No_of_bits = 100000000 # 1e8



for iter in range(1,14,1):
#for SNRdb in range(-2,2,1):
    SNR = 10**(SNRdb[loop]/10.0)  # linear SNR
    Pe[loop] = 0.5*erfc(np.sqrt(SNR))
    #print(Pe[loop])
    No = 1/SNR
    #print(No)
    tx_sig = np.random.binomial(n=1, p=0.5, size=No_of_bits)
    
    tx_sig = 2*tx_sig-1
    #print(tx_sig)
    noise = np.sqrt(No/2)*np.random.randn(No_of_bits)
    #print(noise)
    rx_sig =  tx_sig + noise
    #rx_sig =  conv(tx_sig, multi_path_channel) + noise
    #print(rx_sig)
    decision = np.sign(rx_sig)
    #print(decision)
    err = decision - tx_sig
    ber_sim[loop] = np.count_nonzero(err)/No_of_bits
    print ('Eb_No_dB=%4.2f, BER_SIM=%10.4e, Pe(BER_CALC)=%10.4e' % \
        (SNRdb[loop], ber_sim[loop], Pe[loop]))    
    loop +=1
plt.semilogy(SNRdb, Pe,'r',linewidth=2)
plt.semilogy(SNRdb, ber_sim,'-s')
plt.grid(True)
plt.legend(('analytical','simulation'))
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.show()
