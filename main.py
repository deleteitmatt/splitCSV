import pandas as pd
import time

# CONFIGURE LINES 5-8 BEFORE RUNNING #
excel_path = "/Users/mattbenedict/Desktop/script testing/WIP_Prostream_error_codes.xlsx"
save_path = "/Users/mattbenedict/Desktop/script testing/"
proj_name = "Prostream"
rows_per_file = 1000

start_time = time.time()
df = pd.read_excel(excel_path)
n_chunks = len(df) // rows_per_file

for i in range(n_chunks):
    start = i * rows_per_file
    stop = (i+1) * rows_per_file
    sub_df = df.iloc[start:stop]
    sub_df.to_csv(f"{save_path}{proj_name}_code_upload{i}.csv",
                  header=['Label name', 'Annotation', 'Object type'], index=False)
# noinspection PyUnboundLocalVariable
if stop < len(df):
    sub_df = df.iloc[stop:]
    # noinspection PyUnboundLocalVariable
    sub_df.to_csv(f"{save_path}{proj_name}_code_upload{i}.csv",
                  header=['Label name', 'Annotation', 'Object type'], index=False)

# Runtime Tracking #
execution_time = round((time.time() - start_time))
execution_time_m = round(execution_time / 60)
execution_time_s = execution_time % 60
print(f"Execution time: {execution_time_m} minutes {execution_time_s} seconds.")
