import csv
from prettytable import PrettyTable
from collections import defaultdict
from datetime import datetime

def User_logon_Host(file_Name, user_column, device_column, date_column):   # Specify the filename and parameters you want to analyze.
    user_login_data = defaultdict(int)     # Store the login data using the defaultdict subclass with default values of 0

    with open(file_Name, 'r') as csv_file:    # Open and read the csv file
        csv_file_reader = csv.DictReader(csv_file)  # Reads each row of the csv file as a dictionary. With each column header as a key and the corresponding value in that column of that row as a value.
        for row in csv_file_reader:       # iterate through each row in the csv file and extract  the values from the specified columns (user_column, device_column, and date_column)
            Users = row[user_column]
            Device = row[device_column]
            Date = row[date_column]

            date = datetime.strptime(Date, '%Y-%m-%d %H:%M:%S:%f')  # convert the Date column strings to a datetime object.
            day = date.strftime('%d-%m,%a')   # creates a formatted string for the date object according to specified format. (Get the day name from the date)
            user_login_data[(Users, Device, day)] += 1   # uses the (Users, Device, day) tuple as key to access the corresponding login count in the user_login_data defaultdict. If the key exist in the user_login_data, the count increments by 1 and 0 is it doesn't.

    User_table = PrettyTable()   # Initialize the User_table object.
    User_table.field_names = ['User', 'Device', 'Day', 'Login Count']  # Set the required field names for the columns on the table

    sorted_users = sorted(user_login_data.items())   # Sort the items

    for (Users, Device, day), count in sorted_users:   # Iterate through the items in the sorted_user's dictionary
        User_table.add_row([Users, Device, day, count])  # For each tuple (user, device, day) and its corresponding count, a new row is added to the PrettyTable.
    print(User_table)

filename = input("Enter name of the csv file: ")
file_Name = f'/home/kali/Desktop/{filename}.csv'
user_column = 'DestinationAccount'
device_column = 'DestinationMachine'
date_column = 'DetectionTime'


User_logon_Host(file_Name, user_column, device_column, date_column)



