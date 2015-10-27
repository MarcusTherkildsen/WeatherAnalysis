# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:37:05 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import matplotlib.ticker
from matplotlib.dates import num2date
# from time import strftime
'''
Instruction from http://www.hydro.washington.edu/~jhamman/hydro-logic/blog/
2013/10/12/plot-netcdf-data/

Stuff about the data
https://cds.nccs.nasa.gov/wp-content/uploads/2015/06/
NEX-GDDP_Tech_Note_v1_08June2015.pdf

Data website https://cds.nccs.nasa.gov/nex-gddp/

Installed nedcdf4 and basemap by using the anaconda terminal
conda install basemap
conda install netcdf4
'''

if __name__ == '__main__':

    # Path to file
    my_example_nc_file = 'D:/Data/pr_day_BCSD_rcp45_r1i1p1_ACCESS1-0_2100.nc'

    # Use the netCDF4 package to read in the .nc file
    fh = Dataset(my_example_nc_file, mode='r')

    # Defining variables
    # Longitudes
    lons = fh.variables['lon'][:]
    # Latitudes
    lats = fh.variables['lat'][:]
    # The dates
    dates = num2date(fh.variables['time'][:])
    # Precipitation
    tmax = fh.variables['pr'][:]*60*24
    # The unit of precipitation, kg m-2 s-1
    tmax_units = fh.variables['pr'].units

    # Releasing file from memory
    fh.close()

    # Defining the map
    m = Basemap(projection='mill', lon_0=180)

    # Because our lon and lat variables are 1D,
    # use meshgrid to create 2D arrays
    # (Not necessary if coordinates are already in 2D arrays.)
    lon, lat = np.meshgrid(lons, lats)
    xi, yi = m(lon, lat)

    # Chose the value interval to include in the plots
    my_min = 0.2
    my_max = 2

    # Number of levels, basically defines how many intervals to split the
    # colorbar into
    clevs = np.linspace(0.2, 2, 100)

    cb_locs = np.linspace(0.2, 2, 5)
    cb_labels = np.linspace(0.2, 2, 5)
    for i in xrange(len(tmax[:, 0, 0])):

        # Draw grid at certain longitudes and latitudes
        m.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0])
        m.drawmeridians(np.arange(m.lonmin, m.lonmax+30, 60),
                        labels=[0, 0, 0, 1])

        # Fancy overlay
        m.bluemarble()

        # Plotting precipitation data
        cs = m.contourf(xi, yi, np.squeeze(tmax[i, :, :]),
                        clevs, cmap='jet', zorder=100)

        # Colorbar
        cbar = m.colorbar(cs, location='bottom', pad="10%")
        # Fixing white stripes in colorbar
        cbar.solids.set_edgecolor('face')

        # Formatting ticks
        cbar.locator = matplotlib.ticker.FixedLocator(cb_locs)
        cbar.formatter = matplotlib.ticker.FixedFormatter(cb_labels)
        cbar.update_ticks()

        # Add Title
        plt.title('Mean precipitation, [mm/day], ' +
                  dates[i].strftime('%d-%m-%Y'))

        '''
        Uncomment the commented lines below to save the plots
        '''

        # plt.savefig(filepath + '.png',dpi=400,bbox_inches='tight')
        plt.show()
        # plt.close('all')
