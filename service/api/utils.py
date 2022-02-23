from datetime import date, datetime, timedelta


def get_current_date() -> date:
    return datetime.now().date()


def get_date_in_30_days() -> date:
    return (datetime.now() + timedelta(days=30)).date()
