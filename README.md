# Grootan-Coding-Assignment

### * Requirement Understanding

1. Create Web Application with Import CSV option when upload button is clicked
    
    a. Import function – To upload the csv file
    
    b. Import File validation (success or Failure )
        
        i. If it is .CSV then it will should throw the success message “File uploaded Successfully”
        
        ii. If it is not .csv file then it should throw the error “ Upload CSV file only”

    c. Read the first row in the CSV file. [Assumption First row will be Header field for CSV]

        i. Read the file using comma as delimiter

        ii. Validate the Each column in the first row for any special character

            1. If any special character then Exception handling

            2. If no special character then it should create the Table in the database with the column name present in CSV first row header

        iii. Compare each column in the first with string “password” and assign data field as password (Encryption and decryption )

    d. Read the second records and store it in Database
        
        i. Create query with the available data and insert the record in New created Table.[Student_table]
        
        ii. Create success and failure record counter

            1. If insert is success then increase the counter by 1

            2. If insert is failure then increase the counter by 1

2. Display record inserted counter display
    
    a. “Successfully processed Records :” = 20(example)
    
    b. “Insert Failed Records :” = 20(example)

3. Progressing bar when the recorded gets inserted

    a. Show progressing bar / indicator to show the records are getting inserted

    b. Once processing completed.
  
        i. Display the time take to complete the upload activities

        ii. Calculate the time from insert of the first row to last row of insertion.
        
### * Output
