# import csv,re,os,sys
# import pandas as pd
# from tabulate import tabulate

# # print(os.getcwd())

# import usecsv
# # sys.path.append('c:/test/issue')
# # sys.path.append('c:\Users\LG\Desktop\Python_practice')
# os.chdir('c:/test/issue')

# # print(os.listdir())

# file = usecsv.opencsv('ISSUE_201905.xls')
# file_a = []

# for i in file:
#     file_a.append(i[0].split('\t'))

# # print(file_a)

# final_file = pd.DataFrame(file_a)

# final_file.columns = ['일시', '지점', '폭염여부', '최고체감온도', '최고기온', \
#     '평균기온', '최저기온', '평균상대습도', '폭염특보', '폭염영향예보', '열대야', '자외선지수']

# final_file = final_file[1:]

# print(final_file)


