import matplotlib.pyplot as plt
import numpy as np

################ fft ################
def plot_a(gesture):
  path1 = f"data/{gesture}_18.csv"
  path2 = f"data/{gesture}_19.csv"
  a1 = np.genfromtxt(path1, delimiter=",", skip_header=1, usecols=(0,1,2)).T
  a2 = np.genfromtxt(path2, delimiter=",", skip_header=1, usecols=(0,1,2)).T
  
  sr = 100 # sampling rate
  interval = 1.0/sr # sampling interval
  n = 400 # number of samples taken
  dt = np.arange(0, n*interval, interval) # time domain

  fig = plt.figure(figsize=(8, 6))

  sp1 = fig.add_subplot(2, 1, 1)
  sp1.set_title(f"{gesture}_18 Acceleration")
  sp1.set_xlabel("Time (s)")
  sp1.set_ylabel("Magnitude")
  sp1.plot(dt, a1[0])
  sp1.plot(dt, a1[1])
  sp1.plot(dt, a1[2])

  sp2 = fig.add_subplot(2, 1, 2)
  sp2.set_title(f"{gesture}_19 Acceleration")
  sp2.set_xlabel("Time (s)")
  sp2.set_ylabel("Magnitude")
  sp2.plot(dt, a2[0])
  sp2.plot(dt, a2[1])
  sp2.plot(dt, a2[2])

  fig.tight_layout()
  plt.show()


def plot_b(gesture):
  path1 = f"data/{gesture}_18.csv"
  path2 = f"data/{gesture}_19.csv"
  g1 = np.genfromtxt(path1, delimiter=",", skip_header=1, usecols=(3,4,5)).T
  g2 = np.genfromtxt(path2, delimiter=",", skip_header=1, usecols=(3,4,5)).T
  
  sr = 100 # sampling rate
  interval = 1.0/sr # sampling interval
  n = 400 # number of samples taken
  dt = np.arange(0, n*interval, interval) # time domain

  fig = plt.figure(figsize=(8, 6))

  sp1 = fig.add_subplot(2, 1, 1)
  sp1.set_title(f"{gesture}_18 Gyroscope")
  sp1.set_xlabel("Time (s)")
  sp1.set_ylabel("Magnitude")
  sp1.plot(dt, g1[0])
  sp1.plot(dt, g1[1])
  sp1.plot(dt, g1[2])

  sp2 = fig.add_subplot(2, 1, 2)
  sp2.set_title(f"{gesture}_19 Gyroscope")
  sp2.set_xlabel("Time (s)")
  sp2.set_ylabel("Magnitude")
  sp2.plot(dt, g2[0])
  sp2.plot(dt, g2[1])
  sp2.plot(dt, g2[2])

  fig.tight_layout()
  plt.show()

def plot_c(gesture):
  path1 = f"data/{gesture}_18.csv"
  path2 = f"data/{gesture}_19.csv"
  a1 = np.genfromtxt(path1, delimiter=",", skip_header=1, usecols=(0,1,2))
  a2 = np.genfromtxt(path2, delimiter=",", skip_header=1, usecols=(0,1,2))
  a1 = np.array([np.linalg.norm(vec) for vec in a1])
  a2 = np.array([np.linalg.norm(vec) for vec in a2])

  sr = 100 # sampling rate
  interval = 1.0/sr # sampling interval
  n = 400 # number of samples taken
  dt = np.arange(0, n*interval, interval) # time domain

  # plot specgram
  fig = plt.figure(figsize=(8, 6))
  sp1 = fig.add_subplot(2, 1, 1)
  sp1.set_title(f"{gesture}_18 Acceleration")
  sp1.set_xlabel("Time (s)")
  sp1.set_ylabel("Frequency (Hz)")
  s_acc1, f_acc1, t_acc1, im_acc1 = sp1.specgram(a1, Fs=sr, NFFT=32, noverlap=16, cmap="rainbow")
  fig.colorbar(im_acc1, label="Power (dB)")
  sp2 = fig.add_subplot(2, 1, 2)
  sp2.set_title(f"{gesture}_19 Acceleration")
  sp2.set_xlabel("Time (s)")
  sp2.set_ylabel("Frequency (Hz)")
  s_acc2, f_acc2, t_acc2, im_acc2 = sp2.specgram(a2, Fs=sr, NFFT=32, noverlap=16, cmap="rainbow")
  fig.colorbar(im_acc2, label="Power (dB)")
  fig.tight_layout()
  plt.show()


def plot_d(gesture):
  path1 = f"data/{gesture}_18.csv"
  path2 = f"data/{gesture}_19.csv"
  g1 = np.genfromtxt(path1, delimiter=",", skip_header=1, usecols=(3,4,5))
  g2 = np.genfromtxt(path2, delimiter=",", skip_header=1, usecols=(3,4,5))
  g1 = np.array([np.linalg.norm(vec) for vec in g1])
  g2 = np.array([np.linalg.norm(vec) for vec in g2])

  sr = 100 # sampling rate
  interval = 1.0/sr # sampling interval
  n = 400 # number of samples taken
  dt = np.arange(0, n*interval, interval) # time domain

  # plot specgram
  fig = plt.figure(figsize=(8, 6))
  sp1 = fig.add_subplot(2, 1, 1)
  sp1.set_title(f"{gesture}_18 Gyroscope")
  sp1.set_xlabel("Time (s)")
  sp1.set_ylabel("Frequency (Hz)")
  s_acc1, f_acc1, t_acc1, im_acc1 = sp1.specgram(g1, Fs=sr, NFFT=32, noverlap=16, cmap="rainbow")
  fig.colorbar(im_acc1, label="Power (dB)")
  sp2 = fig.add_subplot(2, 1, 2)
  sp2.set_title(f"{gesture}_19 Gyroscope")
  sp2.set_xlabel("Time (s)")
  sp2.set_ylabel("Frequency (Hz)")
  s_acc2, f_acc2, t_acc2, im_acc2 = sp2.specgram(g2, Fs=sr, NFFT=32, noverlap=16, cmap="rainbow")
  fig.colorbar(im_acc2, label="Power (dB)")
  fig.tight_layout()
  plt.show()

def plot_all(gesture):
  plot_a(gesture)
  plot_b(gesture)
  plot_c(gesture)
  plot_d(gesture)

################ main ################

plot_all('up')
plot_all('down')
plot_all('left')
plot_all('right')