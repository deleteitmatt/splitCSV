import pandas as pd

# CONFIGURE LINES 5-8 BEFORE RUNNING #
excel_path = "/Users/mattbenedict/Desktop/script testing/WIP_Prostream_error_codes.xlsx"
save_path = "/Users/mattbenedict/Desktop/script testing/"
proj_name = "Prostream"
rows_per_file = 1000
# remove 'Annotation' in ln 19 + 25 if you are preparing a file for deleting labels #

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
    sub_df.to_csv(f"{save_path}{proj_name}_code_upload{i+1}.csv",
                  header=['Label name', 'Annotation', 'Object type'], index=False)
