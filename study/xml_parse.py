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

doc.childNodes[0].tagName

doc.getElementsByTagName('task')[0].toxml()

doc.getElementsByTagName('task')[0].firstChild.toxml()





#insertChild
#removeChild
#writexml






# for HUGE files
from xml.dom import pulldom


doc = pulldom.parse('tasks.xml')

for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'task':
        doc.expandNode(node)
        print node.toxml()









# sax
from xml import sax

class MyHandler(sax.ContentHandler):
    def startElement(self, name, attrs):
        if name == 'task':
            self.task = True

    def characters(self, content):
        if self.task:
            content = 'test'
            print content

    def endElement(self, name):
        if name == 'task':
            self.task = False

    def __init__(self):
        self.task = False



parser1 = sax.make_parser()

parser1.setContentHandler(MyHandler())
parser1.parse(open('tasks.xml', 'r'))
