from sys import argv
import ast
import sys

script, modelfile = argv


model_handle = open(modelfile,'r',errors='ignore')
learning = model_handle.read();

learnComponents = learning.split("\n")

classList = []
classList = ast.literal_eval(learnComponents[1])

#print (classList)

#classList.remove('')


globallistOfWeightDict = dict()
globallistOfWeightDict = ast.literal_eval(learnComponents[5])

#print (globallistOfWeightDict)

   
inputDoc = input()
input_handle = open(inputDoc,'r',errors='ignore')

content = input_handle.read()

content = content.strip('\r')
content = content.split("\n")



def maxfn(listWeights):
	z = ""
	maxweight = float("-inf")
	for k,v in listWeights.items():
		if maxweight < v:
			maxweight = v
			z = k
		
	return z


def checkEqual(equalList):
	prev = equalList[0]
	count = 1
	for item in equalList[1:]:
		if item == prev:
			count = count + 1

	if count == len(equalList):
		return True
	else:
		return False


listWeights = {}
equalList = []
for iclass in classList:
	sumOfWeights = 0
	d = globallistOfWeightDict[iclass + "Weights"]
	for words in content:
		wordline = words.split(" ")
		for word in wordline:
			word = word.rstrip('\r')
			if word in d:			
				sumOfWeights += d[word]
			
			
	listWeights[iclass] = sumOfWeights
	equalList.append(sumOfWeights)	
z = maxfn(listWeights)
dec = checkEqual(equalList)
equalList = []
if dec == True:
	z = clList[0]
print (z)
# also flush the output
sys.stdout.flush()



		









