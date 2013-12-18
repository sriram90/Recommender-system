'''
Created on Nov 16, 2013
@author: hai
'''

import getRecommendedItems
import recommendation
import calculateSimilarItems
import GetRecommendation


#itemsim = calculateSimilarItems.calculateSimilarItems(recommendation.critics)#
#print(itemsim)     
#print(getRecommendedItems.getRecommendedItems(recommendation.critics,itemsim,'Toby'))itemsim=recommendations.calculateSimilarItems(prefs,n=50)

prefs=recommendation.loadMovieLens()

itemsim=calculateSimilarItems.calculateSimilarItems(prefs,n=50)
print(getRecommendedItems.getRecommendedItems(prefs,itemsim,'87')[0:30])



#print(GetRecommendation.getRecommendations(prefs,'87')[0:30])
