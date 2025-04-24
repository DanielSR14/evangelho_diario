from modules.mod_date import get_tomorrow_date

year, month, day = get_tomorrow_date()
URL = f'https://www.vaticannews.va/pt/palavra-do-dia/{year}/{month}/{day}.html'
CANVA_URL = 'https://www.canva.com/design/DAGdpJC1jdc/krwRm28n4pC_82qR0D_PnA/edit'
JSON_FILE = "evangelho_logs.json"