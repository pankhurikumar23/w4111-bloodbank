# w4111-bloodbank
Web Application for COMS-W4111 (Introduction to Databases) Blood Bank Project

---

* *PostgresSQL account* - sv2525 (UNI)
* *URL* of web application - https://35.231.15.255:8111
* *Description* - <br>
Implemented the overall aim that we set out with. We have also tried to impement various specific features specified in project1-part1 and tried to extend their scope through our web application system. <br> *The following are working:- * <br>
  * Functionality and database support for the four different user personas or use-cases of the application -- (Donor/Recipient/Hospital Admin/ Blood Bank Administrator) <br>
  * Displaying information pertaining to individual patients receiving blood.  <br>
  * Displaying information pertaining to individual blood donors.  <br>
  * Ability to add new blood donors to the existing database. <br>
  * Ability to register a new patient as a blood recipient in the admin page of the hospital.
  * Ability to query the details about any blood units in hospitals (only available if admin) <br>
  * Ability to query availability of blood for a recipient in any department of the hospital <br>
  * Ability to query the history of transfusions for a recipient in a particular hospital. <br>
  
 *Few things we would like to improve further:-* (which we believe are currently beyond the scope of this project)
 * To query the availability of blood levels with a limit on certain rare blood types like (AB-ve) and some other ones that are low in units at all the banks and hospitals.
 * Optimizing which hospital or department receives blood on some order of priority. 

* *Two interesting web pages* - <br>
  * searchUser.html - Provides details pertaining to any donor or recipient. Lets a user query their past donations, date, units, 
  * searchAdmin.html - Provides in-depth information about the availability of blood in the entire system.
       * - Lets admin at hospital look at the list of available blood, blood type, units etc.
       * - Lets admin at hospital ad new requets for a department requiring blood of any type at the particular hospital for patient.
       * - Lets admin at blood bank query the blood availablity in their blood bank, other blood banks in the system and add new donations (for existing donors and also add new donors to the working database list.)

_Commit log_:
 - Add Button Working
 - Created new landing page
 - Add button works now
 - Multiple pages created for different users
 - Querying DB through flask
 - Displaying results on textarea in jinja templates
 - Adding queries
 - Adding new page for displaying final results
