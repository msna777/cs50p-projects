bp=int(input("Please enter the battery precentage : "))
mt=int(input("Please enter the motor Temperature : "))

if bp<20 or mt>=80:
    print("STATUS: CRITICAL","\n Emergency shutdown required.")
elif 20<=bp<=49 or 60<=mt<=79:
    print("STATUS: WARNING","\n Battery is getting low.")
elif bp>=50 and mt<60:
    print("STATUS: SAFE","\n Robot ready for operation.")
