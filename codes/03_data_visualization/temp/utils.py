def print_df_info(df):
    print('='*15)
    print('------ HEAD -----')
    print(df.head())
    print('------ TAIL -----')
    print(df.tail())
    print('------ Shape -----')
    print(df.shape)
    print('------ Count -----')
    print(df.count())


TEST_VAR = 10