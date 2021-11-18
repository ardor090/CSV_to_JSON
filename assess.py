import csv
import json
 
 
# a function to import the data from csv - json)
# takes two argument which eventually will be our csv source and json output.
def convert_json(csvFile, jsonFile):
 
    data = {}                                           # an empty dictionary that eventually will be populated 
 
    with open(csvFile, 'r') as csvf:                    # this block of code imports the contents of the csv file into our program
        csvReader = csv.DictReader(csvf)
 
        for i, row in enumerate (csvReader):            # our loop that makes every key a number to eliminate the possibilty
                                                        # that two identical last names gets overwritten
            details = {

                
                "first_name": row["First Name"],        # our pre-defined keys and structure of the dictionary
                "second_name": row["Last Name"],
                "age": row["Age (Years)"],
                "sex": row["Sex"],
                "retired": bool(row["Retired"]),
                "marital_status": row["Marital Status"],
                "dependents": row["Dependants"],
                "salary": row["Yearly Salary (£)"],
                "pension": row["Yearly Pension (£)"],
                "company": row["Employer Company"],
                "commute_distance": row["Distance Commuted to Work (miles)"],
                "Address": {
                    "street": row["Address Street"],
                    "city": row["Address City"],
                    "postcode": row["Address Postcode"],
                },
                "Credit Card": {
                    "start_date": row["Credit Card Start Date"],
                    "end_date": row["Credit Card Expiry Date"],
                    "number": row["Credit Card Number"],
                    "ccv": row["Credit Card CVV"],
                    "iban": row["Bank IBAN"]
                },
                "Vehicle": {
                    "make": row["Vehicle Make"],
                    "model": row["Vehicle Model"],
                    "year": row["Vehicle Year"],
                    "category": row["Vehicle Type"]

                }

            }

            data.setdefault(i, details)                      # returning the value of the key and assigning it
    
        
    with open(jsonFile, 'w', encoding='utf-8') as jsonf:     # creating our json dict
        jsonf.write(json.dumps(data, indent=4))
    
 
csvFile = r'acw_user_data (1).csv'
jsonFile = r'Company_Db.json'
 
convert_json(csvFile,jsonFile)                                # here we call the function with the two params
