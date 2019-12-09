import numpy as np
import scipy.fftpack
from matplotlib import pyplot as plt

#References : Scipy.org

#Expt 1 : Run, as is. Analyse time domain plot. Analyse freq. domain plot
#Expt 2 : Comment line 26 and uncomment line 28. Repeat expt 1.
#Activity 3 : IFFT is a transformer, that which ensures orthogonality among sub-carrers  and creates the OFDM waveform. (Non-orthogonal to orthogonal transformer)
time_step = 0.5

w0=0.2*np.pi
w1=0.4*np.pi
w2=0.6*np.pi
w3=0.8*np.pi

time_vec = np.arange(0, 80, time_step)
print(time_vec.size) # Totally 160 samples
#sig = (np.sin(2 * np.pi / period * time_vec)
 #      + 0.5 * np.random.randn(time_vec.size))
sig1 = np.sin(w0*time_vec)
sig2 = np.sin(w1*time_vec)
sig3 = np.sin(w2*time_vec)
sig4 = np.sin(w3*time_vec)

#sum_sgl =  sig1+sig2+sig3+sig4
#sum_sgl =  sig1 
sum_sgl =  sig1+sig2+sig3+sig4+np.random.randn(time_vec.size)
#sum_sgl =  np.random.randn(time_vec.size)

plt.figure(figsize=(6, 5))
plt.plot(time_vec, sum_sgl, label='Summed Sine wave')

plt.show()

fft_sum_sgl = scipy.fftpack.fft(sum_sgl)
fft_sum_sgl_abs = np.abs(fft_sum_sgl)

plt.figure(figsize=(6, 5))
plt.plot(time_vec, fft_sum_sgl_abs, label='FFT of Summed Sine wave')
plt.show()
