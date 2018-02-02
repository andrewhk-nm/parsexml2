import xml.etree.ElementTree as etree
import csv

# TODO: Get a better name for this module
# TODO: Figure out how to extract the namespace from the xml file, or learn if it will always be the same.
# DONE: Create the output file.
# TODO: Create an input dialog for the file names to parse


def extract_data(xmlns, tree):
    """ given an xml tree, output a dictionary of data

    yield {'insured': insured, 'payer': payer, 'owner': owner, 'final conversion year': final_year}
    generator
    """
    # This is where I would add more data to extract.
    # TDD

    # Find all of the ContactGroup elements
    #all_links = tree.findall('.//{_x007B_04D313F1-5010-E511-80D0-005056866F29_x007D_}ContactGroup')
    all_links = tree.findall('.//{' + xmlns + '}ContactGroup')

    # Constants for the xml key names
    KEY_INSUREDNAME = 'InsuredName'
    KEY_FINALCONVYEAR = 'FinalConvYear'

    for link in all_links:
        my_dict = link.attrib
        # link keys are ['PolicyAnnivDate', 'AgeChgDateOrAttainedAge', 'ContactInformation', 'Phone', 'InsuredName', 'PlanNameOrPolicyNumber', 'Amount', 'Premium', 'FinalConvYear', 'PolicyYear', 'StatusOrSegment', 'JointWorkPartner']
    
        # Prints the names from the report:
        # 'I: Insured Name'   <-- Create the phone call Regarding this person
        # 'P: Payer Name'
        # 'O: Owner Name'   <-- Create the phone call with this person as the Recipient
        name_block = my_dict[KEY_INSUREDNAME]
        for entry in name_block.split('\n'):
            component = entry.split(': ')
            # print('key={}, name={}'.format(component[0], component[1]))
            # print(entry.split(': '))
            if component[0] == 'I':
                # Insured
                insured = component[1].strip()
            elif component[0] == 'P':
                payer = component[1].strip()
            elif component[0] == 'O':
                owner = component[1].strip()
        final_year = my_dict[KEY_FINALCONVYEAR].strip()
        yield {'insured': insured, 'payer': payer, 'owner': owner, 'final conversion year': final_year}

def get_tree(filename):
    """ Given a filename of an xml doc, return the tree.
    """
    # TDD
    tree = etree.parse(filename)
    #root = tree.getroot()
    
    return tree

def fml_to_lcf(name):
    """ Takes a name from the format "First M Last" or "First Last"
    and returns "Last, First M" or "Last, First"

    Probably breaks if their last name has a space in it.
    """
    split_name = name.rsplit(maxsplit=1) 
    lcf = split_name[-1] + ', ' + split_name[0]
    return lcf




if __name__ == '__main__':
    #filename = r'C:\Users\perm7158\Documents\_Josh\Projects\CRM Term Conversion XML Report\2018-02-02 Term Conversion.xml'
    filename = r'C:\Users\perm7158\Documents\Visual Studio 2017\Projects\parsexml2\parsexml2\test\Term Conversion - Anonimized Test Data.xml'
    # Pulled from an example file. I'm not yet sure if it's always the same.
    xmlns = "_x007B_04D313F1-5010-E511-80D0-005056866F29_x007D_"
    
    tree = get_tree(filename)

    test_gen = extract_data(xmlns, tree)
    
    with open('./output/output.csv', mode='w', encoding='utf-8', newline='') as out_csv_file:
        # Print the csv file header
        out_csv_file.write('Due,Recipient,Assigned To,Subject,Regarding,On Behalf Of Team\n')
        phone_call_writer = csv.writer(out_csv_file, dialect='excel')
        for phone_call_details_dict in test_gen:
            # Assign the row of data
            due = '2/3/2018' # due date for phone call
            recipient = fml_to_lcf(phone_call_details_dict['owner'])
            assigned_to = 'Henning-Kolberg, Andrew' # Employee to assign the call to
            subject = 'Call RE Term Conversion'
            regarding = fml_to_lcf(phone_call_details_dict['insured'])
            on_behalf_of_team = 'Rang, Joshua David 006525'

            # write the row of data
            phone_call_writer.writerow([due, recipient, assigned_to, subject, regarding, on_behalf_of_team])
    
    
    


