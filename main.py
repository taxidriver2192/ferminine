import os
import requests
from bs4 import BeautifulSoup, Comment
import json

# URL to be crawled
url = "https://feminine.planway.com/"

# Send a GET request to the URL
response = requests.get(url)

# Base directory to save the files
base_dir = "produkter"

# Create base directory if it doesn't exist
os.makedirs(base_dir, exist_ok=True)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all comments and remove the comment tags to parse the inner HTML
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment_soup = BeautifulSoup(comment, 'html.parser')
        comment.insert_after(comment_soup)
        comment.extract()

    # Now the soup contains the previously commented HTML as part of the normal HTML
    categories_wrapper = soup.find('div', class_='categoriesWrapper')

    if categories_wrapper:
        categories_data = []

        # Find all category slots
        category_slots = categories_wrapper.find_all('div', class_='slot')
        for category_slot in category_slots:
            category_id = category_slot['data-id']
            category_title = category_slot.find('span', class_='title')
            if category_title:
                category_name = category_title.text.strip()
                category_data = {
                    "id": category_id,
                    "name": category_name,
                    "services": []
                }

                # Look for services under this category
                service_slots = categories_wrapper.find_all('div', class_='slotproductr', attrs={"data-category_id": category_id})
                for service_slot in service_slots:
                    service_id = service_slot['data-id']
                    service_title = service_slot.find('span', class_='title')
                    service_duration = service_slot.find('div', class_='duration')
                    service_price = service_slot.find('div', class_='price')
                    service_description = service_slot.find('div', class_='description')

                    if service_title:
                        service_data = {
                            "service_id": service_id,
                            "name": service_title.text.strip(),
                            "duration": service_duration.text.strip() if service_duration else None,
                            "price": service_price.text.strip() if service_price else None,
                            "description": service_description.text.strip() if service_description else None
                        }
                        
                        category_data["services"].append(service_data)

                categories_data.append(category_data)

        # Convert the collected data to JSON and save to a file
        json_file_path = os.path.join(base_dir, "services.json")
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(categories_data, json_file, ensure_ascii=False, indent=4)

        # Print the JSON data for verification
        print(json.dumps(categories_data, ensure_ascii=False, indent=4))
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
