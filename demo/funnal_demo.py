import FundamentalAnalysis as fa

ticker = "AAPL"

# Show the available companies
companies = fa.available_companies()
print(companies)

# Collect general company information
profile = fa.profile(ticker)

# Collect recent company quotes
quotes = fa.quote(ticker)

# Collect market cap and enterprise value
entreprise_value = fa.enterprise(ticker)

# Show recommendations of Analysts
ratings = fa.rating(ticker)

# Collect the Balance Sheet statements
balance_sheet_annually = fa.balance_sheet_statement(ticker, period="annual")
balance_sheet_quarterly = fa.balance_sheet_statement(ticker, period="quarter")

# Collect the Income Statements
income_statement_annually = fa.income_statement(ticker, period="annual")
income_statement_quarterly = fa.income_statement(ticker, period="quarter")

# Collect the Cash Flow Statements
cash_flow_statement_annually = fa.cash_flow_statement(ticker, period="annual")
cash_flow_statement_quarterly = fa.cash_flow_statement(ticker, period="quarter")

# Show Key Metrics
key_metrics_annually = fa.key_metrics(ticker, period="annual")
key_metrics_quarterly = fa.key_metrics(ticker, period="quarter")
