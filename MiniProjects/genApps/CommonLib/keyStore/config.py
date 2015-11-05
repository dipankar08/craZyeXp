#######################################################
# This is the con fig file which includes the restrictions on table.
#  
#
########################################################

CONFIG ={}

# Adding config for table<aa>
CONFIG['test'] = {
    'contrains':[('name','unique')], # add insit a list if someone is in random..
    'getAutoRandom6':['share_id'],   # add if you want to be automated random value while insert.
    'notnull':[] # list your attribute which can't be null 
}