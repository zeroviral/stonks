from yahoofinancials import YahooFinancials
from collections import defaultdict

data = defaultdict(list)

# Make this the list input from either the file or a CLI

someList = []
someList.append('AAPL')
someList.append('NOK')
someList.append('TSLA')
someList.append('HITIF')
someList.append('BNGO')
someList.append('OCGN')


for element in someList:
    if element is None or element == '':
        continue
    yF = YahooFinancials(element)
    print('Net Income for', element, ':', yF.get_financial_stmts('annual',
                                                                 'balance'))


# data[ticker].append(yF.get_net_income())

# Push this to a Pandas DF and then push to CSV, open CSV at last step
