import json 

class DataExtractor:
    def __init__(self, data_type, filename, extract_function):
        self.data_type = data_type
        self.filename = filename
        self.extract_function = extract_function

    def filter_data(self, data):
        return [item for item in data['map_data'] if item['type'] == self.data_type]

    def extract_and_save(self, data):
        filtered_data = self.filter_data(data)
        relevant_data = [self.extract_function(item) for data_group in filtered_data for item in data_group['data'] if self.extract_function(item)]
        self._save_to_md_file(relevant_data)

    def _save_to_md_file(self, output_data):
        filepath = f"data/{self.filename}"
        with open(filepath, "w") as file:
            for line in output_data:
                file.write("- " + line + "\n")

def accommodation_extract(item):
    city = item.get('city')
    name = item.get('name')
    url = item.get('url')
    if city and name and url:
        return f"{city}, {name}, Bilgi Kaynağı: {url}"
    return None


def pharmacy_extract(item):
    city = item.get('city')
    district = item.get('district')
    name = item.get('name')
    if city and district and name:
        return f"{city}, {district}, {name}"
    return None


def gathering_extract(item):
    city = item.get('city')
    name = item.get('name')
    source = item.get('source')
    if city and name and source:
        return f"{city}, {name}, Bilgi Kaynağı: {source}"
    return None


def vet_extract(item):
    name = item.get('name')
    phone_number = item.get('phone_number')
    address = item.get('address')
    if name and phone_number and address:
        return f"{name}, Tel: {phone_number}, Adres: {address}"
    return None


def food_extract(item):
    city = item.get('city')
    county = item.get('county')
    name = item.get('name')
    maps_url = item.get('maps_url')
    url = item.get('url')
    if city and county and name and maps_url and url:
        return f"{city}, {county}, {name}, Konum: {maps_url}, Kaynak: {url}"
    return None


def hospital_extract(item):
    city = item.get('city')
    county = item.get('county')
    name = item.get('name')
    source = item.get('source')
    if city and county and name and source:
        return f"{city}, {county}, {name}, Kaynak: {source}"
    return None


def evacuation_extract(item):
    city = item.get('city')
    county = item.get('county')
    name = item.get('name')
    source = item.get('source')
    if city and county and name and source:
        return f"{city}, {county}, {name}, {source}"
    return None


def main():
    with open('data/map_data.json') as f:
        data = json.load(f)

    extractors = [
        DataExtractor('map-city-accommodation', 'accommodations.md', accommodation_extract),
        DataExtractor('map-container-pharmacy', 'container_pharmacy.md', pharmacy_extract),
        DataExtractor('map-gathering-list', 'gathering_list.md', gathering_extract),
        DataExtractor('map-data-vet', 'vets_list.md', vet_extract),
        DataExtractor('map-food-items', 'food_list.md', food_extract),
        DataExtractor('map-hospital-list', 'hospital_list.md', hospital_extract),
        DataExtractor('map-evacuation-points', 'evacuation_points.md', evacuation_extract)
    ]

    for extractor in extractors:
        extractor.extract_and_save(data)

if __name__ == "__main__":
    main()
