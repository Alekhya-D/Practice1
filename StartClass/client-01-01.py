# 01-01-2022
class Client:
    name = "Sukesh"
    mobile = "99919228374"
    email = "abc@gmail.com"
    purchases = 0


def main():
    firstClient = Client()
    print('Name: ', firstClient.name)
    print('Email: ', firstClient.email)
    print('Name: ', firstClient.mobile)
    print('Name: ', firstClient.purchases)
    print('\nAfter modification')
    firstClient.name = "Mahesh"
    firstClient.email = "urs@gmail.com"
    firstClient.purchases = 22
    print('Name: ', firstClient.name)
    # firstClient.name = "Mahi"
    print('Email: ', firstClient.email)
    print('Name: ', firstClient.mobile)
    print('Name: ', firstClient.purchases)


main()
