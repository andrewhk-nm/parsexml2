import xml.etree.ElementTree as etree



def extract_data(xmlns, root):
    """ given an xml node, output a dictionary of data

    yield {'insured': insured, 'payer': payer, 'owner': owner}
    generator
    """
    # This is where I would add more data to extract.
    # TDDS

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

def get_root(filename):
    """ Given a filename of an xml doc, return the root.
    """
    # TDD
    tree = etree.parse(filename)
    root = tree.getroot()
    
    return root

if __name__ == '__main__':
    filename = r'C:\Users\perm7158\Documents\_Josh\Projects\CRM Term Conversion XML Report\2018-02-02 Term Conversion.xml'
    # Pulled from an example file. I'm not yet sure if it's always the same.
    xmlns = "_x007B_04D313F1-5010-E511-80D0-005056866F29_x007D_"
    
    root = get_root(filename)

    test_gen = extract_data(xmlns, root)
    for item in test_gen:
        print(item)

    # root[0][0][0][0][0].attrib returns a dictionary of the attributes and their contents
    # {'PolicyAnnivDate': '1/1/2011 12:00:00 AM\r\n', 'AgeChgDateOrAttainedAge': '03/11\r\n28', 'ContactInformation': 'Client Name\r\n\r\n\r\n', 'Phone': 'H:\r\nM:\r\nB:\r\n\r\n', 'InsuredName': 'I: Client Name \r\nP: Payer Name \r\nO: Owner Name ', 'PlanNameOrPolicyNumber': 'TERM 80\r\n123456789', 'Amount': '100000.00\r\n', 'Premium': '100.00\r\n', 'FinalConvYear': '2099\r\n', 'PolicyYear': '9', 'StatusOrSegment': 'Active\r\n\r\n', 'JointWorkPartner': 'Rang, Joshua David 006525\r\n-------------------------\r\n'}
    # root[0][0][0][0][0].attrib
