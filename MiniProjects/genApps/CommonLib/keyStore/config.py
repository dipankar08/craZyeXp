#######################################################
# This is the con fig file which includes the restrictions on table.
#  
#
########################################################

CONFIG ={}

# Adding config for table<aa>
CONFIG['test'] = {
    'contrains':[('name','unique')], # add insit a list if someone is in random..
    'getAutoRandom6':['share_id_1','share_id_2'],   # add if you want to be automated random value while insert.
    'notnull':['email'], # list your attribute which can't be null 
    'explore':['table_test'] # This will explore any reference table and include the result.    
}
#Adding config for test1
CONFIG['test1'] = {
    'contrains':[('name','unique')], # add insit a list if someone is in random..
    'explore':['table_test'] # This will explore any reference table and include the result.    Working fine
}
