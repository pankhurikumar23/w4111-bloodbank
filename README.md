# w4111-bloodbank
Web Application for COMS-W4111 (Introduction to Databases) Blood Bank Project

---

* *PostgresSQL account* - sv2525 (UNI)
* *URL* of web application - https://35.231.15.255/:8111
* *Description* - <br>
Implemented the overall aim that we set out with. We have also tried to impement various specific features specified in project1-part1 and tried to extend their scope through our web application system. <br> *The following are working:- * <br>
  * Functionality and database support for the four different user personas or use-cases of the application -- (Donor/Recipient/Hospital Admin/ Blood Bank Administrator) <br>
  * Displaying information pertaining to individual patients receiving blood.  <br>
  * Displaying information pertaining to individual blood donors.  <br>
  * Ability to add new blood donors to the existing database in the 'searchUser.html' page. <br>
   * Ability to register a new patient as a blood recipient in the admin page of the hospital (and not in the blood bank).
  * Ability to query the details about any blood units in hospitals and bloodbanks (only available if admin) <br>
  * Ability to query availability of blood for new patient in any department of the hospital <br>
  
 *Few things we would like to improve further:-* (which we believe are currently beyond the scope of this project)
 * To query the availability of blood levels with a limit on certain rare blood types like (AB-ve) and some other ones that are low in units at all the banks and hospitals.
 * Optimizing which hospital or department receives blood on some order of priority. 

* *Two interesting web pages* - <br>
  * searchUser.html - Provides details pertaining to any donor or recipient.
  * searchAdmin.html - Provides in-depth information about the availability of blood for new patient in any department of the hospital 


_Commit log_:
 - Add Button Working
 - Created new landing page
 - Add button works now
 - Multiple pages created for different users
 - Querying DB through flask
 - Displaying results on textarea in jinja templates
