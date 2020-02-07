
while True:
    user_input = input('What is the weather today?   ').lower().strip()
    if user_input == 'rainy and stormy':
        print('Stay home')
    elif user_input == 'sunny':
        print('Take your shorts!')
    elif user_input == 'stormy':
        print('Take rain coat')
    elif user_input == 'rainy':
        print('Take your umbrella')
    elif user_input == 'no more magic':
        break
    else:
        print("Sorry, I didn't get that")
