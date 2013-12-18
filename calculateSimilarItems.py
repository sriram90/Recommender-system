'''
Created on Nov 16, 2013

@author: hai
'''

import GetRecommendation
import Pearson_Similarity
import Ranking
import recommendation
import sim_distance

def calculateSimilarItems(prefs,n=10):
    
    # Create a dictionary of items showing which other items they
    # are most similar to.
    result={}
    # Invert the preference matrix to be item-centric
    itemPrefs = GetRecommendation.transformPrefs(prefs)
    
    for item in itemPrefs:
    
        # Find the most similar items to this one
        scores=Ranking.topMatches(itemPrefs,item,n=n,similarity= sim_distance.sim_distance)
        result[item]=scores
        
    return result




