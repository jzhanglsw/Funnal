import FundamentalAnalysis as fa

ticker = "CUE"

profile = fa.profile(ticker)

balance_sheet_annually = fa.balance_sheet_statement(ticker, period="annual")

#print(balance_sheet_annually.describe())

#print(list(balance_sheet_annually.columns.values))

#print(list(balance_sheet_annually["Total current assets"]))

bs_rows = list(balance_sheet_annually.index.values)
print(bs_rows)

print(getRowValues(balance_sheet_annually, 'Total current assets')

def getRowValues(df, row):
    return list(df.loc[ row , : ])