# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bmillett"
__date__ ="$Nov 12, 2010 3:56:36 PM$"

def parse_emails():
    import csv
    file_out = open('/Users/bmillett/Desktop/cpr_contacts_all.csv', 'wb')
    file_in = open('/Users/bmillett/Desktop/cpr_emails.csv', 'rb')

    writer = csv.writer(file_out)
    emailReader = csv.reader(file_in, delimiter=',', quotechar='"')

    # write the new columns
    writer.writerow(['Email', 'Name', 'State', 'Country', 'Which Properties', 'Which Packages'])

    # column order
    col_email       =0
    col_question    =1
    col_answer      =2
    col_questopt    =3

    pos_email           =0
    pos_name            =1
    pos_state           =2
    pos_country         =3
    pos_property        =4
    pos_package         =5


    last_email  = ''
    
     # Define the size of the list to the amount of columns we want (zero based)
    cur_row = [None]*6

    # Properties list for options
    properties = []

    # Properties list for options
    packages = []

    counter=0
    for row in emailReader:
        counter = counter +1

        # skip first row with column names
        if counter <=1:
            continue

        # if emails are different write a row if we have data top write
        if row[col_email] != last_email and last_email != '':

            # get the propterties options
            cur_row[pos_property] = ", ".join(properties)

            # get the packages options
            cur_row[pos_package] = ", ".join(packages)

            # Write the freakin row!
            #if last_email != bad_email:
            writer.writerow(cur_row)

            # Reset the dang row list
            cur_row = [None]*6
            
            # Reset properties
            del properties[:]

            # Reset packages
            del packages[:]

        # Store last email.
        last_email = row[col_email]

        # ovewrite the column (no problem)
        cur_row[pos_email] = row[col_email]

        if row[col_question] == 'Name':
            #if matches('^([a-z .-]|\s*)$', row[col_answer], True):
                cur_row[pos_name] = row[col_answer]
            #else:
            #    bad_email = row[col_email]
            #continue

        if row[col_question] == 'State':
            cur_row[pos_state] = row[col_questopt]
            continue

        if row[col_question] == 'Country':
            cur_row[pos_country] = row[col_questopt]
            continue

        if row[col_question] == 'What property are you interested in?':
            properties.append(row[col_questopt]);
            continue

        if row[col_question] == 'What type of fishing packages are you interested in?':
            packages.append(row[col_questopt]);

        

def matches(pat, str, icase=None):
    import re
    if icase: re.IGNORECASE
    return re.match(pat, str) is not None


if __name__ == "__main__":
    parse_emails()

