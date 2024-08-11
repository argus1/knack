from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search_images():
    # Get the image URL from the request
    image_url = request.form.get('image_url')

    # Make a POST request to the Google Lens API
    api_url = 'https://vision.googleapis.com/v1/images:annotate?key=YOUR_API_KEY'
    headers = {'Content-Type': 'application/json'}
    data = {
        'requests': [
            {
                'image': {
                    'source': {
                        'imageUri': image_url
                    }
                },
                'features': [
                    {
                        'type': 'WEB_DETECTION'
                    }
                ]
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)

    # Process the response and extract relevant information
    if response.status_code == 200:
        # Extract the search results from the response
        search_results = response.json()['responses'][0]['webDetection']['webEntities']

        # Print the search results
        for result in search_results:
            print(result['description'])

        return 'Search completed successfully'
    else:
        return 'Error occurred while searching'

if __name__ == '__main__':
    app.run()
