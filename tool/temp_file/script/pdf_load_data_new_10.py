import os
import camelot
os.system("rm /home/hadoop/project/BigDataTool/tool/temp_file/stagging/*")
os.system("rm /home/hadoop/project/BigDataTool/tool/temp_file/convert/*")
os.system("hdfs dfs -get /user/hadoop/pdf_load/* /home/hadoop/project/BigDataTool/tool/temp_file/stagging/")
os.system("hdfs dfs -rm /user/hadoop/pdf_load/*")
file_name = os.listdir("/home/hadoop/project/BigDataTool/tool/temp_file/stagging/")
input_file = camelot.read_pdf("/home/hadoop/project/BigDataTool/tool/temp_file/stagging/"+file_name[0])
df = input_file[0].df
df.columns = df.iloc[0]
df = df.drop(df.index[1])
output_df = df[['Date', 'Open', 'High', 'Low', 'Close / Last']]
output_df = output_df.drop(index=0)
output_df.to_csv("/home/hadoop/project/BigDataTool/tool/temp_file/convert/"+file_name[0]+".csv", index=False,header=False)
os.system("hdfs dfs -put /home/hadoop/project/BigDataTool/tool/temp_file/convert/* /user/hive/warehouse/pdf_load_data_new")
