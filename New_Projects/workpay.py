import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('workpay.db')
c = conn.cursor()

# Create the work_log table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS work_log (
             id INTEGER PRIMARY KEY,
             date TEXT,
             normal_hours REAL,
             overtime_hours REAL,
             normal_pay REAL,
             overtime_pay REAL,
             total_pay REAL,
             taxes_paid REAL,
             tax_rate REAL,
             net_pay REAL
             )''')
conn.commit()

def calculate_tax_rate(total_pay, taxes_paid):
    if total_pay == 0:
        return 0
    return round((taxes_paid / total_pay) * 100, 2)

def insert_data():
    normal_rate = 16.50
    overtime_rate = 24.75

    date = input("Enter the date of the paycheck (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    normal_hours = round(float(input("Enter the number of normal hours worked: ")), 2)
    overtime_hours = round(float(input("Enter the number of overtime hours worked: ")), 2)
    taxes_paid = round(float(input("Enter the total taxes paid: ")), 2)

    normal_pay = round(normal_hours * normal_rate, 2)
    overtime_pay = round(overtime_hours * overtime_rate, 2)
    total_pay = round(normal_pay + overtime_pay, 2)
    net_pay = round(total_pay - taxes_paid, 2)

    tax_rate = calculate_tax_rate(total_pay, taxes_paid)

    c.execute('''INSERT INTO work_log (date, normal_hours, overtime_hours, normal_pay, overtime_pay, 
                total_pay, taxes_paid, tax_rate, net_pay) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (date, normal_hours, overtime_hours, normal_pay, overtime_pay, 
               total_pay, taxes_paid, tax_rate, net_pay))
    conn.commit()

    print("Data inserted successfully.")

def view_data():
    print("View options:")
    print("1. All-time")
    print("2. By month")
    print("3. By year")
    choice = input("Choose an option: ")

    if choice == '1':
        query = "SELECT * FROM work_log ORDER BY date ASC"
        c.execute(query)
    elif choice == '2':
        c.execute("SELECT DISTINCT strftime('%m', date) FROM work_log ORDER BY strftime('%m', date) ASC")
        months = c.fetchall()
        month_map = {
            "01": "January", "02": "February", "03": "March", "04": "April", 
            "05": "May", "06": "June", "07": "July", "08": "August", 
            "09": "September", "10": "October", "11": "November", "12": "December"
        }
        print("Available months:")
        for month in months:
            month_num = month[0]
            print(f"{month_num} - {month_map[month_num]}")
        selected_month = input("Enter the month (number): ")
        query = "SELECT * FROM work_log WHERE strftime('%m', date) = ? ORDER BY date ASC"
        c.execute(query, (selected_month,))
    elif choice == '3':
        c.execute("SELECT DISTINCT strftime('%Y', date) FROM work_log ORDER BY strftime('%Y', date) ASC")
        years = c.fetchall()
        print("Available years:")
        for year in years:
            print(year[0])
        selected_year = input("Enter the year: ")
        query = "SELECT * FROM work_log WHERE strftime('%Y', date) = ? ORDER BY date ASC"
        c.execute(query, (selected_year,))
    else:
        print("Invalid choice. Please try again.")
        return

    rows = c.fetchall()
    
    if rows:
        print("-" * 118) 
        print("Date       | Normal Hours | Overtime Hours | Normal Pay | Overtime Pay | Total Pay | Taxes Paid | Tax Rate  | Net Pay")
        print("-" * 118)

        total_normal_hours = 0
        total_overtime_hours = 0
        total_normal_pay = 0
        total_overtime_pay = 0
        total_pay = 0
        total_taxes_paid = 0
        total_net_pay = 0
        total_tax_rate = 0

        for row in rows:
            total_normal_hours += row[2]
            total_overtime_hours += row[3]
            total_normal_pay += row[4]
            total_overtime_pay += row[5]
            total_pay += row[6]
            total_taxes_paid += row[7]
            total_net_pay += row[9]
            total_tax_rate += row[8]

            print(f"{row[1]:<10} | {row[2]:<12.2f} | {row[3]:<14.2f} | {row[4]:<10.2f} | {row[5]:<12.2f} | {row[6]:<9.2f} | {row[7]:<10.2f} | {row[8]:<8.2f}% | {row[9]:<8.2f}")

        average_tax_rate = total_tax_rate / len(rows)

        print("-" * 118)
        print(f"{'TOTALS':<10} | {total_normal_hours:<12.2f} | {total_overtime_hours:<14.2f} | {total_normal_pay:<10.2f} | {total_overtime_pay:<12.2f} | {total_pay:<9.2f} | {total_taxes_paid:<10.2f} | {average_tax_rate:<8.2f}% | {total_net_pay:<8.2f}")
        print("-" * 118)
    else:
        print("No data found.")

def main():
    while True:
        print("\n1. Insert work log data")
        print("2. View work log data")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

conn.close()
