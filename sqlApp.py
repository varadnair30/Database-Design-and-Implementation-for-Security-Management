import mysql.connector
from mysql.connector import Error
 
# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='academicmysql.mysql.database.azure.com',
    user='', #put_your_net_ID___vxn1475
    password='', #put_your_password___vnvarad30
    database='', #put_your_net_ID___vxn1475
    port=3306
)
 
# Function to execute a query
def execute_query(query, params=None):
    if params is None:
        params = []
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        # Fetch results only if the query is a SELECT statement
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            cursor.close()  # Close the cursor
            return results
        else:
            connection.commit()
            cursor.close()  # Close the cursor
            return None
    except Error as err:
        print(f"Error executing query: {err}")
        return None
 
def insert_relation_privilege():
    r_id = int(input("Enter relation privilege ID: "))
    privilege_name = input("Enter privilege name: ")
    privilege_desc = input("Enter privilege description: ")
    
    query = """
    INSERT INTO RELATION_PRIVILEGE (R_ID, PRIVILEGE_NAME, PRIVILEGE_DESC)
    VALUES (%s, %s, %s)
    """
    params = (r_id, privilege_name, privilege_desc)
    execute_query(query, params) 


# Function to preload data
def preload_data():
    user_accounts = [
        (1, 'A.Lice', '123-456-7890'),
        (2, 'B.Ob', '123-456-7891'),
        (3, 'C.Harlie', '123-456-7892'),
        (4, 'D.Avid', '123-456-7893'),
        (5, 'E.Mma', '123-456-7894'),
        (6, 'F.Iona', '123-456-7895'),
        (7, 'G.Eorge', '123-456-7896'),
        (8, 'H.Annah', '123-456-7897'),
        (9, 'I.An', '123-456-7898'),
        (10, 'J.Ane', '123-456-7899')
    ]
 
    roles = [
        ("Admin", 1, "Full access to all features"),
        ("Editor", 2, "Can edit records"),
        ("Viewer", 3, "Can view records only")
    ]
 
    account_privileges = [
        ("SELECT_PRIV", "Allows SELECT access", 1, "Admin"),
        ("INSERT_PRIV", "Allows INSERT access", 2, "Editor"),
        ("VIEW_PRIV", "Allows VIEW access", 3, "Viewer")
    ]
 
    relation_privileges = [
        (1, "TABLE_ACCESS", "Access to tables"),
        (2, "ROW_ACCESS", "Access to specific rows")
    ]
 
    tables = [
        ("TAB1", 1),
        ("TAB2", 2),
        ("TAB3", 3),
        ("TAB4", 4),
        ("TAB5", 5),
        ("TAB6", 6),
        ("TAB7", 7),
        ("TAB8", 8),
        ("TAB9", 9),
        ("TAB10", 10)
    ]
 
    has_relationships = [
        ("TAB1", "Admin", "TABLE_ACCESS", 1),
        ("TAB2", "Editor", "ROW_ACCESS", 2),
        ("TAB3", "Viewer", "TABLE_ACCESS", 1),
        ("TAB4", "Admin", "TABLE_ACCESS", 1),
        ("TAB5", "Editor", "ROW_ACCESS", 2),
        ("TAB6", "Viewer", "TABLE_ACCESS", 1),
        ("TAB7", "Admin", "TABLE_ACCESS", 1),
        ("TAB8", "Editor", "ROW_ACCESS", 2),
        ("TAB9", "Viewer", "TABLE_ACCESS", 1),
        ("TAB10", "Admin", "TABLE_ACCESS", 1)
    ]
 
    # Preload user accounts
    print("\nPreloading user accounts...")
    for account in user_accounts:
        execute_query("INSERT IGNORE INTO USER_ACCOUNT (IDNO, NAME, PHONE) VALUES (%s, %s, %s)", account)
 
    # Preload roles
    print("\nPreloading roles...")
    for role in roles:
        execute_query("INSERT IGNORE INTO USER_ROLE (RNAME, RACC_ID, DESCRIPTION) VALUES (%s, %s, %s)", role)
 
    # Preload account privileges
    print("\nPreloading account privileges...")
    for privilege in account_privileges:
        execute_query("INSERT IGNORE INTO ACCOUNT_PRIVILEGE (PRIVILEGENAME, PRIVILEGE_DESC, ACC_ID, RNAME) VALUES (%s, %s, %s, %s)", privilege)
 
    # Preload relation privileges
    print("\nPreloading relation privileges...")
    for relation in relation_privileges:
        execute_query("INSERT IGNORE INTO RELATION_PRIVILEGE (R_ID, PRIVILEGE_NAME, PRIVILEGE_DESC) VALUES (%s, %s, %s)", relation)
 
    # Preload tables
    print("\nPreloading tables...")
    for table in tables:
        execute_query("INSERT IGNORE INTO TABLES (T_NAME, O_ID) VALUES (%s, %s)", table)
 
    # Preload HAS relationships
    print("\nPreloading HAS relationships...")
    for rel in has_relationships:
        execute_query("INSERT IGNORE INTO HAS_PREDEFINED (T_NAME, RNAME, PRIVILEGE_NAME, R_ID) VALUES (%s, %s, %s, %s)", rel)
 
    print("Data preloaded successfully.")
 
