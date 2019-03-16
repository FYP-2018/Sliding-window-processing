	

# this function cuts texts into several pieces based on lines
import math

def ReadFile(fileName):
	with open(fileName) as file:
		docs = []
		for line in file:
		    # The rstrip method gets rid of the "\n" at the end of each line
			docs.append(line.rstrip())
	return docs

def SlidingWindow(docs, maxLength, stride):
	longDocs = {}
	print("length of original docs: ", len(docs))
	processed_doc = ""
	for doc_id, doc in enumerate(docs):
		words = doc.split()
		if len(words) > maxLength:
			numOfPartition = math.ceil((len(words) - maxLength)/stride) + 1
			longDocs[doc_id] = numOfPartition
					
			for i in range(0, numOfPartition-1):
				new_doc = ""
				for j in range(0, maxLength):
					new_doc += words[i*stride + j] + " "
				processed_doc += new_doc +'\n'

			new_doc = ""
			for i in range((numOfPartition-1)*stride, len(words)):
				new_doc += words[i] + " "
			processed_doc += new_doc +'\n'

		else:
			processed_doc += doc +'\n'

	print("longDocs: ", longDocs)
	
	with open("sliding_window_sampled_content.txt", "w") as text_file:
		text_file.write(processed_doc)
	return longDocs

def ExpandLableTxt(longDocs):
	labels = ReadFile("sampled_summary.txt")
	print("length of original labels: ", len(labels))
	for id in sorted(longDocs.keys(), reverse=True):
		for i in range(longDocs[id]-1):
			labels.insert(id, labels[id])
	print("length of processed labels: ", len(labels))
	result = ""
	for label in labels:
		result += label +'\n'	
	with open("sliding_window_sampled_summary.txt", "w") as text_file:
		text_file.write(result)

# def ExtractLines(docs, maxLength):
# 	for doc_id, doc in enumerat(docs):
# 		if len(doc.split()) > maxLength:
# 		numNewfiles = len(lines)//numOfPartition
# 		newFiles = ["" for x in range(numNewfiles)]

# 		for index, line in enumerate(lines):
# 			newFiles[int(index%numNewfiles)] += line

# 	for file_num, file in enumerate(newFiles):
# 		fileName = "output" + str(file_num) + ".txt"
# 		with open(fileName, "w") as text_file:
# 			text_file.write(file)

docs = ReadFile("sampled_content.txt")
longDocs = SlidingWindow(docs, maxLength=100, stride=80)
ExpandLableTxt(longDocs)