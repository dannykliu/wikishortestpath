import time
import json
import retinasdk
import wikipedia

fC = retinasdk.FullClient('37762630-a8ac-11e6-a057-97f4c970893c', apiServer="http://api.cortical.io/rest", retinaName="en_associative")
start_time = time.time()
# fC.compare(json.dumps([{"term": "apple"}, {"term": "oranges"}]))
# fC.compare(json.dumps([{"term": "math"}, {"term": "calculus"}]))
# print(fC.compare(json.dumps([{"term": "Donald Trump"}, {"term": "China"}])))
print(fC.compareBulk(json.dumps([[{"term": "calculus"}, {"term": "math"}], 
	[{"term": "trigonometry"}, {"term": "math"}], [{"term": "Donald Trump"}, {"term": "math"}]])))

print('=================', time.time() - start_time, '===================== seconds')

def getSimilarity(metric):
	return metric.weightedScoring
