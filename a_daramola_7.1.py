#Akinola Daramola Jr
#Programming Exercise: 7.1
#Due Date: 07/31/2022

"""
Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week.
The amounts should be stored in a list.
Use a loop to calculate the total sales for the week and display the result.
"""

#Define main() function to call weeklySales()
def main():

    #Invoke weeklySales() function
    weeklySales()

#Define weeklySales() function
def weeklySales():

    #Create list element of seven days
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #Initialize list variable
    sales = []

    #Initializing total sales variable
    total_sales = 0

    #Loop through days of week
    for day in week:

        #Prompt user to enter store sales for each day
        sales_eachday = float(input(f"Enter store sales for {day}. "))

        #Append sales to list
        sales.append(sales_eachday)

        #Calculate total Sales
        total_sales += sales_eachday

    #Display total sales for week
    print(f"Total Sales: ${total_sales:,.2f}")

#Invoke mian() function to start program
main()
