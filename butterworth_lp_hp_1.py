from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
# References : scipy.org, buttord.html

#btype : {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}, optional
#Band pass

#Expt 1 : Run, as is. Observe output. Repeat by changing minus_3dB_point to 400 and 500.  

# Low pass configuration
#minus_3dB_point = 500 # cutoff frequency
#typ_of_filter = 'lowpass'

#Expt 2 : Comment lines 12 and 13 and uncomment lines 18 and 19. Observe output. Repeat by changing minus_3dB_point to 800 and 900.  


# High pass configuration
minus_3dB_point = 100 # cutoff frequency
typ_of_filter = 'highpass'


b, a = signal.butter(4, minus_3dB_point, typ_of_filter, analog=True)
w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(minus_3dB_point, color='green') # cutoff frequency
plt.show()


