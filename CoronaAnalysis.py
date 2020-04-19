# 'D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx'

# import pandas as pd
# data = pd.read_excel('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx',sheet_name='Cases', header = 3, skiprows=3, index_col=0)
# # data = pd.ExcelFile.parse('D:\CJ\Academic\CMPT340\Project\Public_COVID-19_Canada.xlsx',sheet_name='Cases', header = 3, skiprows=3, index_col=0)
# # print(data)
# print(data[['ageCase']])

from xlrd import *
import numpy as np
import copy
import datetime
import matplotlib.pyplot as plt

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

# # takes dates in day-month-year
# def compareDates(date11, date22):
#     date1 = date11.split('-')
#     date2 = date22.split('-')
#     dateDifference = date2[0] - date1[0]
#     monthDifference = date2[1] - date1[1]
#     yearDifference = date2[2] - date1[2]
#     totalDifference = yearDifference*365+monthDifference*30+dateDifference
#     print(totalDifference, date11, date22)
#     return totalDifference

# take date in x+19000101 format and return yearmonthdate in int format
def swapDate(date):
    initialDate = datetime.datetime(1900,1,1)
    currentTime = initialDate + datetime.timedelta(date)
    return currentTime
    
# takes dateTime format and return int version
# not that accurate?
def to_integer(dt_time):
    year = dt_time.year
    month = dt_time.month
    day = dt_time.day
    # if month == 4:
    #     month = month-1
    #     day = day+31
        
    return 10000*year + 100*month + day    
    
for i in provinceCaseData:
    for j in i:
        date = swapDate(j[7])
        date = to_integer(date)
        j[7] = copy.deepcopy(date)

# sort provinceCaseData by dateReported
for i in provinceCaseData:
    for j in i:
        sorted(j, key = lambda column: j[7])
        
for i in provinceTestingData:
    for j in i:
        date = swapDate(j[0])
        date = to_integer(date)
        j[0] = copy.deepcopy(date)
        
for i in provinceTestingData:
    for j in i:
        sorted(j, key = lambda column: j[0])
        # print(j)
        # print()

# by province
timeCaseDataX = [[] for i in provinceCase]
timeCaseDataY = [[] for i in provinceCase]
for i in provinceCaseData:
    for j in i:
        timeCaseDataX[provinceCase.index(j[5])].append(j[7])
        timeCaseDataY[provinceCase.index(j[5])].append(float(j[1]))

timeTestingDataX = [[] for i in provinceTesting]
timeTestingDataY = [[] for i in provinceTesting]
for i in provinceTestingData:
    for j in i:
        if j[2] != 'NA':
            timeTestingDataX[provinceTesting.index(j[1])].append(j[0])            
            timeTestingDataY[provinceTesting.index(j[1])].append(float(j[2]))
        
# calculate polynomial
z = np.polyfit(timeCaseDataX[1], timeCaseDataY[1], 6)
f = np.poly1d(z)

# print(timeTestingDataX[1])
# print(timeTestingDataY[1])
z1 = np.polyfit(timeTestingDataX[1], timeTestingDataY[1], 6)
f1 = np.poly1d(z1)
# # calculate new x's and y's
# x_new = np.linspace(timeCaseDataX[0][0], timeCaseDataX[0][-1], 50)
# y_new = f(x_new)

# plt.plot(timeCaseDataX[0],timeCaseDataX[0],'.')
# # plt.xlim([timeCaseDataX[0][0]-1, timeCaseDataX[0][-1] + 1 ])
# plt.show()

date = 20200419
# date = 20200350
print(provinceCase[1])
print('date', timeCaseDataX[1][-1])
print('infected', timeCaseDataY[1][-1])
print("expected infected", f(date))
print()

print(provinceTesting[1])
print('date', timeTestingDataX[1][0])
print('tested', timeTestingDataY[1][0])
print("expected tested", f1(date))


testingdiff = (f1(date)-timeTestingDataY[1][0])/timeTestingDataY[1][0]*100
casediff = (f(date)-timeCaseDataY[1][-1])/timeCaseDataY[1][-1]*100
print(testingdiff,casediff)
print(f(date)/f1(date)*100)
print(timeCaseDataY[1][-1]/timeTestingDataY[1][0]*100)

# dateSwap hack vs nonhack both have less than 5% deviance in accuracy at latest day