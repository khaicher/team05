import csv
from pathlib import Path

def cash_on_hand_function():
    """
    - This function identifies dataset trends (increase, decrease, or fluctuation) and 
    calculates the highest increment or decrement. 
    - In fluctuating datasets, it lists days and deficit amounts, 
    highlighting the top 3 deficits with their occurrence days.
    - No parameters needed
    """

    # Get respective csv file and append output to summary text
    fp_summary = Path.cwd() / "summary_report.txt"
    fp = Path.cwd() / "csv_reports" / "cash-on-hand.csv"
    fp_summary.touch()

    # Get respective data set from the csv file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        # Create two empty list 
        cash_on_hand = []
        deficit_days = []

        # Append data from the csv file to empty list
        for row in reader:
            cash_on_hand.append([int(row[0]), float(row[1])])

        # Initialize with the first deficit amount and its day
        max_amount = cash_on_hand[1][1] - cash_on_hand[0][1]
        max_day = cash_on_hand[1][0]

        # Initialise decreasing and increasing variable
        decreasing = False 
        increasing = False 

        # Iterates through the range of data in list 
        # and assign profit of current and previous day
        for days in range(1, len(cash_on_hand)):
            current_cash = cash_on_hand[days][1]
            prev_cash = cash_on_hand[days - 1][1]
            
            # Assign difference in value
            difference_in_cash = current_cash - prev_cash

            # Append respective day and amount to list
            deficit_days.append([cash_on_hand[days][0], difference_in_cash])
            
            # Identify if the data set is always increasing or decreasing
            # and assign the repective amount and day
            if difference_in_cash > 0:
                increasing = True
                if max_amount < difference_in_cash:
                    max_day = cash_on_hand[days][0]
                    max_amount = difference_in_cash
            else:
                decreasing = True
                if max_amount > difference_in_cash:
                    max_day = cash_on_hand[days][0]
                    max_amount = difference_in_cash

    # Open fp_summary and append 
    with fp_summary.open(mode="a", encoding="UTF-8", newline="") as file:

    # Append what to print in fp_summary for always increasing or decreasing data set
        if increasing and not decreasing:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            file.write(f"[HIGHEST CASH SURPLUS] DAY:{max_day}, AMOUNT:${max_amount}")
        elif decreasing and not increasing:
            file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
            file.write(f"[HIGHEST CASH DEFICIT] DAY:{max_day}, AMOUNT:${abs(max_amount)}")

    # For fluctuating data set
        else:
            #if difference_amount > 0:
            top_deficits = [[0, 0] for days in range(3)]  

    # Write list of days with deficit amount
            for days in range(len(deficit_days)):              

                if deficit_days[days][1] < 0:
                    file.write(f"\n[CASH DEFICIT] DAY:{deficit_days[days][0]}, AMOUNT:${deficit_days[days][1]*-1}")

    # Find out top three decifit amounts and days
                    for cash in range(3):
                        if deficit_days[days][1] < top_deficits[cash][1]:
                            top_deficits.insert(cash, (deficit_days[days][0], deficit_days[days][1]))
                            top_deficits.pop()
                            break

    # Assign the respective label to the amount and day
            for highest in range(3): 
                day, deficit = top_deficits[highest] 
                if deficit < 0:  # Ensure it's a deficit
                    if highest == 0:
                        label = "[HIGHEST CASH DEFICIT]"
                    elif highest == 1:
                        label = "[2ND HIGHEST CASH DEFICIT]"
                    elif highest == 2:
                        label = "[3RD HIGHEST CASH DEFICIT]"

                file.write(f"\n{label} DAY: {day}, AMOUNT: ${abs(deficit)}")                            


