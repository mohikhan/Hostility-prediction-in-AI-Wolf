# This file is used to extract the feautures for the neural networks from the agent game 
# in every day ending

from OMGUS import *

def extract_update(base_info,diff_data,request,myid,counter_negative,counter_positive,mytarget):
    


    for row in diff_data.itertuples():
        type = getattr(row,"type")
        text = getattr(row,"text")

        if (type == "talk" and "[{:02d}]".format(myid) in text):

            source = getattr(row,"agent")

            if(source == mytarget):


                logging.debug("My target said the sentence  : {}".format(text))

                # Calculate the number of negative sentences in a day

                if ("VOTE Agent[{:02d}]".format(myid) in text or "ESTIMATE Agent[{:02d}] WEREWOLF".format(myid) in text
                or "ESTIMATE Agent[{:02d}] POSSESSED".format(myid) in text or  "DIVINED Agent[{:02d}] WEREWOLF".format(myid)  in text 
                or "REQUEST ANY (VOTE Agent[{:02d}])".format(myid) in text):

                    counter_negative[0]+=1

                    logging.debug("The value of counter -ve is {}".format(counter_negative[0]))

                # Calculate the number of positive sentences in a day

                elif("ESTIMATE Agent[{:02d}] VILLAGER".format(myid) in text or "ESTIMATE Agent[{:02d}] SEER".format(myid) in text
                or "ESTIMATE Agent[{:02d}] MEDIUM".format(myid) in text or "ESTIMATE Agent[{:02d}] BODYGUARD".format(myid) in text or
                "DIVINED Agent[{:02d}] HUMAN".format(myid) in text):

                    counter_positive[0]+=1

                    logging.debug("The value of counter +ve is {}".format(counter_positive[0]))

        # elif (type == "vote"):
    
        #     voter = getattr(row,"idx")
        #     target = getattr(row,"agent")
         
        #     if (target == myid and voter == mytarget):
        #         logging.debug("Agent target {} voted for me!".format(voter))
        #         vote = 1
        #         logging.debug(vote)
                


        



# Calculate the complexity of the sentence (inspired from killer queen)  