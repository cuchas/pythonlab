score_list = 1,2,2,4,4
s = None

def score():
    if(0 <= s < 1):
        return 'Terrible'
    elif 1<=score<2: 
        return 'Bad'
    elif 2<=score<3:
        return 'Good'
    else:
        return 'Excellent'

def remove_edges():