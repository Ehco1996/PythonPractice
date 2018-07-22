'''
 从csv中读写文件，
 生成平均分之后，再导出为新的csv文件
'''
import pandas as pd
stu_df = pd.DataFrame()
stu_df = pd.read_csv('stu_scores.csv')
stu_df['sum'] = stu_df['Python'] + stu_df['Math']
print(stu_df)
stu_df.to_csv('stu_scores1.csv')