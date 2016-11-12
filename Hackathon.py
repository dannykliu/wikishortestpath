import json
import retinasdk
import wikipedia

fC = retinasdk.FullClient('601227f0-a8ad-11e6-a057-97f4c970893c', apiServer = "http://api.cortical.io/rest", retinaName = "en_associative")
BO = wikipedia.page("barackobama").links[2]
print(BO)
print(fC.compareBulk(json.dumps([[{"term": "ferhthjgfdx"}, {"term": "oranges"}], 
		[{"term": "math"}, {"term": "calculus"}], [{"term": "Donald Trump"}, {"term": "China"}]])))
# print(fC.compare(json.dumps([{"term":"cat"},{"term":"dog"}])))
# print(fC.compare(json.dumps([{"term":"cat"},{"term":"dog"}])))