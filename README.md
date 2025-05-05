# Matrix Multiplication Web App

A web app that performs n x n matrix multiplication using a C backend with optional OpenMP parallelization. Built with AngularJS for the frontend and Flask for the backend.

## Prerequisites
- Docker

## Build and Run
1. Build the Docker image:
   ```bash
   docker build -t matrix-app .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 matrix-app
   ```
3. Access the app at `http://localhost:5000`.

## Usage
- Enter the matrix size (n) for n x n matrices.
- Toggle "Use OpenMP" to enable/disable parallelization.
- Click "Calculate" to perform multiplication and view execution time.

## File Structure
```
matrix-app/
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── backend/
│   ├── matrix.c
│   ├── matrix_module.c
│   ├── server.py
│   ├── setup.py
│   └── requirements.txt
├── Dockerfile
└── README.md
```

## File Descriptions
- **frontend/index.html**: The main HTML file for the AngularJS frontend. Defines the structure of the web page, including input fields for matrix size, an OpenMP toggle, and a submit button.
- **frontend/app.js**: AngularJS script that handles the frontend logic. Manages user input, sends HTTP requests to the backend, and displays the execution time or errors.
- **frontend/styles.css**: CSS file for styling the frontend, ensuring a clean and responsive user interface.
- **backend/matrix.c**: C code implementing the matrix multiplication logic. Supports optional OpenMP parallelization for performance optimization.
- **backend/matrix_module.c**: C code that creates a Python extension module, allowing the Flask backend to call the matrix multiplication function.
- **backend/server.py**: Flask server script that serves the frontend files and handles the `/calculate` endpoint to process matrix multiplication requests.
- **backend/setup.py**: Python script to build the C extension module with OpenMP support.
- **backend/requirements.txt**: Lists Python dependencies (Flask) required for the backend.
- **Dockerfile**: Defines the Docker image build process, including installing dependencies, building the C extension, and running the Flask server.
- **README.md**: This file, providing an overview of the project, setup instructions, usage guide, file structure, and file descriptions.

## Notes
- Matrices are populated with random integers (0-9).
- Execution time is measured in seconds.
- OpenMP requires a compatible system (e.g., Linux with libomp).