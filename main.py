import re
import FileManager
import StateModel

logfile = open("app_log_10.txt","r")
patternDate = r'(\d{4})-(\d{1,2})-(\d{1,2})'

#Lsit for date column
date_list = []
#Lsit for state column
state_list = []
#Lists for description
description_list = []
exception_list = []

for log in logfile:
    try:
       #Date list for Date column
       date = re.match(patternDate, log).group()
       lst = log.split(" ")
       #Extract ERROR state
       currentState = lst[4]

       if currentState == StateModel.StateModel.errorstate():
           date_list.append(date)
           state_list.append(currentState)

           #No Exception error
           decription = ' '.join(lst[8:13])
           commonerror_list = list(StateModel.StateModel.commonerror_set)
           if commonerror_list[0] in decription or commonerror_list[1] in decription:
               description_list.append(decription)

           #error with Exception
           exception_list.extend([' '.join(lst[14:30]) for n in lst if "Exception" in n])
    except AttributeError:
          date = re.match(patternDate, log)

#Create colomnun and write to output.txt file
FileManager.createdataframe(date_list, state_list, description_list, exception_list)









