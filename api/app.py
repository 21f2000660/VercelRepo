import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Specify the correct path to your JSON file
file_path = 'q-vercel-python.json'  # Update this if your file is in a different location

try:
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Print the type of data to confirm it's been loaded correctly
    print(f"Data type: {type(data)}")
    
    # Store the data in a variable for potential further use
    json_data = [{"name":"CQebKCMSwQ","marks":69},{"name":"t","marks":5},{"name":"V8On57G","marks":93},{"name":"xTk","marks":13},{"name":"X6DPzkb97","marks":49},{"name":"6m","marks":83},{"name":"ZhCp2EtY","marks":38},{"name":"J42C","marks":66},{"name":"Bg4","marks":67},{"name":"qOWK","marks":98},{"name":"h","marks":32},{"name":"o","marks":84},{"name":"WHIyW","marks":40},{"name":"VHjeK4","marks":88},{"name":"QKA8ASF1","marks":48},{"name":"E3nLo","marks":62},{"name":"lAR","marks":78},{"name":"B6oN","marks":90},{"name":"f53","marks":95},{"name":"H3kUZs","marks":32},{"name":"mWr0C6","marks":38},{"name":"oC","marks":55},{"name":"mO","marks":72},{"name":"SU8","marks":89},{"name":"Um","marks":24},{"name":"SC5axbDZC","marks":31},{"name":"gvlFcEi9b","marks":98},{"name":"WrSBtk1tDu","marks":76},{"name":"RnoCzQ","marks":93},{"name":"2hqGu","marks":8},{"name":"x","marks":30},{"name":"HLzjbvKpj","marks":56},{"name":"Ai","marks":87},{"name":"yndNAXli8","marks":16},{"name":"B","marks":17},{"name":"yB9A","marks":3},{"name":"Z9f","marks":40},{"name":"Z7WTOFcu00","marks":58},{"name":"MmOTWklviq","marks":97},{"name":"Lj","marks":69},{"name":"tIo","marks":47},{"name":"psVMlnsT","marks":63},{"name":"V0V9Wt","marks":58},{"name":"NnPN","marks":2},{"name":"Ha","marks":50},{"name":"pq9kOKx5OW","marks":20},{"name":"KGZd","marks":19},{"name":"R","marks":58},{"name":"x7boufw","marks":85},{"name":"7A2Tr","marks":19},{"name":"9FO7NR","marks":17},{"name":"JdiQ5N63JX","marks":19},{"name":"NgQJwo1US","marks":13},{"name":"nrrRPc","marks":39},{"name":"WBdYx","marks":8},{"name":"ci7qsxc","marks":15},{"name":"Gq4vAt","marks":74},{"name":"IQk3oEh8AW","marks":51},{"name":"oRuWH","marks":68},{"name":"F","marks":46},{"name":"g","marks":9},{"name":"G","marks":99},{"name":"T8nhruSqx","marks":79},{"name":"Y45","marks":66},{"name":"l6SCxoGN","marks":91},{"name":"vM","marks":34},{"name":"n91","marks":29},{"name":"nHuN6","marks":89},{"name":"1NvA","marks":83},{"name":"xG5btHBQK","marks":23},{"name":"yG9t","marks":24},{"name":"X","marks":37},{"name":"RA6lR99Ur","marks":0},{"name":"VYEqjqj","marks":84},{"name":"on3ik","marks":65},{"name":"nXv1lkO","marks":96},{"name":"QEy","marks":56},{"name":"jXBmk","marks":79},{"name":"1i5K","marks":60},{"name":"iw16Cft","marks":77},{"name":"5slLRtRONq","marks":2},{"name":"KDQOGNo","marks":60},{"name":"usGgkOmdM","marks":49},{"name":"C8xS","marks":99},{"name":"oJf3loq0k7","marks":16},{"name":"q3KHekcTt","marks":53},{"name":"IF8badWSxy","marks":71},{"name":"ylh3","marks":59},{"name":"2QYoCP","marks":91},{"name":"k5","marks":25},{"name":"Hngj2OzEi0","marks":53},{"name":"iVtWMe","marks":86},{"name":"oLhP4","marks":11},{"name":"6mB2zMly0p","marks":21},{"name":"T","marks":6},{"name":"qmV3","marks":16},{"name":"YulvetgzhC","marks":37},{"name":"xpm3Ilp","marks":45},{"name":"1Tp","marks":59},{"name":"oUX","marks":22}]
    print("JSON data loaded successfully")

    @app.route('/api', methods=['GET'])
    def get_marks():
        names = request.args.getlist('name')
        marks = [next((item['marks'] for item in data if item['name'] == name), 0) for name in names]
        return jsonify({"marks": marks})

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: The file '{file_path}' does not contain valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    app.run()
