'''
Created on Nov 13, 2013

@author: hai
'''
import Pearson_Similarity
import recommendation
    # Returns the best matches for person from the prefs dictionary.
    # Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=Pearson_Similarity.sim_pearson):
    scores=[(similarity(prefs,person,other),other)
    for other in prefs if other!=person]
    # Sort the list so the highest scores appear at the top
    scores.sort( )
    scores.reverse( )
    return scores[0:n]

