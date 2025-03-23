# 🏥 Health Data Insights  

## 📌 Overview  
**Health Data Insights** is a data analysis and cleansing application focused on extracting and transforming epidemiological data. The project automates data loading, filtering, and processing, ensuring an efficient pipeline for data exploration.  

## 🚀 Features  
✅ **Data Loading**: Imports raw CSV files for analysis.  
✅ **Data Cleaning & Standardization**: Performs value mapping, column renaming, and data preprocessing.  
✅ **Intelligent Filtering**: Selects only relevant data for analysis.  
✅ **Automated Export**: Generates processed CSV files ready for visualization and modeling.  

## Folder Structure

The project follows the structure below:

![Project Architecture](https://i.imgur.com/Pygo1Ui.png)

## 📂 Description of the Folders

- **`data/`**: Contains the datasets used in the project. It is subdivided into:
  - **`raw/`**: Stores the original datasets before any modification.
  - **`processed/`**: Stores the cleaned and processed datasets, ready for analysis.

- **`src/`**: The main source code of the project, responsible for loading, cleaning, and processing data. It includes:
  - **`maps/`**: Contains mappings for value standardization and column renaming.
    - **`__init__.py`**: Marks the directory as a package for easy imports.
    - **`value_maps.py`**: Stores dictionaries for mapping categorical values.
  - **`__init__.py`**: Initializes the `src/` package.
  - **`analysis.py`**: The main script responsible for analyzing the processed data.
  - **`data_cleaner.py`**: Handles data cleaning and transformation tasks.
  - **`data_loader.py`**: Loads raw CSV files into DataFrames.
  - **`data_selector.py`**: Selects relevant columns for analysis.

- **`main.py`**: The entry point of the project. It runs the full data pipeline, including loading, cleaning, selecting, and saving processed data.

- **`.gitignore`**: Specifies files and directories that should be ignored by Git.

- **`LICENSE`**: The project license file.

- **`README.md`**: Documentation for the project.

- **`requirements.txt`**: Contains the list of dependencies needed to run the project.

## 🚀 Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Health_Data_Insights.git
   cd Health_Data_Insights

2. Create and activate a virtual environment:
- On Windows (PowerShell):
  ```bash
  python -m venv venv
  venv/Scripts/activate
- On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate

3. Install dependencies:
  ```bash
  pip install -r requirements.txt

## ⚒️ Usage

1. After setting up the environment and installing dependencies, run the project with:
  ```bash
  python src/analysis.py```

This will execute the data processing pipeline, including loading, cleaning and analyzing the dataset

## 📊 Project Structure

The project is structured into different modules to keep the code organized and maintainable. Refer to the folder descriptions above for more details.

## ✅ Features

- Load and preprocess raw data.
- Select relevant columns for analysis.
- Clean and transform categorical values.
- Save processed data for further insights.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

## 📜 License

This project is licensed under the MIT License - see the [MIT License](./LICENSE) file for details.

## 📩 Contact

For questions or seggestions, reach out via?
- Email: pedrodutra@infoservicetechnology.com.br
- LinkedIn: https://www.linkedin.com/in/pedro-paulo-dutra-a62365184/
- GitHub: https://github.com/PedroDutra86