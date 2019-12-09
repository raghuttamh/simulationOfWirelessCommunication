from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
# References : Scipy.org, buttord.html

#Activity : Application of sampling theorem and filtering put together 
#Expt 1 : Run the program as is; Observe the output 
#Expt 2 : Comment line 25 and uncomment line 26 ; Observe the output
#Expt 3 : Add noise by uncommenting the 2nd half of line 17; Do experiments 1 and 2 again; Observe the output
 
#Generate a signal made up of f1 Hz and f2 Hz, sampled at 1 kHz
f1_Hz = 150
f2_Hz = 300
fs_Hz = 1000 # Sampling frequency

t = np.linspace(0, 1, fs_Hz, False)  # 1 second
sig = np.sin(2*np.pi*f1_Hz*t)+ np.sin(2*np.pi*f2_Hz*t)+ 0.5 * np.random.randn(t.size)
#sig = np.sin(2*np.pi*f1_Hz*t)
#sig =np.sin(2*np.pi*f1_Hz*t)
#sig = 0.5 * np.random.randn(t.size)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t, sig)
ax1.set_title('Sum of sinusoids')
ax1.axis([0, 1, -2, 2])
b, a = signal.butter(5, 0.5)# 0.5 corresponds to fs_Hz/4 
#b, a = signal.butter(5, 0.99)# 0.99 corresponds to fs_Hz/2 
filtered = signal.filtfilt(b, a, sig)

ax2.plot(t, filtered)
ax2.set_title('After  filtering')
ax2.axis([0, 1, -2, 2])
ax2.set_xlabel('Time [seconds]')
plt.tight_layout()

plt.show()

