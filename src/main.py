import pandas as pd
import geopandas as gpd
from osgeo import gdal

pandas_v = pd.__version__
geopandas_v = gpd.__version__
gdal_v = gdal.__version__

print ('Installati Pandas {0}, GeoPandas {1}, GDAL {2}'.format(pandas_v, geopandas_v, gdal_v))