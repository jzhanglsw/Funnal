import FundamentalAnalysis as fa

def formatCurrencyRow(row):
	return "${:.1f}K".format(x/1000)

#ticker = "ZM"
ticker = input("Stock : ") 

# Collect general company information
profile = fa.profile(ticker)
##print("General company info:\n")

# Collect the Balance Sheet statements
balance_sheet_annually = fa.balance_sheet_statement(ticker, period="annual")
#print(balance_sheet_annually)

balance_sheet_quarterly = fa.balance_sheet_statement(ticker, period="quarter")
#print(balance_sheet_quarterly)

# Collect the Income Statements
income_statement_annually = fa.income_statement(ticker, period="annual")
#print(income_statement_annually)
income_statement_quarterly = fa.income_statement(ticker, period="quarter")
#print(income_statement_quarterly)

# Collect the Cash Flow Statements
cash_flow_statement_annually = fa.cash_flow_statement(ticker, period="annual")
#print(cash_flow_statement_annually)
cash_flow_statement_quarterly = fa.cash_flow_statement(ticker, period="quarter")
#print(cash_flow_statement_quarterly)

# Show Key Metrics
key_metrics_annually = fa.key_metrics(ticker, period="annual")
key_metrics_quarterly = fa.key_metrics(ticker, period="quarter")

#Load header to write into html
with open('header.txt', 'r') as file:
	header = file.read()

#Add better formatting later
with open(ticker + ".html", "w") as _file:
	_file.write("<html lang=\"en\">")
	_file.write(header)
	_file.write("<h1>" + ticker + " Profile</h1>")
	_file.write(profile.to_html() + "\n\n")
	_file.write("<h1>Balance Sheet Annually</h1>")
	_file.write(balance_sheet_annually.to_html() + "\n\n")
	_file.write("<h1>Balance Sheet Quarterly</h1>")
	_file.write(balance_sheet_quarterly.to_html() + "\n\n")
	_file.write("<h1>Income Statement Annually</h1>")
	_file.write(income_statement_annually.to_html() + "\n\n")
	_file.write("<h1>Income Statment Quarterly</h1>")
	_file.write(income_statement_quarterly.to_html() + "\n\n")
	_file.write("<h1>Cash Flow Statement Annually</h1>")
	_file.write(cash_flow_statement_annually.to_html() + "\n\n")
	_file.write("<h1>Cash Flow Statement Quarterly</h1>")
	_file.write(cash_flow_statement_quarterly.to_html() + "\n\n")
	_file.write("<h1>Key Metrics Annually</h1>")
	_file.write(key_metrics_annually.to_html() + "\n\n")
	_file.write("<h1>Key Metrics Quarterly</h1>")
	_file.write(key_metrics_quarterly.to_html() + "\n\n")
	_file.write("</html>")




