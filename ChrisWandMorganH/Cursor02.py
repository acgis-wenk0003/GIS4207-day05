import os
import arcpy

scriptFolder=os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

fieldlist=["Name","Prov"]

cursor=arcpy.da.SearchCursor("..\..\..\Data\Canada\Can_Mjr_Cities.shp", fieldlist)

currentCity=""

cityCount=0

print "Name, Prov"

for row in cursor:
    if currentCity != row[0]:
        currentCity=row[0]
    print row[0]+", "+ row[1]
    cityCount+=1

print "There are "+ str(cityCount)+" cities in the above list."

del row
del cursor