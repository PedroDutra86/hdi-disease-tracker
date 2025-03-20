## Folder Structure

The project follows the structure below:

project/
│── venv/                  <!-- Python Virtual Environment --> 
│── data/                  <!-- Stores CSV files and other datasets  -->
│   ├── raw/               <!-- Raw, unprocessed data -->
│   ├── processed/         <!-- Processed data, cleaned and ready for analysis -->
│── src/                   <!-- Main source code -->
│   ├── __init__.py        <!-- Initializes the src package -->
│   ├── data_loader.py     <!-- Functions to load CSV files -->
│   ├── data_cleaner.py    <!-- Functions for data cleaning -->
│   ├── analysis.py        <!-- Code for data analysis -->
│── main.py                <!-- Main file that runs the project -->
│── requirements.txt       <!-- Project dependencies -->
│── README.md              <!-- Project documentation -->

## Description of the folders:

- **`venv/`**: This folder contains the virtual environment for the project, which isolates the dependencies required by the project.
- **`data/`**: The `data/` folder contains the datasets used in the project. It is subdivided into:
  - **`raw/`**: Contains the original datasets that are not modified.
  - **`processed/`**: Contains the cleaned and processed datasets ready for analysis.
- **`src/`**: This is where the main code for the project resides. It includes:
  - **`__init__.py`**: This file marks the `src/` directory as a Python package and allows importing functions from it.
  - **`data_loader.py`**: A script containing functions to load raw CSV files into the project.
  - **`data_cleaner.py`**: A script for cleaning and preprocessing the data.
  - **`analysis.py`**: A script for performing the analysis on the processed data.
- **`main.py`**: This is the entry point for the project. It will run the entire pipeline.
