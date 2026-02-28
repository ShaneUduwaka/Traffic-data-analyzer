# Traffic-data-analyzer

A Python command-line application for processing traffic survey CSV data, generating statistical insights, and visualizing vehicle frequency per hour using graphical histograms.

## Features

* Validates user input for survey date with proper error handling
* Processes traffic survey CSV files for selected dates
* Calculates key traffic statistics, including:

  * Total vehicles
  * Trucks and electric vehicles
  * Two-wheeled vehicles
  * Speed limit violations
  * Hourly traffic frequency
* Displays results clearly in the command-line interface
* Saves processed results to a text file (`results.txt`)
* Generates graphical histograms to visualize hourly vehicle distribution
* Supports processing multiple datasets in a single session

## Requirements

* Python 3.x
* `graphics.py` library (included or installed)

## How to Run

1. Place the traffic CSV files in the project directory
   Example file format:

   ```
   traffic_dataDDMMYYYY.csv
   ```

2. Open Command Prompt or Terminal and navigate to the project folder

3. Run the program:

   ```
   python traffic.py
   ```

4. Enter the survey date when prompted to process and visualize the data

## Output

* Traffic statistics displayed in the command-line interface
* Results saved automatically to:

  * `results.txt`
* Histogram visualization displayed in a graphical window

## Project Purpose

This project demonstrates file handling, data processing, input validation, and graphical data visualization using Python.
