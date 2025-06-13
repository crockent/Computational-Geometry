import dcel
import pygmt as pg
import xarray as xr

data = xr.open_dataset("dataset/binned_border_c.nc")

print(data)

