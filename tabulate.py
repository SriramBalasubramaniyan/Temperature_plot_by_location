import pandas as pd

def get_df(data):
    daily_date = data['daily'] # extract daily dictionary
    df = pd.DataFrame({
        "date": daily_date['time'],
        "max_temp": daily_date['temperature_2m_max'],
        "min_temp": daily_date['temperature_2m_min']
    }) # made it into data frame(table)

    """
    Example:
    	      date	max_temp  min_temp
    0	2026-02-09	   11.4	       4.3
    1	2026-02-10	   12.8	       9.1
    2	2026-02-11	   13.4	       10.6
    3	2026-02-12	   12.3	       9.0
    4	2026-02-13	   9.2	       7.7
    5	2026-02-14	   8.0	       0.9
    6	2026-02-15	   10.2	       -0.6
    7	2026-02-16	   11.5	       7.3
    """

    df['date'] = pd.to_datetime(df['date']) # changed date from string to datetime type
    return df