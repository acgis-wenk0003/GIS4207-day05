from sys import argv
import os

"""delayed import of arcpy"""
arcpy= None

def importarcpy():
    import arcpy
    global arcpy

def exportToKML(infile, outkml):

    """remove file and folder if they exist"""
    if os.path.exists("../output/" + outkml):
        os.remove("../output/" + outkml)
    if os.path.exists("../output/"):
        os.rmdir("../output/")

    """prepare output location"""
    os.mkdir("../output/")
    out_kml = open("../output/" + outkml, "w")

    """get header"""
    out_kml.write(getKmlHeader())

    """get list of locations and their placemark"""
    cursorList = getCursorList(infile)
    for cursor in cursorList:
        placemark = getkmlplacemark(cursor[0], cursor[1], cursor[2], cursor[3])
        out_kml.write(placemark)

    """get footer and save file"""
    out_kml.write(getKmlFooter())
    out_kml.close()

#KML setup code
def getKmlHeader():
    """gets the header from .txt file"""
    """returns the top part of the kml file including the <Document> element"""
    return '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>'

def getKmlFooter():
    """has no parameters and returns </Document></kml>"""
    return '\n</Document>\n</kml>'

def getkmlplacemark(name, prov, lat, lon):
    """returns formated placemark"""
    return '\n\t<Placemark>\n\t\t<name>{name}, {prov}</name>\n\t\t<description>http://www.canmaps.com/topo/nts50/map/001n10.htm</description>\n\t\t<Point>\n\t\t\t<coordinates>{lon},{lat},0</coordinates>\n\t\t</Point>\n\t</Placemark>'.format(name=name, prov=prov, lat=lat, lon=lon)

def getCursorList(infile):
    """returns a list name province and lat long location"""
    importarcpy()

    fieldlist=["Name","Prov", "SHAPE@XY"]
    rows=arcpy.da.SearchCursor(infile, fieldlist)

    cursorlist = []

    for row in rows:
        cursorlist.append((row[0].encode('utf8'), row[1].encode('utf8'), row[2][0], row[2][1]))

    del row
    del rows

    return cursorlist