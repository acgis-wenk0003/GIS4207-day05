from sys import argv
import os
arcpy= None
def importarcpy():
    import arcpy
    global arcpy
if len(argv) !=2:
    print "Usage: <province abbreviation>"

else:
    importarcpy()
province=str(argv[1].upper())
sql= "PROV = '%s' " %province


rows= arcpy.SearchCursor("..\..\..\Data\Canada\Can_Mjr_Cities.shp",
                        sql,
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