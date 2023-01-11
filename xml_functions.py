import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def clean_xml(root):
    for elem in root.findall('.//*[not(node())]'):
        elem.clear()
    for elem in root.findall('.//*[not(@*)]'):
        elem.clear()
    return root

def transform_xml(root):
    for elem in root.iter():
        elem.set('new_attribute', str(len(elem.text or "")))
    return root
    
def visualize_xml(root):
    values = [int(elem.attrib.get('new_attribute',0)) for elem in root.iter()]
    plt.bar(range(len(values)), values)
    plt.show()

try:
    # load the xml file
    tree = ET.parse('data.xml')
    root = tree.getroot()
    # clean the data
    root = clean_xml(root)
    # Transform the data
    root = transform_xml(root)
    # Visualize the data
    visualize_xml(root)
except FileNotFoundError:
    # Handle missing file
    print('data.xml file not found')
    exit(1)
except ET.ParseError:
    # Handle invalid XML
    print('Invalid XML file')
    exit(1)
