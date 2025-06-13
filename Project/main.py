import dcel
import pygmt as pg
import xarray as xr

data = xr.open_dataset("dataset/binned_border_c.nc")

ds = data.values

fig = pygmt.Figure()

fig.coast(
    region="g",
    projection="M6i",
    shorelines="1/0.25p,black",
    borders=[1, 2],  # 1 = national borders, 2 = state/province
    land="lightgray",
    water="skyblue",
    frame=True
)

fig.show()


