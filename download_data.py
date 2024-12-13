"""Download Koulukone data from YLE file and save it to a CSV file"""
import re
import requests
import os

# URL of the JavaScript file containing the data
URL = 'https://deski.yle.fi/2023-02-S2-oppilaat-kouluittain/js/script.js'
# Output CSV file
OUTPUT_FOLDER = 'data'
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, 'schools.csv')


def extract_data(content):
    """Function to extract data between backticks and normalize line endings"""
    match = re.search(r'const Mk=`([\s\S]*?)`', content)
    if match:
        data = match.group(1).replace('\\r', '') + '\n'
        print(f"Data successfully extracted to {OUTPUT_FILE}")
        return data
    else:
        raise ValueError('No matching data found.')


def main():
    """Main function to download data and save it to a file"""
    try:
        response = requests.get(URL)
        response.raise_for_status()
        response.encoding = 'utf-8'  # Specify the encoding
        content = response.text
        normalized_data = extract_data(content)

        # Create the output folder if it doesn't exist
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
            file.write(normalized_data)
    except Exception as e:
        print('An error occurred:', e)


if __name__ == '__main__':
    main()
