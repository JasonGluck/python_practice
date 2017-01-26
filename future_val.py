def futval():
    principal = eval(raw_input("Please principal investment: "))
    years = eval(raw_input("Please enter years to investment maturity: "))
    apr = eval(raw_input("Please enter apr (decimal form): "))

    for i in range(years):
        principal = principal * (1 + apr)

    print "The value in", years, "years is", principal,"."

futval()
