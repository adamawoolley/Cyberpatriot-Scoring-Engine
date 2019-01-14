def add():
  command = input('Command to check: ')
  output = input('Expected output: ')
  success = input('Success description: ')
  points = input('Number of points worth: ')
  with open('scoringinfo', 'a+') as file:
    file.write(f'cmd("{command}", "{output}", "{success}", "{points}")\n')

if __name__ == '__main__':
  add()
