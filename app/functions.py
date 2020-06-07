# calculates daily_limit

def limit(budget):
    
    import calendar
    from datetime import date
    
    current_year, current_month, current_day = str(date.today()).split("-")
    
    current_day = int(current_day)
    current_month = int(current_month)
    current_year = int(current_year)
    
    
    today = date.today()
    
    last_day_month = calendar.monthrange(current_year, current_month)[1]
    
    days_to_end_month = last_day_month - current_day
    
    daily_exp_limit = budget / days_to_end_month
    
    return daily_exp_limit
