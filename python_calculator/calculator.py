#calculator

def get_trip_price(distance,gas_prise, consunption):
    calculation_result = distance*(consunption/100*gas_prise)

    if calculation_result <= 99:
        print(f'It s going to be cheap')
        print(calculation_result, "EUR We will spend to get there")
    elif calculation_result > 101:
        print("It's okaysch"),
        print(calculation_result, "EUR We will spend to get there")



get_trip_price(100,1.78,8)