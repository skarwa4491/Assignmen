########################## create user test data ###################################
single_user = ('6', 'tywin11', 'tywinn', 'lanister', 'tywin@yopmail.com', 'Admin@123', '523523432')
multiple_user = [
    ('1', 'red_keep_111', 'Cersi', 'Lanister', 'cersi.l@yopmail.com', 'Admin@123', '43242142'),
    ('2', 'westros_111', 'Jammy', 'Lanister', 'jammy.l@yopmail.com', 'Admin@123', '25323423')
]
create_user_response_valid_keys = ['code', 'type', 'message']

############################### get_user_data #######################################

error_response_keys = ['code' , 'type' , 'message']
error_message = 'User not found'
type = 'error'

########################## update user test data ###################################

single_user_update = ('6', 'tywin11_updated', 'tywinn', 'lanister', 'tywin2@yopmail.com', 'Admin@123', '523523432')
multiple_user_update = [
    ('1', 'red_keep_111_updated', 'Cersi', 'Lanister', 'cersi.l@yopmail.com', 'Admin@123', '43242142'),
    ('2', 'westros_111_updated', 'Jammy', 'Lanister', 'jammy.l@yopmail.com', 'Admin@123', '25323423')
]
update_response_valid_keys = ['code', 'type', 'message']