# Display all user accounts
# Display all user accounts along with their account privilege, relation privilege, and predefined relationships
def display_all_users():
    query = """
    SELECT
        UA.IDNO,
        UA.NAME,
        UA.PHONE,
        UR.RNAME AS RoleName,
        AP.PRIVILEGENAME AS AccountPrivilege,
        RP.PRIVILEGE_NAME AS RelationPrivilege,
        HP.T_NAME AS HasPredefinedTable
    FROM
        USER_ACCOUNT UA
    LEFT JOIN
        USER_ROLE UR ON UA.IDNO = UR.RACC_ID
    LEFT JOIN
        ACCOUNT_PRIVILEGE AP ON UA.IDNO = AP.ACC_ID
    LEFT JOIN
        HAS_PREDEFINED HP ON UR.RNAME = HP.RNAME
    LEFT JOIN
        RELATION_PRIVILEGE RP ON HP.R_ID = RP.R_ID
    """
    results = execute_query(query)
    if results:
        print("\nUser Accounts with Privileges and Relationships:")
        for row in results:
            print(f"IDNO: {row[0]}, Name: {row[1]}, Phone: {row[2]}, "
                  f"Role: {row[3]}, Account Privilege: {row[4]}, "
                  f"Relation Privilege: {row[5]}, Table: {row[6]}")
    else:
        print("No user accounts found.")

def insert_account_privilege():
    privilege_name = input("Enter privilege name: ")
    privilege_desc = input("Enter privilege description: ")
    acc_id = int(input("Enter associated account ID: "))
    role_name = input("Enter role name: ")
    
    query = """
    INSERT INTO ACCOUNT_PRIVILEGE (PRIVILEGENAME, PRIVILEGE_DESC, ACC_ID, RNAME)
    VALUES (%s, %s, %s, %s)
    """
    params = (privilege_name, privilege_desc, acc_id, role_name)
    execute_query(query, params)  
 
def get_privileges_by_role():
    role_name = input("Enter role name: ")
    query = """
    SELECT 
        AP.PRIVILEGENAME AS AccountPrivilege,
        RP.PRIVILEGE_NAME AS RelationPrivilege
    FROM 
        USER_ROLE UR
    LEFT JOIN 
        ACCOUNT_PRIVILEGE AP ON UR.RNAME = AP.RNAME
    LEFT JOIN 
        HAS_PREDEFINED HP ON UR.RNAME = HP.RNAME
    LEFT JOIN 
        RELATION_PRIVILEGE RP ON HP.R_ID = RP.R_ID
    WHERE 
        UR.RNAME = %s;
    """
    results = execute_query(query, (role_name,))
    print(f"\nPrivileges for Role '{role_name}':")
    if results:
        for row in results:
            print(f"Account Privilege: {row[0]}, Relation Privilege: {row[1]}")
    else:
        print("No privileges found for this role.")

