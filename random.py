# def keeps_balance(balance):
#     """
#     keeps the balance always positive
#     balance:float, current balance
#     """
#     if balance < 10:
#         balance += 10
    
#     return balance

# def check_overweight(weight, height):
#     if 18.5 <= weight / height**2 < 25:
#         print('your weight is normal')
#     else:
#         print('you are overweight, control your diet')

# def which_prize(points):
#     if points <= 50:
#         print('your prize is {}'.format('wooden rabbit'))
#     elif points <= 150:
#         print('no prize')
#     elif points <= 180:
#         print('wafer-thin mint')
#     else:
#         print('penguin')

# #print(keeps_balance(9))
# which_prize(10)

# check_overweight(73, 1.72)

# altitude = 10000
# speed = 250
# propulsion = "Propeller"

# print((altitude > 500 and speed > 100) or not propulsion == "Propeller")

# names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']

# for name in names:
#     name = name.title()

# print(names)

def html_list(l):
    html = []
    html.append('<ul>')
    for i in l:
        html.append('<li>{}</li>'.format(i))
    html.append('</ul>')
    return '\n'.join(html)
    
print(html_list(['first string', 'second string']))

for i in range(100):
    print(i)