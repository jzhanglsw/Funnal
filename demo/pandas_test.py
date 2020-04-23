import FundamentalAnalysis as fa

ticker = "CUE"

profile = fa.profile(ticker)

balance_sheet_annually = fa.balance_sheet_statement(ticker, period="annual")

print(balance_sheet_annually.describe())

print(list(balance_sheet_annually.columns.values))
print(list(balance_sheet_annually.columns.values)[1])
print(list(balance_sheet_annually.index.values))
print(list(balance_sheet_annually["Total current assets"]))
