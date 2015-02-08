'''
Created on Nov 13, 2013

@author: Sriram
'''

import Pearson_Similarity
import recommendation
import Ranking


#function used to invert the rating and the userid table
def transformPrefs(prefs):
    result={}
    
    for person in prefs:
        for item in prefs[person]:
        
            result.setdefault(item,{})
            # Flip item and person
            result[item][person]=prefs[person][item]
            
    return result


# Gets recommendations for each user by using a weighted average
# of every other user's rankings
#user based colloborative filtering
def getRecommendations(prefs,person,similarity= Pearson_Similarity.sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        # don't compare me to myself
        if other==person: continue
        sim=similarity(prefs,person,other)

        # ignore scores of zero or lower
        if sim<=0: continue
        for item in prefs[other]:
             
        # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item]==0:
                # Similarity * Score
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                # Sum of similarities
                simSums.setdefault(item,0)
                simSums[item]+=sim
           
    # Create the normalized list
    rankings=[(total/simSums[item],item) for item,total in totals.items( )]
    
    # Return the sorted list
    rankings.sort( )
    rankings.reverse( )
    return rankings 

#movies=transformPrefs(recommendation.critics)


   

   



  
    
