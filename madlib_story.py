with open("madlib_story.txt","r")as f:
    story=f.read()
#print(story)
#The enumerate function generates pairs of (index, element) for each element in the story.
#words=[]
#we use set() because it does not includ duplicate elements
words=set()
start_of_word=-1
target_start="<"
target_end=">"
for index,character in enumerate(story):
    if character==target_start:
        start_of_word=index
    if character==target_end and start_of_word!=-1:
        word=story[start_of_word : index+1]
        #words.append(word)
        words.add(word)
        start_of_word=-1
#print(words)
answers= {} 
for word in words:
    answer=input("Enter a word for "+ word + ": ")
    answers[word]=answer
print(answers)
for word in words:
    story=story.replace(word,answers[word])      

print(story)