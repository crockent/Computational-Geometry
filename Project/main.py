import dcel
import pygmt
import xarray as xr
from shapely.geometry import Point

data = xr.open_dataset("dataset/binned_border_c.nc")

ds = data.values

# Load sample Earth relief data
grid = pygmt.datasets.load_earth_relief(resolution="01d")

# Plot the data
fig = pygmt.Figure()
fig.grdimage(
    grid=grid,
    region=[-180, 180, -80, 80],  # minlon, maxlon, minlat, maxlat (latitudes < 90)
    projection="M6i",
    frame=True,
)
fig.show()


# Example: Load sample data (replace with your actual dataset)


# Example dataset
#print(data)
# If your data is a DataFrame with 'longitude' and 'latitude' columns:
#points = [Point(row.longitude, row.latitude) for row in data.itertuples()]

# Now 'points' is a list of shapely Point objects
# print(points[:100])  # Show first 5 points

""" 
fig.coast(
    region=[-180, 180, -80, 80],  # minlon, maxlon, minlat, maxlat (latitudes < 90)
    projection="M6i",
    frame=True,
    land="gray",
    water="skyblue"
)

fig.show()"""


