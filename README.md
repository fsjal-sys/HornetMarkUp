JSON, XML, YAML, HTML Processing Scripts

A set of scripts to clean, transform, and visualize JSON, XML, YAML, and HTML files.
Requirements

    Python 3.x
    beautifulsoup4
    matplotlib (if you want to visualize the data)

Installation

pip install beautifulsoup4 matplotlib

Usage

python formatter.py [file_name] [file_type]

Where [file_name] is the path to the file you want to process, and [file_type] is the type of file, this could be json, xml, yaml, or html.
Scripts
json_functions.py

This script contains the following functions:

    clean_json(data) : Takes a JSON object and removes any key-value pairs where the value is None
    transform_json(data) : Takes a JSON object and adds a new key-value pair to each record, where the key is "new_field" and the value is the length of the value of the key "existing_field"
    visualize_json(data) : Takes a JSON object and create a bar chart that visualizes the values of the key "new_field"

xml_functions.py

This script contains the following functions:

    clean_xml(root) : Takes an xml element tree root and remove any elements that have no children or attributes
    transform_xml(root) : Takes an xml element tree root and adds an attribute "new_attribute" for each element with the length of element text
    visualize_xml(root) : Takes an xml element tree root and create a bar chart that visualizes the values of the attribute "new_attribute"

yaml_functions.py

This script contains the following functions:

    clean_yaml(data) : Takes a YAML object and removes any key-value pairs where the value is None
    transform_yaml(data) : Takes a YAML object and adds a new key-value pair to each dictionary, where the key is "new_field" and the value is the length of the value of the key "existing_field"
    visualize_yaml(data) : Takes a YAML object and create a bar chart that visualizes the values of the key "new_field"

html_functions.py

This script contains the following functions:

    clean_html(soup) : Takes a BeautifulSoup object and removes any tags that have no content
    transform_html(soup) : Takes a BeautifulSoup object and adds an attribute "new_attribute" for each tag with the length of tag text
    visualize_html(soup) : Takes a BeautifulSoup object and create a bar chart that visualizes the values of the attribute "new_attribute"
