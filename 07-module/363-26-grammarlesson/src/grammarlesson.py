
def characteristic_word(word):
    if word[-4:] == 'lios':
        return 'adj', 'm'
    elif (word[-5:]) == 'liala':
        return 'adj', 'f'
    elif (word[-3:]) == 'etr':
        return 'n', 'm'
    elif (word[-4:]) == 'etra':
        return 'n', 'f'
    elif (word[-6:]) == 'initis':
        return 'v', 'm'
    elif (word[-6:]) == 'inites':
        return 'v', 'f'
    else:
        return 'none'

def isPetyaLanguage():
    result = True
    sentence = input().split()
    length = len(sentence)
    if length == 0:
        print("YES")
        return result
    else:
        init = list(characteristic_word(sentence[0]))
        if init == 'none':
            result = False
            print("NO")
            return result
        elif init[0] == 'n':
            noun = True
        else:
            noun = False
        if length > 1:
            for word in sentence[1:]:
                feature = characteristic_word(word)
                adj = False
                if feature != 'none':
                    if feature[1] != init[1]:
                        result = False
                        print("NO")
                        return result
                    elif (not noun) and feature[0] == 'adj':
                        continue
                    elif (not noun) and feature[0] == 'n':
                        noun = True
                        continue
                    elif noun and feature[0] == 'v':
                        continue
                    else:
                        result = False
                        print("NO")
                        return result
                else:
                    result = False
                    print("NO")
                    return result
    if result:
        print("YES")
    return result