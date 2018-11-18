# check if users have praised the leader within 1 hour time limit
# i.e. check discord ids that have praised against list of ids in server
# bad!users get sent to Sam for bad!points

# timestamps are stored by discord as such:
# 2018-11-17 22:33:29.273000
# runs immediately when praise is detected
# so i can get a timestamp immediately and we are happy
# DICTIONARIES ARE THE WAY FORWARD
# i.e. store userid as key and FALSE as value if they haven't replied within 1 hour
# TRUE if they have.... obviously
# reset all values to FALSE when praise is asked for again

def praisecheck(serverid_list, userid_list, sent_time):
    import time
    
    sent_time2 = sent_time.split(".")                         
    sent_time3 = time.strptime(sent_time2[0], "%Y-%m-%d %H:%M:%S")
    
    userid_time = userid_list[1].split(".")    
    userid_time2 = time.strptime(userid_time[0], "%Y-%m-%d %H:%M:%S")
    
    difference = time.mktime(userid_time2) - time.mktime(sent_time3)
    if difference < 60**2:
        serverid_list.remove(userid_list[0])

    return serverid_list