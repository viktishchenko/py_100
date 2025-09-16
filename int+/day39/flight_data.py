class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.lowest_price = price
        self.origin = origin_airport
        self.destination = destination_airport
        self.out_date = out_date
        self.return_date = return_date