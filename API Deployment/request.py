import requests
import json
import os

# Function for single image ocr
def ocr_request_api(document_type, image_path, output_path):

    # Base url for ocr
    url_base = 'http://localhost:5000/ocr/local/'

    # Create url based on document type
    url = url_base + document_type

    # Send a POST request to the endpoint with the image path
    response = requests.post(url, data={'image_path': image_path,
                                        'type' : type})
    # Print the response text
    print(response.content)

    # Check if the response status is successful (200)
    if response.status_code == 200:
        # Convert response to JSON format
        json_data = json.loads(response.content)
        
        # Save JSON data to a file
        with open(output_path, 'w') as f:
            json.dump(json_data, f)
        
        print(f"Saved JSON file to {output_path}")
    else:
        print(f"Error: Response status code is {response.status_code}")

# ocr_request_api(document_type = 'tdp',
#                 image_path = 'D:\Magang dll\Kampus Gratis (MSIB Batch 4)\coding\Inputting Automattion\Dokumen_TDP\TDP_6.jpg',
#                 output_path= 'D:\Magang dll\Kampus Gratis (MSIB Batch 4)\coding\Inputting Automattion\API Deployment\json_output\\tdp.json')

# Function for folder that contains image for ocr purposes
def ocr_request_dir(document_type, dir_path, output_path, reset_data = False):
    # Base url for ocr
    url_base = 'http://localhost:5000/ocr/local/'

    # Create url based on document type
    url = url_base + document_type
    
    # List all image files in the directory
    image_list = os.listdir(dir_path)

    # Filter the list to include only image files, e.g. JPG or PNG
    image_extensions = [".jpg", ".jpeg", ".png"]
    image_files = [f for f in image_list if os.path.splitext(f)[1].lower() in image_extensions]
    
    # If reset_data is True, delete the existing output file
    if reset_data and os.path.exists(output_path):
        os.remove(output_path)

    # Load existing JSON data
    if os.path.exists(output_path):
        with open(output_path, 'r') as f:
            # Load existing JSON data from the output file
            existing_data = json.load(f)
    else:
        # Create an empty dictionary for the JSON data
        existing_data = []

    # Use for loop to loop over the image files and call your test function for each one
    for image in image_files:
        image_path = os.path.join(dir_path, image)

        # Send a POST request to the endpoint with the image path
        response = requests.post(url, data={'image_path': image_path,
                                            'type' : type})
        
        # Print the response text
        print(response.content)

        # Check if the response status is successful (200)
        if response.status_code == 200:
            # Convert response to JSON format
            new_data = json.loads(response.content)
            
            # Append new data to existing data
            existing_data.append(new_data)
        else:
            print(f"Error: Response status code is {response.status_code}")
    if response.status_code == 200: 
        # Save JSON data to a file
        with open(output_path, 'w') as f:
            json.dump(existing_data, f)
        print(f"Saved JSON file to {output_path}")

# ocr_request_dir(document_type= 'nib',
#                 dir_path = 'D:\Magang dll\Kampus Gratis (MSIB Batch 4)\coding\Inputting Automattion\Dokumen NIB',
#                 output_path = 'D:\\Magang dll\\Kampus Gratis (MSIB Batch 4)\\coding\\Inputting Automattion\\API Deployment\json_ouput_dir\\nib.json',
#                 reset_data = True)

