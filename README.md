Introduction
============
Model slope and curvature from a DEM [1]. The surface is modeled as a six-term polynomial. 

The surface is
F(x,y) = ax<sup>2</sup> + by<sup>2</sup> + cxy + dx + ey + f,

curvature (C) is 

C = 2a + 2b,

which is equivalent to the 2D Laplacian of the surface.

slope (S) is

S = sqrt(d<sup>2</sup> + e<sup>2</sup>),

and smoothed elevation (E) is

E = F(x<sub>c</sub>,y<sub>c</sub>) = ax<sub>c</sub><sup>2</sup> + by<sub>c</sub><sup>2</sup> + cx<sub>c</sub>y<sub>c</sub> + dx<sub>c</sub> + ey<sub>c</sub> + f

where x<sub>c</sub> is the x index of the focal cell and y<sub>c</sub> is the y index of the focal cell.

Use the side length (L), also called scale, to specifying the area of the moving window (L x L) focused on each cell that is used for computing elevation, slope and curvature.

Dependecies
---------
<a href="www.numpy.org">numpy</a>, <a href="http://trac.osgeo.org/gdal/wiki/GdalOgrInPython">GDAL</a>

Example
---------
On Mac or Linux change make sure `surface.py` is set to be executable:
`chmod u+x surface.py`

Create a directory to store output.

`mkdir output`

Then to calculate the elevation, slope, and curvature using a 9 x 9 window with the sample dem ("dem-example.tif") from within the directory containing surface.py type

`./surface.py -d dem-example.tif -o output -l 9`

On Windows you do not need to make the program executable - it already will be. Just make a directory (here called "output") to store the output files.  The run surface.py

`python surface.py -d dem-example.tif -o output -l 9`

Try opening up the output rasters in QGIS or your favorite GIS.

For additional information run

`./surface.py -h` on Mac or Linux 

or

`python surface.py -h` on Windows.


References
---------
[1] Hurst MD, Mudd SM, Walcott R, Attal M, Yoo K (2012) Using hilltop curvature to derive the spatial distribution of erosion rates. J Geophys Res Earth Surf 117:F0217. <a href="http://doi:10.1029/2011JF002057">doi:10.1029/2011JF002057</a>


Notes
---------
For help on getting GDAL up and running see the <a href="http://pcjericks.github.io/py-gdalogr-cookbook/">GDAL cookbook</a>.