# 'D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx'

# import pandas as pd
# data = pd.read_excel('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx',sheet_name='Cases', header = 3, skiprows=3, index_col=0)
# # data = pd.ExcelFile.parse('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx',sheet_name='Cases', header = 3, skiprows=3, index_col=0)
# # print(data)
# print(data[['age']])

from xlrd import *
file = open_workbook('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx')
# print(data)
data = []
for i in range(0,4):
    # 0 = Cases, 1 = Mortality, 2 = Recovered, 3 = Testing
    data.append(file.sheet_by_index(i)) 

# rows and colums 0 indexed: row 0-2 = readme, 3 = header, 4 onwards = data
numCol = data[0].ncols
numRow = data[0].nrows
# print(numCol, numRow)
colData = []
# get data of 'Cases' by column
for i in range(0, numCol):
    col = data[0].col_values(i)
    colData.append(col)
# print(colData[0][4])
rowData = []
for i in range(0, numRow):
    row = data[0].row_values(i)
    rowData.append(row)


# BC = []
# Ontario = []
# Manitoba = []
# Alberta = []
# Quebec = []
# Saskatchewan = []
# PEI = []
# NL = []
# NovaScotia = []

age = []
sex = []
healthRegion = []
province = []
dateReported = []

# initialize data category for each header
# 0CaseID. 1ProvCase. 2Age. 3Sex. 4HealthRegion. 5Province. 6Country. 7DateReported. 8WeekReported
for i in range(4, numRow):
    if rowData[i][2] not in age:
        age.append(rowData[i][2])
    if rowData[i][3] not in sex:
        sex.append(rowData[i][3])
    if rowData[i][4] not in healthRegion:
        healthRegion.append(rowData[i][4])
    if rowData[i][5] not in province:
        province.append(rowData[i][5])
    if rowData[i][7] not in dateReported:
            dateReported.append(rowData[i][7])

# initialize data by each category
ageData = [[] for i in age]
sexData = [[] for i in sex]
healthRegionData = [[] for i in healthRegion]
provinceData = [[] for i in province]
dateReportedData = [[] for i in dateReported]    

# categorize data
# 0CaseID. 1ProvCase. 2Age. 3Sex. 4HealthRegion. 5Province. 6Country. 7DateReported. 8WeekReported
for i in range(4,numRow):
    ageData[age.index(rowData[i][2])].append(rowData[i])
    sexData[sex.index(rowData[i][3])].append(rowData[i])
    healthRegionData[healthRegion.index(rowData[i][4])].append(rowData[i])
    provinceData[province.index(rowData[i][5])].append(rowData[i])
    dateReportedData[dateReported.index(rowData[i][7])].append(rowData[i])

# test for checking data
for i in healthRegionData:
    for j in i:
        print(j[4])