# Function for folder that contains image (5 type of differece document) for ocr purposes
def ocr_request_diff_doc(dir_path, output_path, reset_data = False):
    # List all image files in the directory
    image_list = os.listdir(dir_path)

    # If reset_data is True, delete the existing output file
    if reset_data and os.path.exists(output_path):
        os.remove(output_path)

    # Load existing JSON data
    if os.path.exists(output_path):
        with open(output_path, 'r') as f:
            # Load existing JSON data from the output file
            existing_data = json.load(f)
    else:
        # Create an empty dictionary for the JSON data
        existing_data = []

    # Filter the list to include only image files, e.g. JPG or PNG
    image_extensions = [".jpg", ".jpeg", ".png"]
    image_files = [f for f in image_list if os.path.splitext(f)[1].lower() in image_extensions]

    # for loop to loop over the image files and categorize the document
    for image in image_files:
        image_name = os.path.splitext(image)[0].lower()
        # Use If statement to categorize the document
        if image_name == 'tdp':
            # Create url based on document type
            url = 'http://localhost:5000/ocr/local/tdp'
            image_path = os.path.join(dir_path, image)
            # Send a POST request to the endpoint with the image path
            response = requests.post(url, data={'image_path': image_path})
            # Print the response text
            print(response.content)

            # Check if the response status is successful (200)
            if response.status_code == 200:
                # Convert response to JSON format
                new_data = json.loads(response.content)
                # Append new data to existing data
                existing_data.append({'tdp' : new_data})
            else:
                print(f"Error: Response status code is {response.status_code}")


        elif image_name == 'siup':
            # Create url based on document type
            url = 'http://localhost:5000/ocr/local/siup'
            image_path = os.path.join(dir_path, image)
            # Send a POST request to the endpoint with the image path
            response = requests.post(url, data={'image_path': image_path})
            # Print the response text
            print(response.content)

            # Check if the response status is successful (200)
            if response.status_code == 200:
                # Convert response to JSON format
                new_data = json.loads(response.content)
                # Append new data to existing data
                existing_data.append({'siup' : new_data})
            else:
                print(f"Error: Response status code is {response.status_code}")
        
        elif image_name == 'npwp':
            # Create url based on document type
            url = 'http://localhost:5000/ocr/local/npwp'
            image_path = os.path.join(dir_path, image)
            # Send a POST request to the endpoint with the image path
            response = requests.post(url, data={'image_path': image_path})
            # Print the response text
            print(response.content)

            # Check if the response status is successful (200)
            if response.status_code == 200:
                # Convert response to JSON format
                new_data = json.loads(response.content)
                # Append new data to existing data
                existing_data.append({'npwp' : new_data})
            else:
                print(f"Error: Response status code is {response.status_code}")
        
        elif image_name == 'skdp':
            # Create url based on document type
            url = 'http://localhost:5000/ocr/local/skdp'
            image_path = os.path.join(dir_path, image)
            # Send a POST request to the endpoint with the image path
            response = requests.post(url, data={'image_path': image_path})
            # Print the response text
            print(response.content)

            # Check if the response status is successful (200)
            if response.status_code == 200:
                # Convert response to JSON format
                new_data = json.loads(response.content)
                # Append new data to existing data
                existing_data.append({'skdp' : new_data})
            else:
                print(f"Error: Response status code is {response.status_code}")

        elif image_name == 'nib':
            # Create url based on document type
            url = 'http://localhost:5000/ocr/local/nib'
            image_path = os.path.join(dir_path, image)
            # Send a POST request to the endpoint with the image path
            response = requests.post(url, data={'image_path': image_path})
            # Print the response text
            print(response.content)

            # Check if the response status is successful (200)
            if response.status_code == 200:
                # Convert response to JSON format
                new_data = json.loads(response.content)
                # Append new data to existing data
                existing_data.append({'nib' : new_data})
            else:
                print(f"Error: Response status code is {response.status_code}")
         
        elif image_name == 'sim':
            # Create url based on document type
            url = 'http://localhost:5000/ocr/local/sim'
            image_path = os.path.join(dir_path, image)
            # Send a POST request to the endpoint with the image path
            response = requests.post(url, data={'image_path': image_path})
            # Print the response text
            print(response.content)

            # Check if the response status is successful (200)
            if response.status_code == 200:
                # Convert response to JSON format
                new_data = json.loads(response.content)
                # Append new data to existing data
                existing_data.append({'sim' : new_data}) 
            else:
                print(f"Error: Response status code is {response.status_code}")

    if response.status_code == 200: 
        # Save JSON data to a file
        with open(output_path, 'w') as f:
            json.dump(existing_data,  f, indent= 1)
        print(f"Saved JSON file to {output_path}")

          
ocr_request_diff_doc(dir_path = 'input_dirr_dif_doc',
                     output_path = 'output_dirr_dif_doc\diff_doc.json',
                     reset_data = True)

    

