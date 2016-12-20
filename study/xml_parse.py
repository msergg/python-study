import xml.etree.ElementTree as ET

root = ET.Element('days')
day = ET.SubElement(root, 'day')

day.set('date', '01.01.2017')

task = ET.SubElement(day, 'task')
task.text = 'Wake up!'

task2 = ET.SubElement(day, 'task')
task2.text = 'Make coffee!'

tree = ET.ElementTree(root)

tree.write('tasks.xml')





#

doc = ET.parse('tasks.xml')

root = doc.getroot()
root.tag


print doc.findall('.//task')[0].text



doc.findall('.//task')[0].text = 'Changed'
print doc.findall('.//task')[0].text










# Parsers:
# DOM
# STAX
# SAX





from xml.dom import minidom

doc = minidom.parse('tasks.xml')