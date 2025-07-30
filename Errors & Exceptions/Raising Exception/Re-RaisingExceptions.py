def process_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            # Process data
    except FileNotFoundError as e:
        print(f"File not found: {filename}")
        # Re-raise the exception
        raise
    
try:
    process_file("nonexistentfile.txt")
except FileNotFoundError as e:
    print("Handling the excemption at the higher level")