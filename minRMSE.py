import numpy as np

def plot_ANN_RMSE():
## Number of Directory and Directory Name ##
  ndir = 1;  dirnam = [[]]*ndir; fep = [[]]*ndir 
  dirnam[0] = './ANN_RMSEs'
  
## Computational Condition ##    
  fep [0] = 99999  # Final epoch of file 0  
  fvib = 0       # Vibrational region E:0 EF:560 EFP:620
  
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
  print('total number of epoch: %d' %(cnt))
  print('Vibrational region: 0-%d epoch' %(fvib))
  print('\nTRAIN SET')
  print('minimum RMSE(E) and epoch:')
  print(np.min(re[fvib:]), fvib + np.argmin(re[fvib:]))
  print('minimum RMSE(F) and epoch:')
  print(np.min(rf[fvib:]), fvib + np.argmin(rf[fvib:]))
  print('minimum RMSE(P) and epoch:')
  print(np.min(rp[fvib:]), fvib + np.argmin(rp[fvib:]))

  print('\nTEST SET')
  print('minimum RMSEt(E) and epoch:')
  print(np.min(ret[fvib:]), fvib + np.argmin(ret[fvib:]))
  minep = fvib + np.argmin(ret[fvib:]) 
  print('minimum RMSEt(F) and epoch:')
  print(np.min(rft[fvib:]), fvib + np.argmin(rft[fvib:]))
  print('minimum RMSEt(P) and epoch:')
  print(np.min(rpt[fvib:]), fvib + np.argmin(rpt[fvib:]))

  print('\nRMSEs at epoch %d' %(minep))
  print(re[minep], rf[minep], rp[minep], ret[minep], rft[minep], rpt[minep])
  
plot_ANN_RMSE()