# Function to retrieve all privileges associated with a particular user account
def get_privileges_by_user_account():
    idno = int(input("Enter user account ID: "))
    query = """
    SELECT 
        AP.PRIVILEGENAME AS AccountPrivilege,
        RP.PRIVILEGE_NAME AS RelationPrivilege
    FROM 
        USER_ACCOUNT UA
    LEFT JOIN 
        USER_ROLE UR ON UA.IDNO = UR.RACC_ID
    LEFT JOIN 
        ACCOUNT_PRIVILEGE AP ON UR.RNAME = AP.RNAME
    LEFT JOIN 
        HAS_PREDEFINED HP ON UR.RNAME = HP.RNAME
    LEFT JOIN 
        RELATION_PRIVILEGE RP ON HP.R_ID = RP.R_ID
    WHERE 
        UA.IDNO = %s;
    """
    results = execute_query(query, (idno,))
    print(f"\nPrivileges for User Account ID '{idno}':")
    if results:
        for row in results:
            print(f"Account Privilege: {row[0]}, Relation Privilege: {row[1]}")
    else:
        print("No privileges found for this user account.")

# Function to check if a specific privilege is granted to a user account
def is_privilege_granted_to_user():
    idno = int(input("Enter user account ID: "))
    privilege_name = input("Enter privilege name: ")
    query = """
    SELECT 
        COUNT(*) > 0 AS IsPrivilegeGranted
    FROM 
        USER_ACCOUNT UA
    JOIN 
        USER_ROLE UR ON UA.IDNO = UR.RACC_ID
    JOIN 
        ACCOUNT_PRIVILEGE AP ON UR.RNAME = AP.RNAME
    WHERE 
        UA.IDNO = %s AND AP.PRIVILEGENAME = %s;
    """
    result = execute_query(query, (idno, privilege_name))
    is_granted = result[0][0] if result else False
    print(f"\nIs Privilege '{privilege_name}' granted to User Account ID '{idno}': {is_granted}")



# Menu interface
def show_menu():
    print("\nMenu:")
    print("1. Add User Account")
    print("2. Add Role")
    print("3. Add Table")
    print("4. Add HAS Relationship")
    print("5. Display All Users")
    print("6. Preload Data")
    print("7. Insert New Relation Privilege")
    print("8. Insert New Account Privilege")
    print("9. Retrieve Privileges by Role")
    print("10. Retrieve Privileges by User Account")
    print("11. Check If Privilege is Granted to User")
    print("12. Exit")
    choice = input("Enter your choice: ")
    return choice
 
# Main function
def main():
    while True:
        choice = show_menu()
        if choice == "1":
            idno = input("Enter user ID: ")
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            execute_query("INSERT INTO USER_ACCOUNT (IDNO, NAME, PHONE) VALUES (%s, %s, %s)", (idno, name, phone))
            print("User account added successfully.")
        elif choice == "2":
            rname = input("Enter role name: ")
            racc_id = input("Enter associated user ID: ")
            description = input("Enter role description: ")
            execute_query("INSERT INTO USER_ROLE (RNAME, RACC_ID, DESCRIPTION) VALUES (%s, %s, %s)", (rname, racc_id, description))
            print("Role added successfully.")
        elif choice == "3":
            tname = input("Enter table name: ")
            o_id = input("Enter owner ID: ")
            execute_query("INSERT INTO TABLES (T_NAME, O_ID) VALUES (%s, %s)", (tname, o_id))
            print("Table added successfully.")
        elif choice == "4":
            tname = input("Enter table name: ")
            rname = input("Enter role name: ")
            privilege_name = input("Enter relation privilege name: ")
            r_id = input("Enter relation privilege ID: ")
            execute_query("INSERT INTO HAS_PREDEFINED (T_NAME, RNAME, PRIVILEGE_NAME, R_ID) VALUES (%s, %s, %s, %s)", (tname, rname, privilege_name, r_id))
            print("HAS relationship added successfully.")
        elif choice == "5":
            display_all_users()
        elif choice == "6":
            preload_data()
        elif choice == "7":  
            insert_relation_privilege()
        elif choice == "8":  
            insert_account_privilege()
        elif choice == "9":
            get_privileges_by_role()
        elif choice == "10":
            get_privileges_by_user_account()
        elif choice == "11":
            is_privilege_granted_to_user()
        elif choice == "12":
            print("Exiting...")
            connection.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    try:
        main()
    except Error as err:
        print(f"Unexpected error: {err}")
        connection.close()
 
 