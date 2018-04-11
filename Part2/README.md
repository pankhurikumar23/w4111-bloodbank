COMS 4111 - Introduction to Databases
<h1> Project Part 2 </h1>

##### Shreya Vaidyanathan (sv2525) & Pankhuri Kumar (pk2569)
_PostgreSQL account_ - sv2525 (UNI)

_Online Readme_ - https://github.com/pankhurikumar23/w4111-bloodbank/blob/master/Part2/README.md

**Project Description**
Implementing the advanced features (mostly object-relational) of the PostgresSQL database management system for our Blood Bank Project.


**-> Design changes to existing schema are as follows:-**
  1. ***Composite type:***
      - Created 'contact_details' with two fields (Phno VARCHAR, addr VARCHAR) as a type. 
        - Used the new composite data type in our existing database by appending to the donor and recipients table, and dropped the separate 'phone' and 'address' columns. The two fields have been set to NOT NULL to ensure data integrity of the original table is maintained.
  2. ***Arrays***:
      - Created a new array of integers called 'bloodquantity' of size 8 - It helps map the blood type to quantity. 
        - | 0  | 1    |  2   |   3   |   4   |   5   |    6  |    7  |
          |----|:----:|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|        
          |A+|A-|B+|B-|O+|O-|AB+| AB-| 
          
          The array now helps to store the amount of blood of each type effectively withing the 'bloodbanks' and 'hospital' tables itself, thereby eliminating the need for an extra tale like 'bloodcapacity' (table has been dropped). 
          
          ![alt text](https://github.com/pankhurikumar23/w4111-bloodbank/blob/master/Part2/bloodcapacity.png "Dropped Table Schema")
          
          Earlier we had multiple rows for capturing the amount of blood each blood bank or hospital had for each type of blood, but now with the use of array we are able to make the design more effortless with just one row dedicated to each institution in the respective tables.
          
  3. ***Documents***: 
      - Created a new 'notes' documents field along with the 'internalrequests' table. 
        - This helps store the special instructions or notes from doctors while they try to retrieve blood from their hospital for any internal request. This note will be useful when doctors have to communicate the need for immediate blood transfers during critical procedures or for high-risk patients for instance. This note will also be beneficial in instances when a hospital admin wants to classify all those notes for a particular patient. particular illness or procedure. It allows for various new kinds of text-based manipulations of our existing database design. 
        - Eg. searching for 'immediate' in notes will reveal all the notes that doctors have asked urgent attention or care for. Similarly we could query for all notes that were given for a certain illness like 'Brain hemorrhage' or 'Diabetes.' 


**-> Meaningful SQL QUERIES on updated DB design:-**
  1. To find all hospitals/bloodbanks with the quantity of a particular blood type   
        * Query: SELECT * FROM bloodbanks WHERE bloodquantity[2] is NOT NULL;   
          
          Result: 
          
          ![alt text](https://github.com/pankhurikumar23/w4111-bloodbank/blob/master/Part2/Array1.png "Result has 5 rows")
        * Query: SELECT * FROM hospitals WHERE bloodquantity[3] > 100;
          
          Result: 
          
          ![alt text](https://github.com/pankhurikumar23/w4111-bloodbank/blob/master/Part2/Array2.png "Result has 2 rows")
          
  2. Select all donors/recipients that belong to a particular area (based on phone and address) 
        * Query: Select * FROM donor WHERE (condet).phno LIKE '212%' ORDER BY (condet).addr;
          
          Result:
          
          ![alt text](https://github.com/pankhurikumar23/w4111-bloodbank/blob/master/Part2/Composite%20Type.png "Result has 4 rows")
        
  3. Find and retrieve all notes that doctors gave for a particular illness like 'Diabetes' or with 'Immediate' requirements
        * Query: SELECT * FROM internalrequest WHERE to_tsvector(notes) @@ to_tsquery('diabetes');
          
          Result: Displays rows with closest matches to 'diabetes'.
          
          ![alt text](https://github.com/pankhurikumar23/w4111-bloodbank/blob/master/Part2/Text2.png "Result has 2 rows")
          
        * Query: SELECT * FROM internalrequest WHERE to_tsvector(notes) @@ to_tsquery('immediately');
        
          Result: Displays rows with closest matches to 'immediately,' including 'immediate'
          
          ![alt text](https://github.com/pankhurikumar23/w4111-bloodbank/blob/master/Part2/Text1.png "Result has 3 rows")
