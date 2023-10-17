import os
from bottle import Bottle, route, run, template

app = Bottle()

# Define the directory you want to list files from.
base_dir = "/home/rishi/Downloads"

@app.route('/')
def list_files():
    try:
        # List all files in the specified directory with their sizes.
        files = os.listdir(base_dir)
        file_list = []

        for file in files:
            file_path = os.path.join(base_dir, file)
            file_size = os.path.getsize(file_path)
            file_list.append((file, file_size))

        return template('index', file_list=file_list)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    run(app, host='localhost', port=8081)