import os
import arcpy

scriptFolder=os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

rows=arcpy.SearchCursor("..\..\..\Data\Canada\Can_Mjr_Cities.shp",
                        "",
                        "",
                        "Name; Prov")
currentCity=""
cityCount=0
print "Name, Prov"
for row in rows:
    if currentCity != row.Name:
        currentCity=row.Name
    print row.Name+", "+ row.Prov
    cityCount+=1

print "There are "+ str(cityCount)+" cities in the above list."

del row
del rows