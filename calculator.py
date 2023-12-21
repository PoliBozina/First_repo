counter=0
result = None
operand = None
operator = None
wait_for_number = True

while True:
    oper = input(">>>")
    counter=counter+1
    if counter%2==1:
        try:
            oper=int(oper)
            operand=str(oper)
            print(f'>>>{oper}')
            if result==None:
                result=str(oper)
            else:
                result=result+operator+operand
            
        except ValueError:
            print(f'{oper} is not a number. Try again.')
            counter=counter-1
            
    elif counter%2==0:
        oper=str(oper)
        if oper=='+' or oper=='-' or oper=='*' or oper=='/':
            operator=str(oper)
            print(f'>>{oper}')
            if oper=='+':
                result=int(result)
                operand=int(operand)
                result=result+operand

            
        elif oper=='=':
            
            print(result)
            break    
        else:
            print(f'{oper} is not "+" or "-" or "/" or "*". Try again')
            counter=counter-1
                      
    else:
        if oper=='=':
            print(result)
            break
            
