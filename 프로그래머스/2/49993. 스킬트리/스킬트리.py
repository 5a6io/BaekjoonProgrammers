def solution(skill, skill_trees):
    answer = 0
    comb = []
    
    for skills in skill_trees:
        sk = list(skill)
        
        for s in skills:
            if s in skill:
                if s != sk.pop(0):
                    break
        else:
             answer += 1       
            
    return answer