# Encephalo Investments Coding Pre-Test - main.py
import pandas as pd

def main():
    # main function.
    # Return the top 10 companies with the highest market cap.
    data = pd.read_csv("./data.csv") # read csv using pandas 
    
    # Found Market Cap column, replaced '$' with empty space, and dropped 'N/A' indicies
    # replaced 'M' 'B' with appropriate values and represented it as a number, and found 
    # the 10 largest market caps

    market_cap = data['market_cap'].str.replace(r'$', '').dropna()
    print(market_cap.replace({'M': '*1e6', 'B': '*1e9'}, regex=True).map(pd.eval).nlargest(10))

if __name__ == "__main__":
    main()
