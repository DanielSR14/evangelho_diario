from datetime import datetime, timedelta

def get_tomorrow_date():
    tomorrow = datetime.today() + timedelta(days=1)
    if tomorrow.weekday() == 6:  # Domingo
        return None, None, None
    
    return tomorrow.year, f"{tomorrow.month:02d}", f"{tomorrow.day:02d}"

def formatted_date_func():
    year, month, day = get_tomorrow_date()
    return f"{day}-{month}-{year}"


if __name__ == '__main__':
    get_tomorrow_date()
