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
COMMISSIONED = 100
HOURLY = 500
SALARIED = 200


def calculatePay(employee):
    try:
        if employee.type == COMMISSIONED:
            return calculateCommissionedPay(employee)
        elif employee.type == HOURLY:
            return calculateHourlyPay(employee) 
        elif employee.type == SALARIED:
            return calculateSalariedPay(employee)
    except InvalidEmployeeType:
        raise Exception("The employee type is invalid!")