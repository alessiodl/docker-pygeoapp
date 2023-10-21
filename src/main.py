import pandas as pd
import geopandas as gpd
from osgeo import gdal
import earthaccess
import openpyxl

pandas_v = pd.__version__
geopandas_v = gpd.__version__
gdal_v = gdal.__version__
earthaccess_v = earthaccess.__version__
openpyxl_v = openpyxl.__version__

print ('Installati Pandas {0}, GeoPandas {1}, GDAL {2}, Earthaccess {3}, OpenPyXl {4}'.format(pandas_v, geopandas_v, gdal_v, earthaccess_v, openpyxl_v))