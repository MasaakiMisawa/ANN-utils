import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_ANN_RMSE():
## Number of Directory and Directory Name ##
  ndir = 9;   dirnam = [[]]*ndir; fep = [[]]*ndir
  for n in range(ndir): dirnam[n] = './DATA/data%d' %(n+1)
  
## Computational Condition ##    
  fep [0] = 145  # Final epoch of file 0
  fep [1] = 999  # Final epoch of file 1
  fep [2] = 999
  fep [3] = 3  
  fep [4] = 26 
  fep [5] = 288
  fep [6] = 18 
  fep [7] = 84 
  fep [8] = 2 
  
####################################################################################################

## Initiallization and Array ##  
  ep = np.array([]); cnt = 0
  re = np.array([]); rf = np.array([]); rp = np.array([])
  ret = np.array([]); rft = np.array([]); rpt = np.array([])
  
## Read Data ##
  for n in range(ndir):
    filnam = '%s/train.RMSE.dat' %(dirnam[n])
    fp = open(filnam, 'r')
    print('open: %s' %(filnam))
    while True:
      dat = fp.readline().split()   
      if dat == []: break
      if dat[0][0:1] == '#': continue
      if int(dat[0]) > fep[n]: break
      cnt += 1
      ep = np.append(ep, cnt)
      re = np.append(re, float(dat[1]))
      rf = np.append(rf, float(dat[3]))
      rp = np.append(rp, float(dat[5]))
      ret = np.append(ret, float(dat[7]))
      rft = np.append(rft, float(dat[9]))
      rpt = np.append(rpt, float(dat[11]))
    fp.close()
    
## Console Output ##  
  print('total number of data: %d' %(cnt))
  
## Plot Figure ##
  plt.subplot(3, 1, 1)
  plt.title('Evolution of RMSEs')
  plt.yscale('log')
  plt.ylim(0.001,0.5)
  plt.plot(ep, re, label = 'Train set')
  plt.plot(ep, ret, label = 'Test set', linestyle='dashed')
  plt.legend()
  plt.ylabel('RMSE \n(eV/atom)')
  plt.tick_params('x', length=0)
  plt.xticks(color='w')
  plt.subplot(3, 1, 2)
  plt.yscale('log')
  plt.ylim(0.1,50)
  plt.plot(ep, rf)
  plt.plot(ep, rft, linestyle='dashed')
  plt.ylabel('RMSE (eV/$\mathrm{\AA}$)')
  plt.tick_params('x', length=0)
  plt.xticks(color='w')
  plt.subplot(3, 1, 3)
  plt.yscale('log')
  plt.ylim(0.1,50)
  plt.plot(ep, rp)
  plt.plot(ep, rpt, linestyle='dashed')
  plt.ylabel('RMSE (GPa)')
  plt.xlabel('Epoch')
  plt.subplots_adjust(left=0.165, right=0.94, bottom=0.12, top=0.92, hspace=0.05)
  plt.show()
  
plot_ANN_RMSE()
