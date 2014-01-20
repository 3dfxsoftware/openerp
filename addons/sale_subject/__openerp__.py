#determines the XML files that will be parsed during the initialization of teh sever and aslo to determine 
#the dependencies of the created module
#init xml had data that will load to DB at the moment of install
#upate xml has data when install or update
#data has xml, csv with data that will load to DB at moment when you install or update module
{
    'name': "Sale Quotation Subject",
    'version': "1.0",
    'author': "Real Time Solutions Pvt. Ltd",
    'category': "Technical Settings",
    'depends':['base','sale'],
    'data':['sale_subject.xml'],
    'demo':[],
    'installable': True,
}