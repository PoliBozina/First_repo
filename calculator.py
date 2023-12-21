#counter=0
result = None
operand = None
operator = None
wait_for_number = True

while True:
    oper = input(">>>")
    #counter=counter+1
    if wait_for_number==True:
        try:
            oper=int(oper)
            #operand=str(oper)
            #print(f'>>>{oper}')
            wait_for_number=False
            #if result==None:
            #    result=str(oper)
            #else:
            #    result=result+operator+operand
            
        except ValueError:
            print(f'{oper} is not a number. Try again.')
            
            
    elif wait_for_number==False:
        oper=str(oper)
        if oper=='+' or oper=='-' or oper=='*' or oper=='/':
            operator=str(oper)
            #print(f'>>{oper}')
            wait_for_number=True
            #if oper=='+':
            #    result=int(result)
            #    operand=int(operand)
            #    result=result+operand

            
        elif oper=='=':
            
            print(result)
            break    
        else:
            print(f'{oper} is not "+" or "-" or "/" or "*". Try again')
                      
    else:
        if oper=='=':
            print(result)
            break
            
