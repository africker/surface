import numpy as np
from numpy.linalg import inv

def getX(L):
	"""X matrix for six term polynomial regression
	"""
	# Computing X matrix outside of Surface object
	# reduces times X must be computed.
	axis = np.arange(L)
	col, row = np.meshgrid(axis,axis)
	# A[row,col] will reproduce A
	colf = col.flatten()
	rowf = row.flatten()
	X = np.column_stack(
		[
			colf**2,
			rowf**2,
			colf*rowf,
			colf,
			rowf,
			np.ones(len(colf))
		]
	)
	return X

class Surface(object):
	def __init__(self, A, X):
		self.A = A
		self.X = X

	def _getY(self):
		""" Get the y vector for regression
		"""
		self.y = A.flatten()

	def fit(self):
		"""Matrix regression
		F(x,y) = ax2+by2+cxy+dx+ey+f
		B = inv(X'X)X'y
		where B is vector of coefficients for F(x,y).
		"""
		self._getY()
		XTXinv = inv(np.dot(self.X.T, self.X))
		XTy = np.dot(self.X.T, self.y)
		self.B = np.dot(XTXinv, XTy)

	def curvature(self):
		"""The 2D Laplacian
		C=2a+2b
		"""
		a,b= self.B[0],self.B[1]
		self.C = 2*a + 2*b
		return self.C

	def slope(self):
		"""Slope
		S=sqrt(d2+e2)
		"""
		d, e = self.B[3],self.B[4]
		self.S = np.sqrt(d**2 + e**2)
		return self.S
