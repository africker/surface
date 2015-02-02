Introduction
============
Model slope and curvature from a DEM [1]. The surface is modeled as a six-term polynomial. 

The surface is
F(x,y) = ax^2 + by^2 + cxy + dx + ey + f,

curvature (C) is 
C = 2a + 2b,

which is equivalent to the 2D Laplacian of the surface.

Slope (S) is
S = sqrt(d^2 + e^2).

Use the side length (L), also called scale, to specifying the area of the moving window (L x L) focused on each cell that is used for computing slope and curvature.

Dependecies
---------
<a href="www.numpy.org">numpy</a>, <a href="http://trac.osgeo.org/gdal/wiki/GdalOgrInPython">GDAL</a>

References
---------
[1] Hurst MD, Mudd SM, Walcott R, Attal M, Yoo K (2012) Using hilltop curvature to derive the spatial distribution of erosion rates. J Geophys Res Earth Surf 117:F0217. <a href="http://doi:10.1029/2011JF002057">doi:10.1029/2011JF002057</a>


Notes
---------
For help on getting GDAL up and running see the <a href="http://pcjericks.github.io/py-gdalogr-cookbook/">GDAL cookbook</a>.