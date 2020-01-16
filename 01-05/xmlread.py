import xml.dom.minidom
with open('/home/zaidi/GitHub-Projects/praxis-academy/01-05/iso3166_full.xml') as xmldata:
    xml = xml.dom.minidom.parseString(xmldata.read()) 
    xml_pretty_str = xml.toprettyxml()
print (xml_pretty_str)