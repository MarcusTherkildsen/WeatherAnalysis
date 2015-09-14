# WeatherAnalysis
Plots NASA weather forecasting data from https://cds.nccs.nasa.gov/nex-gddp/

## Install non-standard packages

  If using Anaconda

      conda install basemap
      conda install netcdf4

  else try
  
      sudo apt-get install basemap
      sudo apt-get install netcdf4


## Download the wanted weather file
 
  Just go to 

      ftp://ftp.nccs.nasa.gov/BCSD/rcp45/day/atmos/pr/r1i1p1/v1.0/
 
  and chose a file ending with this format type

      pr_day_BCSD_rcp45_r1i1p1_ACCESS1-0_2100.nc

  Others might work as well but I have not tested them. Feel free to do so. 
  
  Now just run the script and a plot for each day will be saved. 
