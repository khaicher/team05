import csv
from pathlib import Path

def overheads_function():
    """
    - The purpose of this function is to identify the highest overhead expense 
    along with its corresponding percentage
    - No parameters needed
    """

    # Get respective csv file and append output to summary text
    fp_summary = Path.cwd() / "summary_report.txt"
    fp = Path.cwd() / "csv_reports" / "overheads.csv"
    fp_summary.touch()

    # Get respective data set from the csv file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

    # Assign default value to zero and create an empty list
        max_overheads = 0
        max_category = []

        for row in reader:
            # Assigns float value to overheads
            overheads = float(row[1])
            # Check if overheads is greater than max_overheads, if yes update max_overheads and max_category
            if overheads > max_overheads:
                max_overheads = overheads
                max_category = row[0]
    
    # open fp_summary file and append the values inside
    with fp_summary.open(mode="a", encoding="UTF-8", newline="") as file:   
        
        file.write(f"[HIGHEST OVERHEADS] {max_category}: {max_overheads}%")