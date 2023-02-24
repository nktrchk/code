#calculator

def get_trip_price(distance,gas_prise, consunption):
    calculation_result = distance*(consunption/100*gas_prise)

    if calculation_result <= 100:
        print(f'It s going to be cheap')
        print(calculation_result, "EUR We will spend to get there")
    if calculation_result > 200:
        print("It's okaysch"),
        print(calculation_result, "EUR We will spend to get there")
    else:
        print('Are you fuckin kidding me?')
        print(calculation_result, "EUR We will spend to get there")



get_trip_price(100,1.78,8)