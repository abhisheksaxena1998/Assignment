## ZOMENTUM HIRING ASSIGNMENT (BACKEND)

https://zomsystem.herokuapp.com/

### Endpoint to view all records. (JSON)

https://zomsystem.herokuapp.com/showallrecords

![automated testing](/Images/beforeinsertion.png)  

### An endpoint to book a ticket using a user’s name, phone number, and timings.

GET REQUEST : https://zomsystem.herokuapp.com/result?uniqueid=NEW_UNIQUE_ID&nm=NEW_NAME&phonenumber=PHONENUMBER&time=TIME

![automated testing](/Images/1.png)  

Showing all records :

![automated testing](/Images/2.png)  


POST REQUEST : 

    import requests
    
    files = {'upload_file': open('one.txt','rb')}
    r = requests.post("https://zomsystem.herokuapp.com/automated_testing", files=files) # Text File containing records.

![automated testing](/Images/onetext.png)  

![automated testing](/Images/multiplepostrecords.png)  

Showing all inserted records using POST:

![automated testing](/Images/4.png)  

### An endpoint to update a ticket timing.

https://zomsystem.herokuapp.com/updatetime?oldtime=PREVIOUS_OLD_TIME&newtime=UPDATED_TIME

![automated testing](/Images/5.png)  

Showing all records:

![automated testing](/Images/6.png)  

### An endpoint to view all the tickets for a particular time.

https://zomsystem.herokuapp.com/listall?query=PARTICULAR_TIME

![automated testing](/Images/7.png)  

### An endpoint to delete a particular ticket.

https://zomsystem.herokuapp.com/deleteticket?query=UNIQUEID_OF_TICKET_TO_BE_DELETED

![automated testing](/Images/8.png)  

### An endpoint to view the user’s details based on the ticket id.

https://zomsystem.herokuapp.com/ticketinfo?query=TICKETID

![automated testing](/Images/9.png)  

### Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current
time.
