# Ethical Priorities in Danish Healthcare AI Policy


This repository contains the code for the quantitative analysis and visualization for the paper _Ethics in Danish Healthcare AI Policy: A Document Analysis_ by Victor Vadmand Jensen (owner of this repository), Marianne Johansson Jørgensen, Rikke Hagensby Jensen, Jeppe Lange, Jan Wolff, and Mette Terp Høybye.
The paper is available as a preprint, though the statistical analysis in the repository has been updated from what is available in the preprint.
The paper is currently under review in the International Journal of Medical Informatics.

## Running the analysis
To run the analysis, you must:
* Create and activate the virtual environment of the project. To create the virtual environment, use the command *python -m venv* followed by the project folder's source location. Then, use the command _venv\Scripts\Activate.ps1_ in the terminal to activate the virtual environment. Note that depending on if your machine has certain restrictions from, e.g., your employer, you might need to _set-ExecutionPolicy_ to allow for the activiation of the virtual environment.
* Install the project dependencies listed in the requirements.txt file. You can do this with the command _pip install requirements.txt_ in the terminal.
* Add a file called _config.py_ in the project folder. This file must have the variable *file_path*, which must point to a _.xlsx_ file on your machine, as well as the variable _sheet_, which must point to the sheet of the _.xlsx_ file you are interested in analyzing. The sheet should have the same structure as the data extraction table provided in the paper's supplementary materials, and rows must be individual documents. Note that the cells for question A will be encoded as binary values, so the values for each document in the question A columns must be either text or empty.
* Run the *quantitative_analysis.py* script with the command *python -m quantitative_analysis.py*. This will first load and transform the data with *pandas*, calculate descriptive statistics with *pandas*, as well perform hypothesis testing with *statsmodels* and effect size calculations with *stikpetP* for each parts of question A. These are saved as a JSON file. Then, the data will be visualized with *matplotlib*.
* The calculations are saved in readable format in the JSON file *results.json* with a timestamp for time of running the analysis. The visualizations are saved as three separate PDF files.

## Citation
Cite the preprint as follows: 

*Jensen, Victor Vadmand and Jørgensen, Marianne Johansson and Jensen, Rikke Hagensby and Lange, Jeppe and Wolff, Jan and Høybye, Mette Terp, Ethics in Danish Healthcare Ai Policy: A Document Analysis. Available at SSRN: https://ssrn.com/abstract=5248408 or http://dx.doi.org/10.2139/ssrn.5248408* 
