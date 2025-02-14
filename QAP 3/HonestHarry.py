# Description: Program for Honest Harry to keep track of sales.
# Author: Spencer Noseworthy
# Date(s): Feb 07 2025 - Feb 08 2025


# Define required libraries.
import datetime
import sys # Using this library to implement the "END" at first name.


# Define program constants.
FINANCE_FEE = 39.99
LICENSE_FEE_LOW = 75.00
LICENSE_FEE_HIGH = 165.00 
TRANSFER_RATE = .01
LUXURY_TAX_RATE = .016
HST_RATE = .15

AllowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
AllowedNum = set("1234567890")

# Main program starts here.

while True:

    # Gather user inputs.

    while True:
        CustFirst = input("Enter the customer's first name: ").title()
        if CustFirst.upper() == "END":
            sys.exit() # This was tricky to figure out, took a while to get it in the right place.
        
        if CustFirst == "":
            print()
            print("   Error - customer name cannot be blank.")
            print()
        else:
            break

    while True:
        CustLast = input("Enter the customer's last name: ").title()

        if CustLast == "":
            print()
            print("   Error - customer name cannot be blank.")
            print()
        else:
            break

    while True:
        Phone = input("Enter the customer's phone number (0000000000): ")
        
        if Phone == "":
            print()
            print("   Error - customer phone number cannot be blank.")
            print()
        elif len(Phone) != 10:
            print()
            print("   Error - customer phone must be 10 digits.")
            print()  
        elif set(Phone).issubset(AllowedNum) == False:
            print()
            print("   Error - customer phone must be digits only.")
            print() 
        else:
            break

    while True:
        PlateNum = input("Enter the customer's plate number (XXX000): ").upper()

        if PlateNum == "":
            print()
            print("   Error - License plate number cannot be blank.")
            print()
        elif len(PlateNum) != 6:
            print()
            print("   Error - License plate number must be 6 characters.")
            print()
        elif set(PlateNum[0:3]).issubset(AllowedChar) == False:
            print()
            print("   Error - Plate number must start with 3 letters.")
            print()
        elif set(PlateNum[3:6]).issubset(AllowedNum) == False:
            print()
            print("   Error - Plate number must end with 3 numbers.")
            print()
        else:
            break
        
    
    CarMake = input("Enter the car make: ")
    CarModel = input("Enter the car model: ")
    CarYear = input("Enter the car year: ")

    while True:
        SellPrice = input("Enter the selling price: ")
        SellPrice = float(SellPrice)
        if SellPrice >= 50000:
            print()
            print("   Error - Sell price cannot exceed $50,000. ")
            print()            
        else:
            break

    while True:
        TradeValue = input("Enter the trade-in value: ")
        TradeValue = float(TradeValue)
        if TradeValue > SellPrice:
            print()
            print("   Error - Trade-in price cannot exceed the selling price.")
            print()
        else:
            break

    while True:
        SalesName = input("Enter the salesperson's name: ")

        if SalesName == "":
            print()
            print("   Error - Salesperson's name cannot be blank.")
            print()
        else:
            break
    

    InvoiceDate = datetime.datetime.now()

    Initial = CustFirst[0]
    FullName = Initial + ". " + CustLast

    PhoneNum = "(" + Phone[0:3] + ") " + Phone[3:6] + "-" + Phone[6:10]
 
    CarDetails = CarYear + " " + CarMake + " " + CarModel

    ReceiptID = CustFirst[0] + CustLast[0] + "-" + PlateNum[3:6] + "-" + Phone[6:10]


    # Perform required calculations.
    PriceAfterTrade = SellPrice - TradeValue

    LuxuryFee = 0

    if SellPrice <= 15000:
        LicenseFee = LICENSE_FEE_LOW
        TransferFee = PriceAfterTrade * TRANSFER_RATE
        Subtotal = PriceAfterTrade + LICENSE_FEE_LOW + TransferFee
        HST = Subtotal * HST_RATE
        TotalPrice = Subtotal + HST

    elif SellPrice > 20000:
        LicenseFee = LICENSE_FEE_HIGH
        LuxuryFee = PriceAfterTrade * LUXURY_TAX_RATE
        TransferFee = (PriceAfterTrade * TRANSFER_RATE) + LuxuryFee
        Subtotal = PriceAfterTrade + LICENSE_FEE_HIGH + TransferFee
        HST = Subtotal * HST_RATE
        TotalPrice = Subtotal + HST

    else:
        LicenseFee = LICENSE_FEE_HIGH
        TransferFee = PriceAfterTrade * TRANSFER_RATE        
        Subtotal = PriceAfterTrade + LICENSE_FEE_HIGH + TransferFee
        HST = Subtotal * HST_RATE
        TotalPrice = Subtotal + HST

    # Formatting done prior to prints, just to keep it all formatted in the code.
    SellPriceDsp = "${:,.2f}".format(SellPrice)
    TradeAllowanceDsp = "${:,.2f}".format(TradeValue)
    PriceAfterDsp = "${:,.2f}".format(PriceAfterTrade)
    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    TransferFeeDsp = "${:,.2f}".format(TransferFee)
    SubtotalDsp = "${:,.2f}".format(Subtotal)
    HSTDsp = "${:,.2f}".format(HST)
    TotalPriceDsp = "${:,.2f}".format(TotalPrice)
    FirstPayment = InvoiceDate + datetime.timedelta(days = 30)

    # Display results
    print()
    print(f"Honest Harry Car Sales                            Invoice Date: {InvoiceDate:%B %d, %Y}")
    print(f"Used Car Sale and Receipt                         Receipt No:         {ReceiptID:>11s}")
    print()
    print(f"                                            Sale price:                {SellPriceDsp:>9s}")
    print(f"Sold to:                                    Trade Allowance:            {TradeAllowanceDsp:>9s}")
    print(f"                                            -------------------------------------")
    print(f"     {FullName:<18s}                     Price after Trade:         {PriceAfterDsp:>9s}")
    print(f"     {PhoneNum:<14s}                         License Fee:                {LicenseFeeDsp:>9s}")
    print(f"                                            Transfer Fee:               {TransferFeeDsp:>9s}")
    print(f"                                            -------------------------------------")
    print(f"Car Details:                                Subtotal:                  {SubtotalDsp:>9s}")
    print(f"                                            HST:                        {HSTDsp:>9s}")
    print(f"     {CarDetails:<30s}         -------------------------------------")
    print(f"                                            Total sales price:         {TotalPriceDsp:>9s}")
    print()
    print(f"---------------------------------------------------------------------------------")
    print()
    print(f"                                  Financing         Total          Monthly")
    print(f"      # Years    # Payments          Fee            Price          Payment")
    print(f"      --------------------------------------------------------------------")
    for Years in range(1, 5):
        Payments = Years * 12
        FinanceFee = FINANCE_FEE * Years
        MonthlyPayment = TotalPrice / Payments
        TotalPayments = TotalPrice + FinanceFee + MonthlyPayment

        FinanceFeeDsp = "${:,.2f}".format(FinanceFee)
        MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)
        TotalPaymentsDsp = "${:,.2f}".format(TotalPayments)
        
        print(f"         {Years:>2d}           {Payments:>2d}         {FinanceFeeDsp:>9s}        {TotalPaymentsDsp:>9s}     {MonthlyPaymentDsp:>9s}")
    print(f"      --------------------------------------------------------------------")
    print(f"      Invoice Date: {InvoiceDate:%d-%b-%y}                First payment date: {FirstPayment:%d-%b-%y}")
    print(f"---------------------------------------------------------------------------------")
    print(f"                        Best used cars at the best prices!")

    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.