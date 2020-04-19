# 'D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx'

# import pandas as pd
# data = pd.read_excel('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx',sheet_name='Cases', header = 3, skiprows=3, index_col=0)
# # data = pd.ExcelFile.parse('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx',sheet_name='Cases', header = 3, skiprows=3, index_col=0)
# # print(data)
# print(data[['ageCase']])

from xlrd import *
file = open_workbook('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx')
# print(data)
data = []
for i in range(0,4):
    # 0 = Cases, 1 = Mortality, 2 = Recovered, 3 = Testing
    data.append(file.sheet_by_index(i)) 

# rows and colums 0 indexed: row 0-2 = readme, 3 = header, 4 onwards = data
numColCases = data[0].ncols
numRowCases = data[0].nrows
rowCases = []
for i in range(0, numRowCases):
    row = data[0].row_values(i)
    rowCases.append(row)

numColTesting = data[3].ncols
numRowTesting = data[3].nrows
rowTesting = []
for i in range(0, numRowTesting):
    row = data[3].row_values(i)
    rowTesting.append(row)    

ageCase = []
sexCase = []
healthRegionCase = []
provinceCase = []
dateReportedCase = []

provinceTesting = []

# initialize data category for each header
# 0CaseID. 1ProvCase. 2ageCase. 3sexCase. 4healthRegionCase. 5provinceCase. 6Country. 7dateReportedCase. 8WeekReported
for i in range(4, numRowCases):
    if rowCases[i][2] not in ageCase:
        ageCase.append(rowCases[i][2])
    if rowCases[i][3] not in sexCase:
        sexCase.append(rowCases[i][3])
    if rowCases[i][4] not in healthRegionCase:
        healthRegionCase.append(rowCases[i][4])
    if rowCases[i][5] not in provinceCase:
        provinceCase.append(rowCases[i][5])
    if rowCases[i][7] not in dateReportedCase:
            dateReportedCase.append(rowCases[i][7])
            
for i in range(4,numRowTesting):
    if rowTesting[i][1] not in provinceTesting:
        provinceTesting.append(rowTesting[i][1])

# initialize data by each category
ageCaseData = [[] for i in ageCase]
sexCaseData = [[] for i in sexCase]
healthRegionCaseData = [[] for i in healthRegionCase]
provinceCaseData = [[] for i in provinceCase]
dateReportedCaseData = [[] for i in dateReportedCase]    
provinceTestingData = [[] for i in provinceTesting]

# categorize data
# 0CaseID. 1ProvCase. 2ageCase. 3sexCase. 4healthRegionCase. 5provinceCase. 6Country. 7dateReportedCase. 8WeekReported
for i in range(4,numRowCases):
    ageCaseData[ageCase.index(rowCases[i][2])].append(rowCases[i])
    sexCaseData[sexCase.index(rowCases[i][3])].append(rowCases[i])
    healthRegionCaseData[healthRegionCase.index(rowCases[i][4])].append(rowCases[i])
    provinceCaseData[provinceCase.index(rowCases[i][5])].append(rowCases[i])
    dateReportedCaseData[dateReportedCase.index(rowCases[i][7])].append(rowCases[i])

for i in range(4,numRowTesting):
    provinceTestingData[provinceTesting.index(rowTesting[i][1])].append(rowTesting[i])
    
    
# test for checking data
# for i in healthRegionCaseData:
#     for j in i:
#         print(j[4])

# test for checking data
# for i in provinceTestingData:
#     for j in i:
#         print(j[1])


# have projected data kept in variable to be called by API
# project rate of infection vs Test to future rate