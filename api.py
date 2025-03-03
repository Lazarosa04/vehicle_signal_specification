import yaml
import sys

def read_yaml(file_path):
    """Read and load a YAML file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(file_path, data):
    """Write data to a YAML file."""
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def get_signal_value(data, signal_path):
    """Get the value of a signal in the data."""
    keys = signal_path.split('.')
    d = data
    for key in keys:
        d = d.get(key, None)
        if d is None:
            return None
    return d

def set_signal_value(data, signal_path, value):
    """Set the value of a signal in the data."""
    keys = signal_path.split('.')
    d = data
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value

def main():
    file_path = 'visualizer.yaml'
    
    while True:
        print("\nOptions:")
        print("1. Read signal value")
        print("2. Set signal value")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = read_yaml(file_path)
            signal_path = input("Enter the signal path: ")
            value = get_signal_value(data, signal_path)
            if value is not None:
                print(f"The value of {signal_path} is {value}")
            else:
                print(f"Signal path {signal_path} not found.")
        
        elif choice == '2':
            data = read_yaml(file_path)
            signal_path = input("Enter the signal path: ")
            value = input("Enter the value: ")
            set_signal_value(data, signal_path, value)
            write_yaml(file_path, data)
            print(f"Set {signal_path} to {value}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()