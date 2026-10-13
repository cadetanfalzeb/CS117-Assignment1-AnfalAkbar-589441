voltage = float(input("Enter Voltage (V):"))
resistance = float(input("Enter Resistance(Ohm):"))
if resistance <=0:
    print("Invalid Resistance")
else:  
    current = voltage / resistance

    if current <= 2 and current >= -2:
        print("Current is:",current,"A")
        print("Circuit is Safe")
    elif current>2 or current<-2:
        print("Current is:",current,"A")
        print("Fuse will blow")
    
