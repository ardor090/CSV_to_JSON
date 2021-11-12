import csv, json

file = 'acw_user_data.csv'
jsonfilepath = 'sample.json'


jsonArray = []
with open(file, 'r') as f:
    csvReader = csv.DictReader(f)
    # next(reader)
    # for val in csvReader:
    #     print(val)
    #     for k,v in list(val.items()):
    #         if v == "" or v == " ":
    #             del val[k]
                # print(val)
                # print(len(val))
    for row in csvReader:
    # for row in val:
        details = {
            "first_name": row["First Name"],
            "second_name": row["Last Name"],
            "age": row["Age (Years)"],
            "sex": row["Sex"],
            "retired": bool(row["Retired"]),
            "marital_status": row["Marital Status"],
            "dependents": row["Dependants"],
            "salary": row["Yearly Salary (Â£)"],
            "pension": row["Yearly Pension (Â£)"],
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

        jsonArray.append(details)


ab = json.dumps(jsonArray, indent=4, sort_keys=True)
print(ab)

# for data in jsonArray:
#     for k, v in data.items():
#         if v == "Lynne" and "last_name" == "Lynne":
#             print(k,v)