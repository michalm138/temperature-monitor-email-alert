# Temperature monitor with e-mail alert


### Requirements:

##### Linux Operating System and package
This program works with linux only. It is based on command "sensors"
       
    $ sudo apt-get install lm-sensors 

##### Python modules
1. Yagmail is used for sending email messages. It works with gmail.
       
        $ pip install yagmail

2. Schedule is used for set the plan when the temperature will be check.

       $ pip install schedule
  
### Lines to change:
To set the maximum temperature:
```
21. if temperature >= 40:
```
To set e-mail parameters:
```
24. 'your_email_addressgmail.com', 'your_password')
26. to='receiver_email_address@gmail.com',
```
To set your plan:
                
    51. schedule.every(30).minutes.do(check)
