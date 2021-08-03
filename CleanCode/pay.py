# public Money calculatePay(Employee e)
# throws InvalidEmployeeType {
# switch (e.type) {
# case COMMISSIONED:
# return calculateCommissionedPay(e);
# case HOURLY:
# return calculateHourlyPay(e);
# case SALARIED:
# return calculateSalariedPay(e);
# default:
# throw new InvalidEmployeeType(e.type);
# }
# }

def calculatePay(employee):
    try:
        if employee.type == "COMMISSIONED":
            return calculateCommissionedPay(employee)
        elif employee.type == "HOURLY":
            return calculateHourlyPay(employee) 
        elif employee.type == "SALARIED":
            return calculateSalariedPay(employee)
    except InvalidEmployeeType:
        raise Exception("The employee type is invalid!")