# 💵 Loan calculator


This program allows you to calculate the principal loan, the monthly payment and the number of periods you need to pay off the principal.

All you need to do is to input all the necessary parameters using CLI, specify the type of calculation (annuity or differentiated) and miss the one parameter you would like to find out.

## How to use it?

1.Download and copy the path to the 'Loan calculator.py' file.

2.Run the command prompt, paste the copied path and start executing the python file as follows:

    python "Loan calculator".py -h
  
  You'll be presented with a quick guide to the calculator with a list of optional arguments.
  
  These are:
  
  - -t: indicates the type of calculation: diff (differentiated) or annuity;
  - -pr: determines the principal amount of your loan;
  - -pe: stands for the number of months for payment;
  - -in: means interest rate;
  - -p: defines monthly payment.
  
 Therefore, to find out the required parameter, you need to provide all the parameters necessary for the calculation and skip the wanted paremeter.
 
 For instance, given the defferentiated calculation type, the loan principal equaled to 30000, 23% interest rate and a year for payment, find out the monthly payment and the total overpayment going like this:
    
    python "Loan calculator".py -t=diff -pr=30000 -pe=12 -in=23
    
 And the result will be as follows:
 
    Month 1: payment is 3075
    Month 2: payment is 3028
    Month 3: payment is 2980
    Month 4: payment is 2932
    Month 5: payment is 2884
    Month 6: payment is 2836
    Month 7: payment is 2788
    Month 8: payment is 2740
    Month 9: payment is 2692
    Month 10: payment is 2644
    Month 11: payment is 2596
    Month 12: payment is 2548
    Overpayment = 3743
    
