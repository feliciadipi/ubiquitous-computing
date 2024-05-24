import matplotlib.pyplot as plt
import numpy as np

################################################################################
                          # SET SRC PATH HERE #
file_path = "./data/up.csv"
################################################################################

a = np.genfromtxt(file_path, delimiter=",", skip_header=1, usecols=(0,1,2)).T
g = np.genfromtxt(file_path, delimiter=",", skip_header=1, usecols=(3,4,5)).T

sr = 1000 # sampling rate
interval = 1.0/sr # sampling interval
n = len(a[0]) # number of samples taken
t_domain = np.arange(0, n*interval, interval) # time domain
f_domain = np.linspace(0, sr, n) # frequency domain

#fft_a = []
#for axis in a:
#  fft_a.append(np.abs(np.fft.fft(axis)))
#
#fft_g = []
#for axis in g:
#  fft_g.append(np.abs(np.fft.fft(axis)))

################################################################################
                            # PLOT FFT HERE #
# X = t_domain
# Y = fft_g
# x_label = ""
# y_label = ""


# plt.plot(X, Y[0], label="x")
# plt.plot(X, Y[1], label="y")
# plt.plot(X, Y[2], label="z")
# plt.xlim(0, 10)
# plt.xlabel(x_label)
# plt.ylabel(y_label)
# plt.legend()
# plt.show()
  
################################################################################
                          # PLOT SPECTROGRAM HERE #

plt.specgram(g[0], Fs=sr, noverlap=8, NFFT=16)
plt.show()