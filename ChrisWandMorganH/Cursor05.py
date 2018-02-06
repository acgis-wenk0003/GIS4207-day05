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

outfile=open("cursor05_output.kml","w")

#KML setup code
def getKmlHeader():
    """gets the header from .txt file"""
    header_line1="<?xml version="+'"1.0"'+ ' encoding="UTF-8"?>'
    header_line2='<kml xmlns="http://www.opengis.net/kml/2.2">'
    header_line3='<Document>'
    return header_line1+'\n'+header_line2+'\n'+header_line3+'\n'

def getKmlFooter():
    """returns the kml footer"""
    return "</Document>"+'\n'+'</kml>'+'\n'
def kmlplacemark(values):
    lines="""
    <Placemark>
    <name>"""+value[0]+','+values[1]+"""</name>
    <description>http://www.canmaps.com/topo/nts50/map/001n10.htm</description>
    <Point>
      <coordinates>"""+values[2][0]+','+values[2][1]"""</coordinates>
    </Point>
   </Placemark>"""

#cursor code
fieldlist=["Name","Prov", "SHAPE@XY"]
rows=arcpy.da.SearchCursor("..\..\..\Data\Canada\Can_Mjr_Cities.shp", fieldlist)

cityCount=0
print "Name, Prov, Latitude, Longitude"
for row in rows:
    print "{}, {}, {}, {}".format(row[0], row[1], row[2][0], row[2][1])
    cityCount+=1

print "There are "+ str(cityCount)+" cities in the above list."

del row
del rows