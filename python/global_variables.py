


#################################################################
############### Create params dictionary ########################
#################################################################


def func1(params):
    print(params['name'])
    pass


params = {
    'name': 'value 1'
}

func1(params)

# Add new variables from any function which has access to params variable

#################################################################
############### Create empty class dictionary ###################
#################################################################

# These would be  global

class flags:
    pass

FLAGS = flags()

FLAGS.type2_name = "Value 2"

print(FLAGS.type2_name)

# Add new variables from anywhere. Its global

#################################################################
############### import from external file #######################
#################################################################

import extras.var_example as var

print(var.file1_var)

# Append new variables dynamically to the file and read from them

