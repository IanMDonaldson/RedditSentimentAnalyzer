import csv
import pandas as pd
import mysql.connector

# write to db.. fuck it
database = mysql.connector.connect(
    host='localhost',
    user='drago',
    password='Fucky0u!',
    database='reddit'
)
cursor = database.cursor()
df = pd.read_csv('../symbolName1')
df.drop_duplicates(subset="Name", keep="first", inplace=True)
for index in df.index:
    symbol = df["Symbol"][index]
    name = df["Name"][index]
    cursor.execute("INSERT INTO Ticker (symbol, companyName) VALUES ( %s, %s)", (symbol, name))

database.commit()
print(cursor.rowcount)
cursor.close()
#CSV = '../datafiles/nasdaq_tickers.csv'
#outfile1 = '../outfile'
#stopwords = {"Inc.", "Ltd.", "Ltd", "Corp.", "Common", "Class A", "Class B", "Class C", "Co.", "Limited", "Depositary"}
#df = pd.read_csv('../symbolName1')
#max = 0
#curr = 0
#i = 0
#for index in df.index:
#    curr = len(df["Name"][index])
#    if curr > max:
#        max = curr
#        i = index
#
#print(max,i)

# trim second column from stopwords
#df = pd.read_csv('../symbolName0')
#for index in df.index:
#    # prints every Name row as array of strings
#    #print(df["Name"][index].split(' '))
#    words = df["Name"][index].split(' ')
#    for word in words:
#        if word in stopwords:
#            df["Name"][index] = df["Name"][index].split(word,1)[0]
#df = df.drop_duplicates(subset="Name")
#df.to_csv('../symbolName1',index=False)




# make file with only first 2 columns
#df = pd.read_csv(CSV)
#keepCols = ["Symbol","Name"]
#newDF = df[keepCols]
#newDF.to_csv("../symbolName0", index=False)

# remove duplicates from file
#with open('../tickers', 'r') as infile:
#    with open('../tickers1','w') as outfile:
#        seen = set()
#        for row in infile:
#            if row in seen: continue
#            seen.add(row)
#            outfile.write(row)




        #reader = csv.reader(infile, delimiter=',')
        #seen = set()
        #for row in infile:
        #    if row in seen: continue
        #    seen.add(row)
        #    outfile.write(row)

