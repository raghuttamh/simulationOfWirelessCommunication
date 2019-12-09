from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# References : Scipy.org, buttord.html

#An analog bandpass filter with passband within 3 dB from 20 to 50 rad/s, while rejecting at least -40 dB below 14 and above 60 rad/s.

# Expt1 : Run the program as is and observe the output

# Expt2 : Comment line 15 and uncomment line 16, to visualise bandstop filter

N, Wn = signal.buttord([20, 50], [14, 60], 3, 40, True)
#b, a = signal.butter(N, Wn, 'band', True) # Bandpass cfg
b, a = signal.butter(N, Wn, 'stop', True) # Bandstop cfg
w, h = signal.freqs(b, a, np.logspace(1, 2, 500))
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth bandpass filter')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.fill([1,  14,  14,   1], [-40, -40, 99, 99], '0.9', lw=0) # stop
plt.fill([20, 20,  50,  50], [-99, -3, -3, -99], '0.9', lw=0) # pass
plt.fill([60, 60, 1e9, 1e9], [99, -40, -40, 99], '0.9', lw=0) # stop
plt.axis([10, 100, -60, 3])
plt.show()
