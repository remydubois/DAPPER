import numpy as np
from scipy.linalg import circulant
from misc import rk4

def lr(x,n,axis=1):
  return np.roll(x,-n,axis=axis)

def dxdt(x,F):
  a = x.ndim-1
  return np.multiply(lr(x,1,a)-lr(x,-2,a),lr(x,-1,a)) - x + F

def step(x0, t, dt):
  return rk4(lambda t,x: dxdt(x,8.0),x0,np.nan,dt)


# Only strictly valid for m=40 ?
def typical_init_params(m):
  mu0 = 2.34*np.ones(m)
  # Auto-corr-function
  acf = lambda i: 0.0 + 14*(i==0) + 0.9*(i==1) - 4.7*(i==2) - 1.2*(i==3)
  P0  = circulant(acf(mirrored_half_range(m)))
  return mu0, P0

def mirrored_half_range(m):
  return np.roll(np.abs(np.arange(m) - m//2), (m+1)//2)
  #return np.concatenate((range((m+1)//2), range(m//2,0,-1)))
