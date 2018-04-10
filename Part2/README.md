COMS 4111 - Introduction to Databases
<h1> Project Part 2 </h1>

**Project Description**
Implementing the advanced features (mostly object-relational) of the PostgresSQL database management system for our Blood Bank Project.


**-> Design changes to existing schema are as follows:-**
  1. ***Composite type:***
      - Created 'contact_details' with two fields (Phno INT, addr VARCHAR) as a type. 
        - Used the new composite data type in our existing database by appending the donor and recipients table.
  2. ***Arrays***:
      - Created a new array of integers called 'bloodquantity' of size 8 - It helps map the blood type to quantity. 
        - | 0  | 1    |  2   |   3   |   4   |   5   |    6  |    7  |
          |----|:----:|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|        
          |A+|A-|B+|B-|O+|O-|AB+| AB-| 
          
          The array now helps to store the amount of blood of each type effectively withing the 'bloodbanks' and 'hospital' tables itself. Thereby eliminating the need for an extra tale like 'bloodcapacity' 
          Earlier we had multiple rows for capturing the amount of blood each blood bank or hospital had for each type of blood, but now with the use of array we are able to make the design more effortless with just one row dedicated to each institution in the respective tables.
          
  3. ***Documents***: 
      - Created a new 'notes' documents field along with the 'internal requests' table. 
        - This helps store the special instructions or notes from doctors while they try to retrieve blood from their hospital for any internal request. This note will be useful when doctors have to communicate the need for immediate blood transfers during critical procedures or for high-risk patients for instance. This note will also be beneficial in instances when a hospital admin wants to classify all those notes for a particular patient. particular illness or procedure. It allows for various nw kinds of tet-based manipulation of our existing database design. 
        - Eg. searching for 'immediate' in notes will reveal all the notes that doctors have asked urgent attention or care for. Similarly we coulr query for all notes that were given for a certain illness like 'Brain hemorrhage' or 'Diabetes' 


**-> Meaningful SQL QUERIES on updated DB design:-**
  1. To find all hospitals/bloodbanks with the quantity of a particular blood type   
        * Query: SELECT * FROM bloodbanks WHERE bloodquantity[2] is NOT NULL;   
          Result:  
        * Query: SELECT * FROM hospitals WHERE bloodquantity[3] > 100;
          Result: Returns two rows. 
          
  2. Select all donors/recipients that belong to a particular zipcode (some address based manipulation)  
        * Query:     
          Result:    
        
  3. Find and retrieve all notes that doctors gave for a particular illness like 'Diabetes'  
        * Query:    
          Result:  
