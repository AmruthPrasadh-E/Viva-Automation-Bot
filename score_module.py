# marks = []
def Keyword_count(N, A):
    # N->list of keywords in answer key
    # A->list of keywords in input audio
    count = 0
    for i in set(A):
        if i in N:
            count = count+1
    return count

def candidate_score(n, a):    
    #N-> no.of keywords used for question set
    #A-> no. of keywords used by candidate
    score = round( (a/n)*100 ,1)
    # marks.append(score)
    return score

# print(candidate_score(13, 4))
