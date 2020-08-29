## ZOMENTUM HIRING ASSIGNMENT (BACKEND)

https://zomsystem.herokuapp.com/

### Endpoint to view all records. (JSON)

https://zomsystem.herokuapp.com/showallrecords

### An endpoint to book a ticket using a user’s name, phone number, and timings.

POST REQUEST : 

    import requests
    
    files = {'upload_file': open('0987908uiy78.txt','rb')}
    r = requests.post("https://zomsystem.herokuapp.com/automated_testing", files=files) # Text File containing records.

    print (r.text)   

GET REQUEST : https://zomsystem.herokuapp.com/result?uniqueid=NEW_UNIQUE_ID&nm=NEW_NAME&phonenumber=PHONENUMBER&time=TIME

### An endpoint to update a ticket timing.

https://zomsystem.herokuapp.com/updatetime?oldtime=PREVIOUS_OLD_TIME&newtime=UPDATED_TIME

### An endpoint to view all the tickets for a particular time.

https://zomsystem.herokuapp.com/listall?query=PARTICULAR_TIME

### An endpoint to delete a particular ticket.

https://zomsystem.herokuapp.com/deleteticket?query=UNIQUEID_OF_TICKET_TO_BE_DELETED

### An endpoint to view the user’s details based on the ticket id.

https://zomsystem.herokuapp.com/ticketinfo?query=TICKETID

### Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current
time.
