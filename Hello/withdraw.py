def withdraw_money(current_bal, amount):
  if(current_bal >= amount ):
     current_bal= current_bal - amount
     return current_bal

balance = withdraw_money(100, 30)
if(balance<=50):
    print("jaza")

else:
    print("ok")


#Learning how to use a return statement
