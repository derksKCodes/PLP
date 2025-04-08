
def process_file():
    filename = input("Enter the name of the file to process: ")
    try:
        # Open the file with UTF-8 encoding and replace errors with the replacement character
        with open(filename, 'r', encoding='utf-8', errors='replace') as file:
            data = file.read()  # Read all contents of the file
            print("File content:\n", data)  # Print the original content of the file
            
        # Count the number of words in the file
        word_count = len(data.split())
        print(f"Word count in the file: {word_count}")
        
        # Modify the data (replace commas with newlines and remove quotes, then convert to uppercase)
        modified_data = data.replace(',', '\n').replace('"', '').upper().strip()
        
        # Write the modified data to output.txt
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(modified_data)  # Write the modified content
            output_file.write(f"\nWord count: {len(modified_data.split())}")  # Write word count
            print("Modified data written to output.txt")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")  # Handle the case when file is not found
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any other unexpected errors

process_file()
