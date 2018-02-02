import xml.etree.ElementTree as etree

filename = r'C:\Users\perm7158\Documents\_Josh\Projects\CRM Term Conversion XML Report\2018-02-02 Term Conversion.xml'

tree = etree.parse(filename)
root = tree.getroot()
print(root)

# root[0][0][0][0][0].attrib returns a dictionary of the attributes and their contents
# {'PolicyAnnivDate': '1/1/2011 12:00:00 AM\r\n', 'AgeChgDateOrAttainedAge': '03/11\r\n28', 'ContactInformation': 'Client Name\r\n\r\n\r\n', 'Phone': 'H:\r\nM:\r\nB:\r\n\r\n', 'InsuredName': 'I: Client Name \r\nP: Payer Name \r\nO: Owner Name ', 'PlanNameOrPolicyNumber': 'TERM 80\r\n123456789', 'Amount': '100000.00\r\n', 'Premium': '100.00\r\n', 'FinalConvYear': '2099\r\n', 'PolicyYear': '9', 'StatusOrSegment': 'Active\r\n\r\n', 'JointWorkPartner': 'Rang, Joshua David 006525\r\n-------------------------\r\n'}
root[0][0][0][0][0].attrib