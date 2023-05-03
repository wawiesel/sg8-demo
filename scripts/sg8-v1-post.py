import pandas as pd
import sys
import os
from collections import defaultdict
from tqdm import tqdm
import csv

# set to true to generate debugging output
debug = False

# function to parse a full case name like
# HEU-COMP-FAST-002-001 and return the last 001
#                   ---
def case_parse(full_case):
    if full_case == "(REJECTED)":
        case0 = -1
    elif full_case == "":
        case0 = 0
    else:
        case0 = int(full_case.split("-")[-1])
    return case0


# function to take the full case name like
# HEU-COMP-FAST-002-001 and a special sequence of
# cases to add like "5-9,13" and expand it to the
# case list of 1,5,6,7,8,9,13. The keyword 'ALL'
# implies all cases found in scanning the excel
# sheet.
def case_list(full_case, add_cases, all_cases):
    case0 = case_parse(full_case)
    cases = list()
    if add_cases == "":
        cases.append(case0)
    else:
        for c in add_cases.split(","):
            if c == "ALL":
                cases.extend(all_cases)
            else:
                c_list = c.split("-")
                if len(c_list) > 1:
                    cases.extend(list(range(int(c_list[0]), int(c_list[1]) + 1)))
                else:
                    cases.append(int(c_list[0]))
    return list(set(cases))


# reads a specially formatted Excel data file with benchmark feedback
def process_excel_file(input_file):

    # get excel sheet data
    header = pd.read_excel(input_file, nrows=11, header=None)
    c_author = header.loc[5, 2]
    c_email = header.loc[5, 4]

    # get ratings data
    print("Reading data from:", input_file)
    data = pd.read_excel(input_file, skiprows=13, usecols="B:I")
    data = data.fillna("")

    # print data for debugging
    if debug:
        print(data)

    # create the ALL case range
    all_cases = defaultdict(list)
    for index, row in tqdm(
        data.iterrows(), desc="Scanning for all cases", ascii=False, ncols=75
    ):
        iden = row["Identifier"]
        full_case = row["Case"]
        case0 = case_parse(full_case)
        all_cases[iden].append(case0)

    # print all cases for debugging
    if debug:
        print(all_cases)

    # create a list element for each records row
    records = list()
    for index, row in tqdm(data.iterrows(), "Processing rows", ascii=False, ncols=75):
        # only add data with a rating
        c_rating = row["Rating"]
        if c_rating != "":
            # extract data
            c_iden = str(row["Identifier"])
            full_case = str(row["Case"])
            c_rev = int(row["Rev."])
            add_cases = str(row["Add Cases*"])
            c_issue_keys = set(str(row["Issue Keys**"]).split(","))
            c_improvements = str(row["Improvements Recommended"] or "")
            c_notes = str(row["Additional Notes"] or "")

            # expand to a case list (repeating the above data for each case)
            for case in case_list(full_case, add_cases, all_cases[iden]):

                # reconstruct full_case identifier
                if case == -1:
                    c_case="REJ"  # rejected
                else:
                    c_case = "{:03d}".format(case)
                c_mat, c_form, c_spec, c_index = c_iden.split('-')

                # create a record with all the data
                records.append(
                    {
                        "Identifier": str(c_iden),
                        "Mat": str(c_mat),
                        "Form": str(c_form),
                        "Spec": str(c_spec),
                        "Index": str(c_index),
                        "Case": str(c_case),
                        "Rev": int(c_rev),
                        "Author": str(c_author),
                        "Rating": "{:2.1f}".format(c_rating),
                        "ModelIssue": "M" in c_issue_keys,
                        "BiasIssue": "B" in c_issue_keys,
                        "UncertaintyIssue": "U" in c_issue_keys,
                        "ImprovementsRecommended": str(c_improvements),
                        "AdditionalNotes": str(c_notes),
                    }
                )
    if debug:
        print(*records, sep="\n")

    # convert records data to a data frame
    df = pd.DataFrame(data=records)

    # replace newlines with spaces and double spaces with single
    df = df.replace('\n',' ', regex=True)
    df = df.replace('\s+',' ', regex=True)

    return df


def main():

    # input file from which we read data
    input_file = sys.argv[1]

    # archive file we merge new data into
    archive_file = sys.argv[2]

    if input_file.lower().endswith((".xlsx")):
        df = process_excel_file(input_file)
    else:
        df = pd.read_csv(input_file)

    # if the archive file exists, append to it.
    if os.path.exists(archive_file):
        print("Updating existing:", archive_file)

        # use a custom index to ensure the combine happens as expected
        df_index = ["Case", "Rev", "Author"]
        df.set_index(df_index, inplace=True)

        # read the old data and update the index as well
        dfa = pd.read_csv(archive_file)
        dfa.set_index(df_index, inplace=True)

        # combine first (also called "upsert" which is a combination of
        # updating existing and inserting). the data frame with priority
        # should call combine first.
        df = df.combine_first(dfa)

        # reset the index so the CSV output is complete
        df.reset_index(inplace=True)

    updated = open(archive_file, "w")
    updated.write(df.to_csv(index=False, header=True, quoting=csv.QUOTE_NONNUMERIC))
    updated.close()
    print("Done.")


main()
