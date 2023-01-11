from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def clean_html(soup):
    for tag in soup.find_all(lambda tag: tag.get_text() == ""):
        tag.extract()
    return soup

def transform_html(soup):
    for tag in soup.find_all():
        tag['new_attribute'] = len(tag.get_text())
    return soup

def visualize_html(soup):
    values = [int(tag.get('new_attribute', 0)) for tag in soup.find_all()]
    plt.bar(range(len(values)), values)
    plt.show()

try:
    # Load the HTML file
    with open('data.html', 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    # Clean the data
    soup = clean_html(soup)
    # Transform the data
    soup = transform_html(soup)
    # Visualize the data
    visualize_html(soup)
except FileNotFoundError:
    # Handle missing file
    print('data.html file not found')
    exit(1)
except Exception as e:
    # Handle other exceptions
    print(f"An error has ocurred: {e}")
    exit(1)

