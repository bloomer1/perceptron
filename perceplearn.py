from sys import argv
import sys


script, trainingfile, modelfile = argv

#for linux
trainingfile_handle = open(trainingfile,'r',errors='ignore')
#trainingfile_handle = open(trainingfile,'r')
content = trainingfile_handle.read()
content = content.strip('\r')
sentence = content.split("\n")


unique_list = []
clList = []
originalDocList = []
trainDocList = []
listWeights = {}
equalList = []
globallistOfWeightDict  = {}
listOfWeightDictList = []
counter = 0
pre_val = 0

Wavdict = {}


unique_words_count = 0

#print (total_docs)

# list of diffrent class and unique words...
def uniqueWords(sentence):
	global originalDocList
	global unique_list
	global unique_words_count
	for doc in sentence:
		words = doc.split(" ")
		

		originalDocList.append(words[0])
		if words[0] not in clList:
			clList.append(words[0])
		for word in words[1:]:
			word = word.rstrip('\r')
			if word not in unique_list:
				unique_list.append(word)
				unique_words_count +=  1
	originalDocList[:] = [x for x in originalDocList if x != '']
	clList[:] = [x for x in clList if x != '']
		


#print (len(originalDocList))
#originalDocList[:] = [x for x in originalDocList if x != '']


#print (len(originalDocList))
#debug point a
'''
print clList
print unique_words_count
print unique_list
'''
# debug point a

#Initialize weight Dictionary for each class



def createGlobalDic():
	global clList
	global listOfWeightDictList
	global globallistOfWeightDict
	
	for iclass in clList:
		name = iclass + "Weights"
	
		name = {}
	
		for words in unique_list:
			name[words] = 0
		listOfWeightDictList.append(name)
		globallistOfWeightDict[iclass + "Weights"] = name
    
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



def checkAccuracy(originalDocList,trainDocList,total_docs):
	
	correct_count = 0
	
	for f, b in zip(originalDocList, trainDocList):
		if f == b:
			correct_count = correct_count + 1


		
	val = float(correct_count)/total_docs
	

	return val
    




'''
for iclass in clList:
	Wavdict[iclass] = 0
'''


def percepLearn(trainingfile,modelfile):
	#print (modelfile)
	#print (trainingfile)	
	global Wavdict
	trainingfile_handle = open(trainingfile,'r',errors='ignore')
	content = trainingfile_handle.read()
	sizeList = {}
	
	content = content.strip('\r')
	sentence = content.split("\n")
	sentence.remove('')
		
	total_docs =  len(sentence)
	
	uniqueWords(sentence)
	createGlobalDic()
	for iclass in clList:
		Wavdict[iclass] = 0
	
	while True:
		global counter 
		counter += 1
		for doc in sentence:
			words = doc.split(" ")
		
			y = words[0]
			for iclass in clList:
			
				sumOfWeights = 0
				d = globallistOfWeightDict[iclass + "Weights"]
				
				for word in words[1:]:
				
				
					word = word.rstrip('\r')
					sumOfWeights += d[word]

			#print iclass,sumOfWeights
				listWeights[iclass] = sumOfWeights
				global equalList			
				equalList.append(sumOfWeights)
		
			z = maxfn(listWeights)
			dec = checkEqual(equalList)
			equalList = []
		
			if dec == True:
				z = clList[0]
			global trainDocList
			trainDocList.append(z)



			if z != y:
				for word in words[1:]:
					word = word.rstrip('\r')
					for iclass in clList:
						d = globallistOfWeightDict[iclass + "Weights"]
						if iclass != y:
							d[word] = d[word] - 1
						else:
							d[word] = d[word] + 1
						sizeList[iclass] = sys.getsizeof(d)
		

						
	

			'''
			for iclass in clList:
			
				sumOfWeights = 0
				d = globallistOfWeightDict[iclass + "Weights"]
				for word in words[1:]:
					word = word.rstrip('\r')
					sumOfWeights += d[word]
				Wavdict[iclass] = Wavdict[iclass] + sumOfWeights   
				#Wavdict[iclass] = float(Wavdict[iclass])/(counter*total_docs)

				listWeights[iclass] = Wavdict[iclass]

				equalList.append(Wavdict[iclass])

			z = maxfn(listWeights)
			dec = checkEqual(equalList)
			equalList = []
		
			if dec == True:
				z = clList[0]
		
		
			trainDocList.append(z)
    			'''
		

		val = checkAccuracy(originalDocList,trainDocList,total_docs)
	
	




	
		#print (sentence)
		print  (val)
		print (counter)
		#print (trainDocList)
		#print counter
		#print (trainDocList)
	
		#print (originalDocList)
		
		#outhandle.write(str(counter))
		#outhandle.write("\n")
		'''	
		for k,v in globallistOfWeightDict.items():
			outhandle.write(str(k) + " " +str(v))
			outhandle.write("\n")
		'''
		#print pre_val, val 
		#print trainDocList
		if 1 - val < 0.02 or counter == 25:
			break
		pre_val = val
		
		trainDocList = []
		#print ("-------------")


 
	modelfile_handle = open(modelfile,'w',errors='ignore')

	modelfile_handle.write("classList")
	modelfile_handle.write("\n")
	modelfile_handle.write(str(clList))
	modelfile_handle.write("\n")
	modelfile_handle.write("sizeList")
	modelfile_handle.write("\n")
	modelfile_handle.write(str(sizeList))
	modelfile_handle.write("\n")
	modelfile_handle.write("globallistOfWeightDict")
	modelfile_handle.write("\n")
	modelfile_handle.write(str(globallistOfWeightDict))

	modelfile_handle.close()


def main():
	percepLearn(trainingfile,modelfile)	
	
if __name__ == "__main__":
	main()	
		
				




				














