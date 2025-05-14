#!/usr/bin/python3

def multiple_returns(sentence):
    
    # Check if the sentence is empty
    for i in range(len(sentence)):
        # if the sentence is empty return None
        if sentence == "":
            return None
        # return the length of the sentence and the first character
    return (len(sentence), sentence[0])
