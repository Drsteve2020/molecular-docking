import os

def create_project_structure():
    # Define base directory
    base_dir = r"c:\Users\PC\Documents\New Bioinformatics"
    
    # Define directories to create
    directories = [
        'src',
        'data',
        'tests',
        'docs',
        'notebooks'
    ]
    
    # Create directories
    for dir_name in directories:
        dir_path = os.path.join(base_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")

if __name__ == "__main__":
    create_project_structure()