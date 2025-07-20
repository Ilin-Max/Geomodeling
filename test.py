from Geomodel.Geomodel.Fild import Fild
from Geomodel.Geomodel.Well import Well
import plotly.express as px

fild = Fild("Piltun")

w1 = Well("PA-101")
w1.X_coord = 673322.819999991
w1.Y_coord = 5843822.33

w2 = Well("PA-128")
w2.X_coord = 673328.29
w2.Y_coord = 5843809.29

fild.AddWell(w1)
fild.AddWell(w2)

data = {
    "Well": [w1.name, w2.name],
    "Easting": [w1.X_coord, w2.X_coord],
    "Northing": [w1.Y_coord, w2.Y_coord],
    }

