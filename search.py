import time
import json
import retinasdk
import wikipedia
import urllib.request

fC = retinasdk.FullClient('37762630-a8ac-11e6-a057-97f4c970893c', apiServer="http://api.cortical.io/rest", retinaName="en_associative")
start_time = time.time()
# fC.compare(json.dumps([{"term": "apple"}, {"term": "oranges"}]))
# fC.compare(json.dumps([{"term": "math"}, {"term": "calculus"}]))
# print(fC.compare(json.dumps([{"term": "Donald Trump"}, {"term": "China"}])))
# print(fC.compareBulk(json.dumps([[{"term": "calculus"}, {"term": "math"}], 
# 	[{"term": "trigonometry"}, {"term": "math"}], [{"term": "Donald Trump"}, {"term": "math"}]])))

def getSimilarity(metric):
	return metric.weightedScoring

def getFiveLinks(links):
	if len(links) < 5:
		return links
	return links[:5]

def getComparison(src, dst):
	return [{"term": src}, {"term": dst}]

def getComparisons(dst, links):
	comparisons = []
	for link in links:
		comparisons.append(getComparison(link, dst))
	return json.dumps(comparisons)

def makeComparisons(comparisons):
	return fC.compareBulk(comparisons)

def A_star(src, dst):
	links = wikipedia.page(src).links
	#print(links)
	comparisons = getComparisons(dst, getFiveLinks(links))
	print(getFiveLinks(links))
	print(makeComparisons(comparisons))
	# if inLinks(dst, links):
	# 	return True

#print(wikipedia.page('mathematics').url)
A_star('mathematics', 'trigonometry')
print('=================', time.time() - start_time, '===================== seconds')

