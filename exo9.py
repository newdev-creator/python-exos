import json
from typing import Dict

def create_data() -> Dict[str, str]:
    """Creates a dictionary containing name, age, and occupation."""
    data: Dict[str, str] = {
        'name': 'John',
        'age': 30,
        'occupation': 'Developer'  # Fixed the extra space in 'occupation'
    }
    return data

def main() -> None:
    """Main function to encode data into JSON format and print it."""
    data = create_data()  # Get the data dictionary
    json_data = json.dumps(data)  # Convert the dictionary to a JSON string
    print(json_data)  # Output the JSON string

# Call the main function
if __name__ == "__main__":
    main()