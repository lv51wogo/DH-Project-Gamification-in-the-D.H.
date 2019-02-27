import os

questionDic = {}
AnswerDic = {}


for filename in os.listdir('Data'):
    numbersInString = int(''.join(list(filter(str.isdigit, filename))))
   
    tempDic = {}
    with open('Data/' + filename) as file:
        for line in file:
            key, value = line.strip().split(':')
            tempDic.update( {key : value} )

    AnswerList = list(tempDic)
    questionDic.update( {numbersInString : tempDic})

    AnswerDic.update( {numbersInString : AnswerList})






	