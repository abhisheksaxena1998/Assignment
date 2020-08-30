## ZOMENTUM HIRING ASSIGNMENT (BACKEND)

https://zomsystem.herokuapp.com/

![automated testing](/Images/11.png)  

**TECH STACK**

Python, Django(Framework), SQLite database, Heroku (for deployment)

### Business cases supported by REST APIs:

    ● An endpoint to book a ticket using a user’s name, phone number, and timings.
    ● An endpoint to update a ticket timing.
    ● An endpoint to view all the tickets for a particular time.
    ● An endpoint to delete a particular ticket.
    ● An endpoint to view the user’s details based on the ticket id.
    ● Mark a ticket as expired if there is a difference of 8 hours between the ticket timing 
      and current time.
    ● All the tickets which are expired automatically deleted.  
    ● For a particular timing, a maximum of 20 tickets can be booked.
    ● REST paradigm implemented.
    ● SQLite database used.
    ● POSTMAN snaps of all APIs attached in README.

### Input format

![automated testing](/Images/format.png)  

    Time should be in format dd/MM/yyyy HH:mm:ss

## Endpoints usage with POSTMAN snaps.

### Endpoint to view all records. (JSON)

https://zomsystem.herokuapp.com/showallrecords

![automated testing](/Images/beforeinsertion.png)  

    This is the start state when there are no records. Purpose of /showallrecords is to display all 
    records to infer changes made using APIs.

### An endpoint to book a ticket using a user’s name, phone number, and timings.

**GET REQUEST** : https://zomsystem.herokuapp.com/addRecord?uniqueid=UNIQUE_ID_OF_NEW_RECORD&nm=NAME&phonenumber=PHONENUMBER&time= dd/MM/yyyy HH:mm:ss

![automated testing](/Images/alter1.png)  

    This accepts a ‘unique_id’, ‘Name’, ‘Phone number’ and ‘time’ for which ticket is to be booked, a 
    ‘created_at’ entry is automatically stored in database which stores the time when request to add a
    new record is generated

*Showing all records :* https://zomsystem.herokuapp.com/showallrecords

![automated testing](/Images/alter2.png)  

    All records are displayed to denote the insertion of a record.

**POST REQUEST :** 

    import requests
    
    files = {'upload_file': open('one.txt','rb')}
    r = requests.post("https://zomsystem.herokuapp.com/automated_testing",files=files)
    # 'one.txt' is Text File containing records.

![automated testing](/Images/altertext.png)  

![automated testing](/Images/multiplepostrecords.png)  

    We can send an automated POST request to the end point with a .txt file which contains records as 
    shown to add multiple records at a time easily through a POST request.

*Showing all inserted records using POST:* https://zomsystem.herokuapp.com/showallrecords

![automated testing](/Images/alter4.png)  

    Shown here are multiple inserted records using automated POST request.

### For a particular timing, a maximum of 20 tickets can be booked.

![automated testing](/Images/alter17.png)  

    GET API ensures that for a particular timing, a maximum of 20 tickets can be booked.

![automated testing](/Images/alter16.png) 

    An instance is shown through POSTMAN, that when records exceed 20 for a particular time they are rejected.

### An endpoint to update a ticket timing.

https://zomsystem.herokuapp.com/updatetime?oldtime=PREVIOUS_OLD_TIME&newtime=UPDATED_TIME

![automated testing](/Images/alter19.png)  

    Here shown the endpoint that accepts a previous time and updated time, to update time entry.
    
![automated testing](/Images/updatetime.png) 

    If the matching query is not found then an error message is returned by API.

*Showing all records:* https://zomsystem.herokuapp.com/showallrecords

![automated testing](/Images/alter21.png)  

    Shown all records after updating

### An endpoint to view all the tickets for a particular time.

https://zomsystem.herokuapp.com/listall?query=PARTICULAR_TIME

![automated testing](/Images/alter22.png)  

    This is the instance that shows information of tickets booked for a particular time.

### An endpoint to delete a particular ticket.

https://zomsystem.herokuapp.com/deleteticket?query=UNIQUEID_OF_TICKET_TO_BE_DELETED

![automated testing](/Images/8.png)  

    Endpoint to delete a particular ticket that accepts unique id of ticket to be deleted
    
![automated testing](/Images/deleteticket.png)

        If the matching query is not found then an error message is returned by API. 

### An endpoint to view the user’s details based on the ticket id.

https://zomsystem.herokuapp.com/ticketinfo?query=TICKETID

![automated testing](/Images/alter23.png)  

    Shown here the example, that is used to view users’ detail for a ticket id.

### Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time.

![automated testing](/Images/alter24.png)

    Since, there is difference of 8 hours between present and other time (the one added here), 
    it will be deleted automatically

![automated testing](/Images/alter25.png)  

    In this example:
    a.	A request is made to add a new record that has a longer difference than 8 hours
    b.	From postman it is clear that record is added successfully
    c.	However, a function is invoked automatically in all the endpoints that automatically deletes 
            entries with difference greater than 8 hours.

### Final records after all operations

![automated testing](/Images/alterfinal.png)             
