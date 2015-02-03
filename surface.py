import argparse
import numpy as np
from numpy.linalg import inv
import gdal
from gdalconst import *
from osgeo import osr


def getArgs():
	parser = argparse.ArgumentParser(
		description="Surface analysis of a DEM"
	)
	parser.add_argument(
		"-d",
		"--dem",
		required=True,
		type=str,
		help= "Input DEM"
	)
	parser.add_argument(
		"-l",
		"--length",
		required=True,
		type = int,
		help = "Side length for L x L kernel"
	)
	parser.add_argument(
		"-o",
		"outdir",
		required=True,
		type = str,
		help = "Output directory"
	)
	parser.add_argument(
		"-v",
		"--verbose",
		required = False,
		action = "store_true",
		help = "Print status updates while executing"
	)
	return parser.parse_args()

class Raster(object):
	def __init__(self, args):
		self.args = args

	def read(self, infile):
		# never want to change the original input raster so use read only constant
		self.infile = infile
		self.raster = gdal.Open(self.infile, GA_ReadOnly)
		self.band = self.raster.GetRasterBand(1)
		self.NDV = self.band.GetNoDataValue()
		self.x = self.band.XSize
		self.y = self.band.YSize
		DataType = self.band.DataType
		self.DataType = gdal.GetDataTypeName(DataType)
		self.GeoT = self.raster.GetGeoTransform()
		prj = osr.SpatialReference()
		self.prj = prj.ImportFromWkt(self.raster.GetProjectionRef())

	def getArray(self):
		self.array = band.ReadAsArray()
		return self.array

	def write(self, array, name):
		driver= gdal.GetDriverByName("GTiff")
		if self.DataType = "Float32":
			self.DataType = gdal.GDT_Float32
		self.outdata = array
		self.outdata[np.isnan(self.outdata)] = self.NDV
		# Create output file
		DataSet = driver.Create(self.name, self.x, self.y, 
			self.band, self.DataType)
		DataSet.SetGeoTransform(self.GeoT)
		DataSet.SetProjection(self.prj.ExportToWkt())
		# Write data array
		DataSet.GetRasterBand(1).WriteArray(self.outdata)
		DataSet.GetRasterBand(1).SetNoDataValue(self.NDV)
		DataSet = None


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



def main():
	pass

if __name__ == "__main__":
	main()