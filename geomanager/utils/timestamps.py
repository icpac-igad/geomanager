from datetime import date
from pandas import date_range


def get_dekadal_dates_range(start_date: date, final_date: date) -> list[date]:
    data_dates = []
    for year in range(start_date.year, final_date.year + 1):
        for month in range(1, 13):
            for dekad in [1, 11, 21]:
                data_date = date(year, month, dekad)
                if data_date >= start_date and data_date <= final_date:
                    data_dates.append(data_date)
    return data_dates


# for all other products
def get_pandas_dates_range(start_date: date, final_date: date, frequency: str | None = "MS") -> list[date]:
    return [
        timestamp.date()
        for timestamp in date_range(start=start_date, end=final_date, freq=frequency, inclusive="right").to_list()
    ]
