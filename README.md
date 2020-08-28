## ZOMENTUM HIRING ASSIGNMENT (BACKEND)

### An endpoint to book a ticket using a user’s name, phone number, and timings.

POST REQUEST : 

    import requests
    
    files = {'upload_file': open('0987908uiy78.txt','rb')}
    r = requests.post("http://127.0.0.1:8000/automated_testing", files=files) # Text File containing records.

    print (r.text)   

GET REQUEST : http://127.0.0.1:8000/result?uniqueid=NEW_UNIQUE_ID&nm=NEW_NAME&phonenumber=PHONENUMBER&time=TIME

### An endpoint to update a ticket timing.

127.0.0.1:8000/updatetime?oldtime=PREVIOUS_OLD_TIME&newtime=UPDATED_TIME

### An endpoint to view all the tickets for a particular time.

### An endpoint to delete a particular ticket.

http://127.0.0.1:8000/deleteticket?query=UNIQUEID_OF_TICKET_TO_BE_DELETED

### An endpoint to view the user’s details based on the ticket id.

http://127.0.0.1:8000/ticketinfo?query=TICKETID

### Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current
time.
