from json_functions import clean_json, transform_json, visualize_json
from xml_functions import clean_xml, transform_xml, visualize_xml
from yaml_functions import clean_yaml, transform_yaml, visualize_yaml
from html_functions import clean_html, transform_html, visualize_html

def process_json(file_name):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f'{file_name} file not found')
        return
    except json.decoder.JSONDecodeError:
        print(f'Invalid JSON file')
        return
    data = clean_json(data)
    data = transform_json(data)
    if data:
        visualize_json(data)
    else:
        print("Data is empty, nothing to visualize")

def process_xml(file_name):
    try:
        tree = ET.parse(file_name)
        root = tree.getroot()
    except FileNotFoundError:
        print(f'{file_name} file not found')
        return
    except ET.ParseError:
        print(f'Invalid XML file')
        return
    root = clean_xml(root)
    root = transform_xml(root)
    visualize_xml(root)
    
def process_yaml(file_name):
    try:
        with open(file_name, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f'{file_name} file not found')
        return
    except yaml.YAMLError as e:
        print(f"Invalid YAML file {e}")
        return
    data = clean_yaml(data)
    data = transform_yaml(data)
    visualize_yaml(data)
    
def process_html(file_name):
    try:
        with open(file_name, 'r') as f:
            html = f.read()
    except FileNotFoundError:
        print(f'{file_name} file not found')
        return
    soup = BeautifulSoup(html, 'html.parser')
    soup = clean_html(soup)
    soup = transform_html(soup)
    visualize_html(soup)
    
def format(file_name, file_type):
    file_types_function = {
        'json': process_json,
        'xml': process_xml,
        'yaml': process_yaml,
        'html': process_html
    }
    function = file_types_function.get(file_type)
    if function:
        function(file_name)
    else:
        print(f'{file_type} is not a supported file type')
