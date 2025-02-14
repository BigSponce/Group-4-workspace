# Description: Marina billing program
# Author: Spencer Noseworthy
# Jan 26th, 2025


# Define Constants
EVEN_RATE = 80.00
ODD_RATE = 120.00
ALT_MEM_RATE = 5.00
CLEANING_RATE = 50.00
VIDEO_RATE = 35.00
HST_RATE = .15
STANDARD_RATE = 75.00
EXEC_RATE = 150.00
PROCESSING_RATE = 59.99
CANCELATION_RATE = .6


# Gather user inputs
Date = input("Enter the date (YYYY-MM-DD): ")
SiteNum = input("Enter the site number (1-100): ")
SiteNum = int(SiteNum)

MemName = input("Enter the customer name: ")
StreetAdd = input("Enter the street address: ")
City = input("Enter the city: ")
Prov = input("Enter the province (XX): ").upper()
Postal = input("Enter the postal code (X#X#X#): ")

PhoneNum = input("Enter the home phone (### ###-####): ")
CellNum = input ("Enter the cellphone number (### ###-####): ")

MemType = input("Enter the membership type (S / E): ")
AltMem = input("Enter the number of additional members (#): ")
AltMem = int(AltMem)
Cleaning = input("Enter the cleaning option (Y / N): ").upper()
Video = input("Enter the video surveilance option (Y / N): ").upper()


# Perform program calculations

if SiteNum % 2 == 0: 
    NumCharge = EVEN_RATE 
else: 
    NumCharge = ODD_RATE 
 
if AltMem >= 1: 
    AltMemCharge = AltMem * ALT_MEM_RATE 
else: 
    AltMemCharge = 0 
 
SiteCharge = NumCharge + AltMemCharge 


if Cleaning == "Y": 
    CleanCharge = CLEANING_RATE 
    CleanDsp = "Yes"
else:
    CleanCharge = 0 
    CleanDsp = "No"
 
if Video == "Y": 
    VideoCharge = VIDEO_RATE 
    VideoDsp = "Yes"
else: 
    VideoCharge = 0 
    VideoDsp = "No"
 
ExtraCharges = VideoCharge + CleanCharge 
MonthCharge = SiteCharge + ExtraCharges
HST = MonthCharge * HST_RATE 

TotMonthCharge = MonthCharge + HST 
 
if MemType == "E":
    MonthDues = EXEC_RATE 
    MemDsp = "Executive"
else:
    MonthDues = STANDARD_RATE 
    MemDsp = "Standard"
TotMonthFees = MonthDues + TotMonthCharge 
YearlyFees = TotMonthFees * 12 
MonthlyPayment = (YearlyFees + PROCESSING_RATE) / 12 

CancelFee = YearlyFees * CANCELATION_RATE 



# Display results
print()
print(f"      St. John's Marina & Yacht Club")
print(f"          Yearly Member Reciept")
print()
print(f"------------------------------------------")
print()
print(f"Client Name and Address:")
print()
print(f"{MemName:<24s}")
print(f"{StreetAdd:<24s}")
print(f"{City:<15s}, {Prov:<2s}, {Postal:<6s}")
print()
print(f"Phone: {PhoneNum:<12s} (H)")
print(f"       {CellNum:<12s} (C)")
print()
print(f"Site #: {SiteNum:>3d}          Member type: {MemDsp:<9s}")
print()
print(f"Alternate Members:                      {AltMem:>2d}")
print(f"Weekly Site cleaning:                  {CleanDsp:<3s}")
print(f"Video Surveillance:                    {VideoDsp:<3s}")
print()

SiteChargeDsp = "${:,.2f}".format(SiteCharge)
print(f"Site charges:                    {SiteChargeDsp:>9s}")

ExtraChargesDsp = "${:,.2f}".format(ExtraCharges)
print(f"Extra charges:                   {ExtraChargesDsp:>9s}")
print(f"                                -----------")

MonthChargeDsp = "${:,.2f}".format(MonthCharge)
print(f"Subtotal:                        {MonthChargeDsp:>9s}")

HSTDsp = "${:,.2f}".format(HST)
print(f"Sales tax (HST):                 {HSTDsp:>9s}")
print(f"                                -----------")

TotMonthChargeDsp = "${:,.2f}".format(TotMonthCharge)
print(f"Total monthly charges:           {TotMonthChargeDsp:>9s}")

MonthDuesDsp = "${:,.2f}".format(MonthDues)
print(f"Monthly dues:                    {MonthDuesDsp:>9s}")
print(f"                                -----------")

TotMonthFeesDsp = "${:,.2f}".format(TotMonthFees)
print(f"Total monthly fees:              {TotMonthFeesDsp:>9s}")

YearlyFeesDsp = "${:,.2f}".format(YearlyFees)
print(f"Total yearly fees:              {YearlyFeesDsp:>10s}")

print()

MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)
print(f"Monthly Payment:                 {MonthlyPaymentDsp:>9s}")

print(f"-------------------------------------------")
print()

print(f"Issued: {Date}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()

CancelFeeDsp = "${:,.2f}".format(CancelFee)
print(f"Cancellation fee:                {CancelFeeDsp:>9s}")
print()
