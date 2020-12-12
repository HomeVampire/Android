def check_str(rule):
    if ' ' not in rule and len(rule) > 2:
        if rule[0].isupper():
            if rule[1] == '#':
                for i in range(2, len(rule) - 1):
                    if rule[i].isupper() and rule[i + 1].isupper():
                        return 1
            else:
                return 1
        else:
            return 1
    else:
        return 1
    return 0
##############################################################################
def FIRSTOP(production_rule):
    firstop=dict()
    for i in production_rule:
        if i[0] not in firstop:
            firstop[i[0]] = list()

    for rule in production_rule:
        for i in rule[2:]:
            if i.isupper():
                if i not in firstop[rule[0]]:
                    firstop[rule[0]].append(i)
                else:
                    pass
            else:
                if i not in firstop[rule[0]]:
                    firstop[rule[0]].append(i)
                    break
                else:
                    pass
                break
    print(firstop)
##############################################################################
def LASTOP(production_rule):
    lastop=dict()
    for i in production_rule:
        if i[0] not in lastop:
            lastop[i[0]] = list()

    for rule in production_rule:
        for i in range(len(rule)-1,1,-1):
            if rule[i].isupper():
                if rule[i] not in lastop[rule[0]]:
                    lastop[rule[0]].append(rule[i])
                else:
                    pass
            else:
                if rule[i] not in lastop[rule[0]]:
                    lastop[rule[0]].append(rule[i])
                    break
                else:
                    pass
    print(lastop)
##############################################################################
def main():
    print("Please Enter Your Production Rules:\n"
          + "Please put '#' instead of '→'....")

    production_rule = list()
    while (1):
        rule = list(input("Enter Rule:\t"))
        problem = check_str(rule)
        if (problem == 0):
            production_rule.append(rule)
            check = input("Press any key to continue or \nPress 'N' or 'n' to stop...")
            if check == 'n' or check == 'N':
                break
        else:
            print("Your Production Rule is not in appropriate format...")

    FIRSTOP(production_rule)
    LASTOP(production_rule)


main()

