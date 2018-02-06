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

fieldlist=["Name","Prov", "SHAPE@XY"]
rows=arcpy.da.SearchCursor("..\..\..\Data\Canada\Can_Mjr_Cities.shp", fieldlist ,sql)

cityCount=0
print "Name, Prov, Latitude, Longitude"
for row in rows:
    print "{}, {}, {}, {}".format(row[0], row[1], row[2][0], row[2][1])
    cityCount+=1

print "There are "+ str(cityCount)+" cities in the above list."

del row
del rows