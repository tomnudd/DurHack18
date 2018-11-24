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
import time

def praisecheck(not_praised_leader, userid_tuple, req_sent_time):
    """
    :param not_praised_leader: list of user IDs who haven't praised leader (currently everyone)
    :param userid_tuple: {userID, time sent praise}
    :param req_sent_time: time praise requested, in string format
    :return: user IDs who have not praised the leader
    """


    time_components = req_sent_time.split(".")
    time_of_praise_req = time.strptime(time_components[0], "%Y-%m-%d %H:%M:%S")
    
    userid_time = userid_tuple[1].split(".")
    time_praise_received = time.strptime(userid_time[0], "%Y-%m-%d %H:%M:%S")
    
    difference = time.mktime(time_praise_received) - time.mktime(time_of_praise_req)
    if difference < 60**2:
        not_praised_leader.remove(userid_tuple[0])

    return not_praised_leader

def test():
    print(praisecheck(["Jimmy", "Paula"], ["Paula", "2018-11-17 22:33:29.273000"], "2018-11-17 22:33:29.273000"))