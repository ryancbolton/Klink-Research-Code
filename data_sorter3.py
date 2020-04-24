# import pandas for file manipulation and jinja2 for styling

import csv
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


def display_menu():
    print("| What action would you like to perform?: |")
    print("|-----------------------------------------|")
    print("| 1. Open a new file.                     |")
    print("| 2. Search for gene by gene name.        |")
    print("| 3. Search for gene by indicator.        |")
    print("| 4. Exit the program.                    |")
    print("|-----------------------------------------|")

    while True:
        choice = None
        try:
            choice = input("Enter the number of your menu option: ")
            if int(choice) <= 0:
                print("Input must be a positive integer! Try again.")
                continue
            elif int(choice) >= 5:
                print("Input must be in range 1-4! Try again")
                continue
        except ValueError:
            print("Input must be a whole integer 1, 2, 3, or 4! Not a string or float.")
            continue
        break

    return str(choice)


def open_file():
    # file name is "raw DCM minus 9 dpi.csv"
    # file = input("Please enter the name of your file. It must include the .csv or .xlsx tag at the end:")
    # file = open(file, encoding='utf-8-sig')

    # Tries to open file, throwing error and re-looping if it fails
    while True:
        file = input("Please enter the name of your file. It must include the .csv tag at the end:")
        try:
            # hardcoded version to avoid typing address every time
            # new panda code: df = pd.read_csv('raw DCM minus dpi.csv')

            # attempt to read file by chunks (uses less memory if file consists of millions of rows)
            chunksize = 100000
            df = pd.read_csv(file, chunksize=chunksize)
            # df = pd.read_csv(file)
            df = pd.concat(df, ignore_index=True)
            # file = open(file, "r+",  encoding='utf-8-sig')  # or "a+", whatever you need
        except IOError:
            print("Could not open file! Please try entering again.")
            continue
        break

    # new code to parse out AFFX Indicator data:
    # Get names of indexes for which column Indicator contains AFFX
    indexindicators = df[df['Indicator'].str.contains("AFFX")].index
    # Delete these row indexes from dataFrame
    df.drop(indexindicators, inplace=True)

    # Deletes indicator column for value comparison (if preferred)
    # del df['Indicator']

    # filters only rows in which the selected cell (indicator) for every gene has a day time point < or > than 0.05
    i = 1
    for df.iteritems in df.itertuples():
        ismarked = input(f"Is time point {df.columns[i]} < 0.05 (Measured)? (Y/N): ")
        cols = [df.columns[i]]

        if ismarked == "yes" or ismarked == "Yes" or ismarked == "Y"or ismarked == "y":
            start = datetime.datetime.now()
            df[cols] = df[df[cols] <= 0.05][cols]  # replaces every element with a T/F
            finish = datetime.datetime.now()
            print("Action took", finish-start, "seconds to run")
        elif ismarked == "no" or ismarked == "No" or ismarked == "N" or ismarked == "n":
            start = datetime.datetime.now()
            df[cols] = df[df[cols] > 0.05][cols]  # replaces every element with a T/F
            finish = datetime.datetime.now()
            print("Action took", finish-start, "seconds to run")
        else:
            print("That is not an accepted input. Please enter yes/Yes/y/Y, or no/No/n/N")
            continue
        i += 1
        if i == len(df.columns):
            df = df.dropna()  # removes all F elements from df
            df = df.reset_index()  # adds index column starting at 0 for readability
            df = df.rename(columns={"index": "OG Index"})
            df.info(memory_usage='deep')  # shows how big the df is and gives general info about it
            df.to_csv('filteredgenes.csv')
            print("Dataframe sent to 'filteredgenes.csv'")  # currently not part of .exe application

            # FOR PLOTTING:
            # df.plot() #plots the dataframe
            # plt.plot.show() #actually displays the plot in SciView

            # FOR STYLING (in beta)
            # df.style. \
            #     applymap(color_negative_red). \
            #     to_excel('styled.xlsx', engine='openpyxl')
            break
        continue


# old code for filtering indexes the manual way
#     i = 1
#     for df.columns in df:
#         df_filtered = df[
#             ((df[df.columns[1]] <= 0.05) & (df[df.columns[2]] <= 0.05)) &
#             ((df[df.columns[3]] <= 0.05) & (df[df.columns[4]] <= 0.05)) &
#             ((df[df.columns[5]] <= 0.05) & (df[df.columns[6]] <= 0.05)) &
#             ((df[df.columns[7]] <= 0.05) & (df[df.columns[8]] <= 0.05)) &
#             ((df[df.columns[9]] <= 0.05) & (df[df.columns[10]] <= 0.05)) &
#             ((df[df.columns[11]] <= 0.05) & (df[df.columns[12]] <= 0.05)) &
#             ((df[df.columns[13]] <= 0.05) & (df[df.columns[14]] <= 0.05)) &
#             ((df[df.columns[15]] <= 0.05) & (df[df.columns[16]] <= 0.05)) &
#             ((df[df.columns[17]] <= 0.05) & (df[df.columns[18]] <= 0.05))
#         ]
#     i += 1

# print(df_filtered)

# df = df[df.columns <= 0.05]
# for df.object in df.columns:
#     new_df = df[df.object <= 0.05]
#     new_df.to_csv("filteredgenes.csv")

# df = df.apply(lambda x: x.sort_values().values)
# print(df.columns)
# df = df[df['Pek-0 dpi-R1'] <= 0.05]  # gets all rows that contain a value for this time point less than 0.05
# print(df)

