# <img src="https://i.imgur.com/gl5r9LJ.png" alt="Logo" width="30" style="margin-right: 8px; vertical-align: middle;"/> HDI - Disease Tracker 

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

## 📌 Overview  
**HDI's Disease Tracker** is an application designed to collect raw parquet files, load them, select relevant tables, clean, and convert them into new translated parquet files. The application is developed for use by Health Data Insights and serves as the foundation for the [HDI - Disease Tracker API](https://github.com/PedroDutra86/hdi-disease-tracker-api)

## 🚀 Features  
- 📁 **Raw Data Loading:** Reads previously extracted Parquet files that must be manually placed in the `data/raw` folder.
- 🧼 **Data Cleaning:** Standardizes column names and values to ensure consistency.
- 🔎 **Column Selection:** Keeps only the fields relevant to epidemiological analysis.
- 🌍 **Location Mapping:** Adds region and municipality information based on IBGE tables.
- 🏥 **Healthcare Facility Mapping:** Integrates CNES codes to retrieve hospital names and locations.
- 📤 **Data Export:** Generates clean, translated Parquet files ready for use.
- 🔄 **Modular Pipeline:** Structured in reusable modules for loading, cleaning, selecting, and exporting data.
- 🧪 **API-Ready:** Serves as a data foundation for the HDI Disease Tracker API.

## Folder Structure

The project follows the structure below:

```bash
hdi-disease-tracker/
├── data/                              # Main data directory
│   ├── raw/                           # Stores raw (.parquet) files to be processed
│   └── processed/                     # Stores cleaned and transformed files
├── src/                               # Source code for the data pipeline
│   ├── maps/                          # Value mappings for standardization
│   │   ├── __init__.py                # Marks the directory as a Python package
│   │   ├── value_maps.py              # Contains dictionaries for value normalization
│   │   └── municipes_cnes_map.py      # Maps municipality names to CNES codes
│   ├── __init__.py                    # Initializes the `src` package
│   ├── data_cleaner.py                # Cleans and standardizes the dataset
│   ├── data_loader.py                 # Loads raw parquet files into DataFrames
│   ├── data_selector.py               # Selects relevant columns for analysis
│   └── data_converter.py              # Converts and saves final parquet output
├── main.py                            # Entry point script to run the pipeline
├── .gitignore                         # Specifies files/folders ignored by Git
├── LICENSE                            # Project license file
├── README.md                          # Project documentation
└── requirements.txt                   # Python dependencies
```

## 🚀 Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PedroDutra86/hdi-disease-tracker.git
   cd hdi-disease-tracker

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
  ```

## ⚒️ Usage

1. After setting up the environment and installing dependencies, run the project with:
  ```bash
  python src/data_converter.py
  ```

This will execute the full processing pipeline, including loading the data, selecting relevant columns, cleaning and translating information, and generating a new output file.

## 📜 License

This project is licensed under the MIT License - see the [MIT License](./LICENSE) file for details.

## 📩 Contact

For questions or suggestions, reach out via:
- Email: pedrodutra@infoservicetechnology.com.br
- LinkedIn: https://www.linkedin.com/in/pedro-paulo-dutra-a62365184/
- GitHub: https://github.com/PedroDutra86
- Portfolio: https://portfolio-pedrodutra.vercel.app