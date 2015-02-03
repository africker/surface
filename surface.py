import numpy as np
from numpy.linalg import inv



class Surface(object):
	def __init__(self, x, y, z, cx, cy):
		self.x = x
		self.y = y
		self.z = z
		self.cx = cx
		self.cy = cy

	def setX(self):
		xf = self.x.flatten()
		yf = self.y.flatten()
		self.X = np.column_stack(
			[
				xf**2,
				yf**2,
				xf*yf,
				xf,
				yf,
				np.ones(len(xf))
			]
		)

	def _getZ(self):
		""" Get the y vector for regression
		"""
		self.Z = self.z.flatten()

	def fit(self):
		"""Matrix regression
		F(x,y) = ax2+by2+cxy+dx+ey+f
		B = inv(X'X)X'y
		where B is vector of coefficients for F(x,y).
		"""
		self._getZ()
		XTXinv = inv(np.dot(self.X.T, self.X))
		XTy = np.dot(self.X.T, self.Z)
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

	def elevation(self):
		"""Elevation
		F(cx,cy) where cx and cy are coordinates for focal
		pixel
		"""
		X_tilde = np.array([self.cx**2,self.cy**2,
			self.cx*self.cy,self.cx,self.cy,1])
		self.elevation = np.dot(self.B, X_tilde)
		return self.elevation
