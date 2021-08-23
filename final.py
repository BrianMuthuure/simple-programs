

# gather input from user and put it into a list
def getRainFall():
    rain = []
    for i in range(1, 13):
        # program will not run if a number is not inputted, also prevents errors in the rest of the program
        while True:
            try:
                amount = float(input('Input Rainfall = '))
                print("    Rainfall for Month", i, "=", amount)
                rain.append(amount)
            except ValueError:
                print("Invalid Entry")
            else:
                break
    return rain


# calculate the sume of the user input
def calculate_total_rainfall(rainfall):
    x = 0
    for i in range(len(rainfall)):
        y = float(rainfall[i])
        x += y
    return (x)


# calculate the average of the user input
def calculate_avg_rainfall(rainfall):
    x = 0
    for i in range(len(rainfall)):
        y = float(rainfall[i])
        x += y
    return (x / 12)


# calls all functions and displays the max and min of the list
def main():
    print("Input Total Rainfall For 12 months (Inches)")
    print()
    rainfall = getRainFall()
    print()
    print("Total Rainfall for 12 months: ", "{:.2f}".format(calculate_total_rainfall(rainfall)))
    print()
    print("Average Rainfall for 12 months: ", "{:.2f}".format(calculate_avg_rainfall(rainfall)))
    print()
    print("Lowest Amount of rainfall for one month: ", "{:.2f}".format(min(rainfall)))
    print()
    print("Highest Amount of rainfall for one month: ", "{:.2f}".format(max(rainfall)))


# calls the main function
if __name__ == "__main__":
    main()
