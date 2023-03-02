import os
import pandas as pd
os.system("rm /home/hadoop/project/BigDataTool/tool/temp_file/stagging/*")
os.system("rm /home/hadoop/project/BigDataTool/tool/temp_file/convert/*")
os.system("hdfs dfs -get /user/hadoop/csv_lOAD/* /home/hadoop/project/BigDataTool/tool/temp_file/stagging/")
os.system("hdfs dfs -rm /user/hadoop/csv_lOAD/*")
file_name = os.listdir("/home/hadoop/project/BigDataTool/tool/temp_file/stagging/")
input_file = pd.read_csv("/home/hadoop/project/BigDataTool/tool/temp_file/stagging/"+file_name[0])
output_data = input_file[['Username', 'Identifier', 'First name']]
output_df = pd.DataFrame(output_data)
output_df.to_csv("/home/hadoop/project/BigDataTool/tool/temp_file/convert/"+file_name[0], index=False,header=False)
os.system("hdfs dfs -put /home/hadoop/project/BigDataTool/tool/temp_file/convert/* /user/hive/warehouse/csv_test_load")
