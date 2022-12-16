from pip import main

def greeting():
    name = input('Thanks for contacting Tiny Space! May I have your name? ')
    print(f'Thanks, {name}!')
    return

def select_category():
    category = input('''Please select from one of the categories below using the number 1-5
                        [1]Store Locator and Hours 
                        [2]Status of Order 
                        [3]Issue with Order 
                        [4]Design Services
                        [5]Other\n''')
    if category == '1':
        store_locator_hours()
        return
    elif category == '2':
        order_status()
        return
    elif category == '3':
        order_issue()
        return
    elif category == '4':
        design_services()
        return
    elif category == '5':
        other()
        return
    else:
        select_category()
        return
    

def store_locator_hours():
    location = '2300 Riverdale Lane Boston,MA 02101'
    hours = 'Monday-Saturday from 10AM to 6PM'
    print(f'Tiny space is located at {location}.')
    print(f'The store is open {hours}')

def order_status():
    print('Sure I can help you with that.')
    full_name = input('May I have the full name on the order?')
    order_number = input('May I have the order number?')
    transfer_Elliot()
    return

def order_issue():
    print('I\'m sorry that you\'re experiencing issues with your order.')
    full_name = input('May I have the full name on the order?')
    order_number = input('May I have the order number?')
    issue = 'Could you please describe the issue with your order?'
    transfer_Chrissa()
    return

def design_services():
    print('I can definitly help you oout with your design questions!.')
    transfer_Ramon()
    return

def other():
    transfer_Trinity()
    return

def transfer_Chrissa():
    print('Thanks for providing that information. I\'m looking into this now.')
    return

def transfer_Ramon():
    design_question = input('Tell me how I may be of assistance')
    return

def transfer_Trinity():
    other_inquiry = input('No problem, please describe to me how I may be of assistance.')
    return

def transfer_Elliot():
    print('Awesome! I\'m checking the status of that order now.')
    return

def main():
    greeting()
    select_category()
    select_category()

if __name__=="__main__":
    main()