# new_df = df.reset_index()
#
#
# print(new_df)
# print(df_filtered)

# del df_filtered['index'] # removes old index row (may or may not want this)
# df = df.reset_index()  # adds row of new indexes starting from 0
# df[df.columns] = df[df[df.columns] <= 0.05][df.columns]
# df.dropna()
# df.to_csv('filteredgenes.csv')  # currently works!


# reader = csv.reader(file)
# headers = next(reader, None)
#
# column = {}
# for h in headers:
#     column[h] = []  # turns every item in "column" into an open list
#
# for row in reader:
#     for h, v in zip(headers, row):
#         column[h].append(v)
#
#         zip(*column.values())
# keys = column.keys()
# lis = [dict(zip(keys, vals)) for vals in zip(*(column[k] for k in keys))]
#
# # Writes list of dictionaries to txt file
# outfile = "genes_sorted.txt"
# with open(outfile, 'w') as fout:
#     new_lis = (sorted(lis, key=lambda kv: (kv['Pek-0 dpi-R1'], kv['Pek-0 dpi-R2'], kv['Pek-0 dpi-R3'],
#                                            kv['Pek-3 dpi-R1'], kv['Pek-3 dpi-R2'], kv['Pek-3 dpi-R3'],
#                                            kv['Pek-6 dpi-R1'], kv['Pek-6 dpi-R2'], kv['Pek-6 dpi-R3'],
#                                            kv['88-0 dpi-R1'], kv['88-0 dpi-R2'], kv['88-0 dpi-R3'],
#                                            kv['88-3 dpi-R1'], kv['88-3 dpi-R2'], kv['88-3 dpi-R3'],
#                                            kv['88-6 dpi-R1'], kv['88-6 dpi-R2'], kv['88-6 dpi-R3'])))
#     fout.write(str(new_lis))
#
# # Writes list of dictionary to excel file
# toCSV = new_lis
# keys = toCSV[0].keys()
# with open('genes_sorted.csv', 'w') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(toCSV)
#
# return new_lis

# def color_negative_red(val):
#     # val = 0
#     file = open('filteredgenes.csv')
#     chunksize = 100000
#     df = pd.read_csv(file, chunksize=chunksize)
#     # df = pd.read_csv(file)
#     df = pd.concat(df, ignore_index=True)
#     """
#     Takes a scalar and returns a string with
#     the css property `'color: red'` for negative
#     strings, black otherwise.
#     """
#     # df_filtered = pd.DataFrame()
#     # for df.iteritems in df.iterrows():
#     if val in df:
#     # if int(df.iloc[row[0], val]) < 0.05:
#         color = 'red'
#     else:
#         color = 'white'
#         # i += 1
#         # continue
#     return 'color: %s' % color

def gene_search(new_lis):
    class Gene:
        def __init__(self, name="", indicator=""):
            self._name = name
            self._indicator = indicator

            # getter method

        def get_name(self):
            return self._name

        def get_indicator(self):
            return self._indicator

            # setter method

        def set_name(self, x):
            self._name = x

        def set_indicator(self, y):
            self._indicator = y

    gene = Gene()

    while True:
        genename = input("What gene are you looking for?")
        for k, v in new_lis:
            if k == str(genename):
                # setting gene name using setter
                gene.set_name(k)

                # retrieving gene name using getter
                print(gene.get_name())
                print(gene._name)
            else:
                print("Gene name not found. Try again.")
                continue
        break


# file = input("Please enter the name of your file. It must include the .csv or .xlsx tag at the end:")
# file = open("raw DCM minus 9 dpi.csv", encoding='utf-8-sig')
# reader = csv.reader(file)
# headers = next(reader, None)

# print(headers)

# column = {}
# for h in headers:
#     column[h] = []  # turns every item in "column" into an open list

# print(column)

# for row in reader:
#     for h, v in zip(headers, row):
#         column[h].append(v)
#
#         zip(*column.values())
# keys = column.keys()
# lis = [dict(zip(keys, vals)) for vals in zip(*(column[k] for k in keys))]

# sorted_dict = sorted(column.items(), key=lambda kv: kv[1])

# # Writes list of dictionaries to txt file
# outfile = "genes_sorted.txt"
# with open(outfile, 'w') as fout:
#     new_lis = (sorted(lis, key=lambda kv: (kv['Pek-0 dpi-R1'], kv['Pek-0 dpi-R2'], kv['Pek-0 dpi-R3'],
#                                            kv['Pek-3 dpi-R1'], kv['Pek-3 dpi-R2'], kv['Pek-3 dpi-R3'],
#                                            kv['Pek-6 dpi-R1'], kv['Pek-6 dpi-R2'], kv['Pek-6 dpi-R3'],
#                                            kv['88-0 dpi-R1'], kv['88-0 dpi-R2'], kv['88-0 dpi-R3'],
#                                            kv['88-3 dpi-R1'], kv['88-3 dpi-R2'], kv['88-3 dpi-R3'],
#                                            kv['88-6 dpi-R1'], kv['88-6 dpi-R2'], kv['88-6 dpi-R3'])))
#     fout.write(str(new_lis))
#
#
# # Writes list of dictionary to excel file
# toCSV = new_lis
# keys = toCSV[0].keys()
# with open('genes_sorted.csv', 'w') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(toCSV)

def main():
    print("Main Menu")

    while True:
        choice = display_menu()

        if choice == "1":
            open_file()
        elif choice == "2":
            # lis = open_file()
            gene_search(open_file())
            print("Blog cleared")
        # elif choice == "3":
        elif choice == "4":
            exit()


main()
