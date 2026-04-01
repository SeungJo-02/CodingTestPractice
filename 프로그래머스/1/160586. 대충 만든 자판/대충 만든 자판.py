def solution(keymap, targets):

    press_dict = {}
    
    for keys in keymap:
        for i, char in enumerate(keys):
          
            if char not in press_dict or i + 1 < press_dict[char]:
                press_dict[char] = i + 1
                
    answer = []
    
  
    for target in targets:
        total_press = 0
        possible = True
        
        for char in target:
            if char in press_dict:
                total_press += press_dict[char]
            else:
                
                possible = False
                break
        
        
        if possible:
            answer.append(total_press)
        else:
            answer.append(-1)
            
    return answer