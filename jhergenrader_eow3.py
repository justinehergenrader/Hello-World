#Justine Hergenrader
#09/14/2025
#End of Week Assignment - Week 3



print("")
#Exercise 1: Shipping Cost Calculator

weight_kg = float(input("Enter the weight of the package in kilograms:"))

#convert kg to lbs
if weight_kg < 0:
    print("Invalid weight. Enter a positive weight.")

else: 
    weight_lbs = weight_kg * 2.20462

#determine shipping cost
    if weight_lbs < 5:
        shipping_cost = "$5"
   
    elif 5 < weight_lbs < 15:
        shipping_cost = "$10"

    else: #weight_lbs > 15
        shipping_cost = "$20"

#results
    print("Package Weight in pounds:", round(weight_lbs,2), "lbs")
    print("Shipping Cost:", shipping_cost)

### Test cases ###
# 0 kg, "Shipping Cost: $5"
# 2.27 kg, "Shipping Cost: $10"
# 6.8 kg, "Shipping Cost: $10"
# 7 kg, "Shipping Cost: $20"
# 15 kg, "Shipping Cost: $20
# -5 kg, "Invalid weight. Enter a positive weight."





print("")
#Exercise 2: Overtime Eligibility Checker

hours_worked = float(input("Enter the number of hours worked:"))
full_time_status = input("Is the employee full time? (T/F):")

if full_time_status == "T":
    fulltime = True
elif full_time_status == "F":
    fulltime = False
else:
    print("Invalid. Full time status mist be 'T' or 'F'.")
    fulltime = False

if hours_worked < 0:
    print("Invalid. Number must be positive.")
else:
    if hours_worked > 40 and fulltime:
        print("Eligible for overtime pay.")
    else:
        print("Not eligible for overtime pay.")

    
### Test cases ###
# 41, T, "Eligible for overtime pay."
# 40, T, "Not eligible for overtime pay."
# 39, T, "Not eligible for overtime pay."
# 45, F, "Not eligible for overtime pay."
# 0, T, "Not eligible for overtime pay."
# 45, abc, "Invalid. Full time status mist be 'T' or 'F'."
# 30, abc, "Invalid. Full time status mist be 'T' or 'F'."
# -5, T, "Invalid. Number must be positive."





print("")
#Exercise 3: Factory Quality Monitor

defect_rate = float(input("Enter the defect rate as a percent:"))
units_produced = int(input("Enter the number of units produced:"))

if defect_rate < 0:
    print("Invalid. Number must be positive.")
elif units_produced <0:
    print("Invalid. Number must be positive.")
else:
    if defect_rate <= 5 and units_produced >= 1000:
        print("Production normal.")
    
    else:
        if defect_rate > 5:
            print("Quality Alert!")
        elif units_produced < 1000:
            print("Quality Alert!")

### Test cases ###
# 0%, 1000, "Production normal."
# 5%, 1000, "Production normal."
# 5.1%, 1000, "Quality Alert!"
# 4%, 999, "Quality Alert!"
# 6%, 900, "Quality Alert!"
# -5%, 1000, "Invalid. Number must be positive."
# 0%, -100, "Invalid. Number must be positive."





print("")
#Exercise 4: Travel Reimbursment Eligibility

#variables
distance_traveled = int(input("Enter the number of miles you traveled:"))
contractor_status = input("Are you a contractor? (True/False):")

if contractor_status == "True":
    is_contractor = True
elif contractor_status == "False":
    is_contractor = False
else:
    print("Invalid. Contractor status must be 'True' or 'False'.")
    is_contractor = False

if distance_traveled < 0:
    print("Invalid. Number must be positive.")
else:
    if contractor_status == "True" or contractor_status == "False":

        if distance_traveled > 100 and contractor_status == "False":
            print("Reimbursement Approved")
        elif distance_traveled < 100:
            print("Reimbursement Approved.")
        else:
            print("Not Approved.")

###Test Cases###
# 90, False, "Reimbursment Approved"
# 90, True, "Reimbursment Approved"
# 110, False, "Reimbursment Approved"
# 110, True, "Not Approved"
# -5, True/False, "Invalid. Number nust be positive."
# 110, abc, "Invalid. Contractor status must be 'True' or 'False'."





print("")
#Exercise 5: Security System Access

manager_status = input("Are you a manager? (True/False):")
probation_status = input("Are you on probation? (True/False):")
days_employed = int(input("How many days have you been employed here?:"))

if manager_status == "True":
    is_manager = True
elif manager_status == "False":
    is_manager = False
else:
    print("Invalid. Manager status must be 'True' or False'.")
    is_manager = False

if probation_status == "True":
    on_probation = True
elif probation_status == "False":
    on_probation = False
else:
    print("Invalid. Probation status must be 'True' or False'.")
    on_probation = False

if days_employed < 0:
    print("Invalid. Number must be postive.")
else:
    if is_manager or (not on_probation and days_employed > 90):
        print("Access Granted.")
    else:
        print("Access Denied.")

###Test Cases###
# True, True/False, 95, "Access Granted."
# True, True/False, 60, "Access Granted."
# False, False, 100, "Access Granted."
# False, False, 85, "Access Denied."
# False, True, 100, "Access Denied."
# abc, False, 100, "Invalid. Manager status must be 'True' or False'."
# True, abc, 100, "Invalid. Probation status must be 'True' or False'."
# True, False, -5, "Invalid. Number must be postive."


