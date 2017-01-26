# computes the avg of two user input scores

# def avg():
#     score1 = eval(raw_input("Please enter first exam score: "))
#     score2 = eval(raw_input("Please enter second exam score: "))
#     average = (score1 + score2) / 2
#     print "The average is: ", average

def avg():
    score1, score2 = eval(raw_input("Please enter two exam scores separated by a comma: "))
    average = (score1 + score2) / 2
    print "The average is: ", average

avg()
