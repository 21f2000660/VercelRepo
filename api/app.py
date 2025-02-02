import json
import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Specify the correct path to your JSON file
file_path = 'data.json'  # Update this if your file is in a different location

try:
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Print the type of data to confirm it's been loaded correctly
    print(f"Data type: {type(data)}")
    
    # Store the data in a variable for potential further use
    json_data = data
    print("JSON data loaded successfully")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: The file '{file_path}' does not contain valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
