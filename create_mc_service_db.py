import sqlite3

# Create a connection to an SQLite database
conn = sqlite3.connect('mc_service.db')

# Create a cursor object to run SQL commands
cur = conn.cursor()

# Create tables
cur.execute('''CREATE TABLE Customers (
                    customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    First_name VARCHAR NOT NULL,
                    Last_name VARCHAR NOT NULL,
                    email VARCHAR NOT NULL,
                    Phone_Number VARCHAR,
                    address TEXT,
                    MC_ID INTEGER,
                    FOREIGN KEY (MC_ID) REFERENCES Motorcycle(MC_ID)
                )''')

cur.execute('''CREATE TABLE MC (
                    MC_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Brand VARCHAR NOT NULL,
                    Model VARCHAR NOT NULL,
                    Years VARCHAR,
                    VIN VARCHAR, 
                    Reg_Number VARCHAR,
                    Customer_ID INTEGER,
                    FOREIGN KEY (Customer_ID) REFERENCES Customers(customer_ID)
                )''')

cur.execute('''CREATE TABLE svc_dept_staff (
                    Staff_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name VARCHAR NOT NULL,
                    Role VARCHAR,
                    Contact_Details VARCHAR,
                    Avail VARCHAR
                )''')

cur.execute('''CREATE TABLE Services (
                    Service_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Service_type VARCHAR NOT NULL,
                    Service_description TEXT,
                    Time_dur INTEGER,
                    Amount DECIMAL,
                    MC_ID INTEGER,
                    FOREIGN KEY (MC_ID) REFERENCES Motorcycle(MC_ID)
                )''')

cur.execute('''CREATE TABLE Bookings (
                    Booking_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Customer_ID INTEGER,
                    MC_ID INTEGER,
                    Service_ID INTEGER,
                    Date DATE,               
                    Time_slot TIME,
                    Status VARCHAR,
                    FOREIGN KEY (Customer_ID) REFERENCES Customers(customer_ID),
                    FOREIGN KEY (MC_ID) REFERENCES Motorcycle(MC_ID),
                    FOREIGN KEY (Service_ID) REFERENCES Services(Service_ID)
                )''')

cur.execute('''CREATE TABLE Payment (
                    Payment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Booking_ID INTEGER,
                    Amount DECIMAL,
                    Payment_Method VARCHAR,
                    Payment_Date DATE,
                    Payment_time TIME,
                    FOREIGN KEY (Booking_ID) REFERENCES Bookings(Booking_ID)
                )''')

cur.execute('''CREATE TABLE Comm_Log (
                    Log_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Booking_ID INTEGER,
                    Customer_ID INTEGER,
                    Date DATE,
                    Time TIME,
                    Communication_Details TEXT,
                    Staff_ID VARCHAR,
                    FOREIGN KEY (Booking_ID) REFERENCES Bookings(Booking_ID),
                    FOREIGN KEY (Customer_ID) REFERENCES Customers(customer_ID)
                )''')
cur.execute('''CREATE TABLE Parts_orders (
                    Order_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Booking_ID INTEGER,
                    Part_Name VARCHAR,
                    Part_Namber INTEGER,
                    Part_Quantity INTEGER,
                    PRISE FLOT,
                    SUPPLIER_ID VARCHAR,
                    Date_Added DATE,
                    Order_Status STRING,            
                    FOREIGN KEY (Booking_ID) REFERENCES Bookings(Booking_ID)
                )''')


# Spara (commit) ändringar och stäng anslutningen
conn.commit()


print("Database and tables created successfully.")
