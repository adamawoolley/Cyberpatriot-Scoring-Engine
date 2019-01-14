from subprocess import Popen, PIPE

class cmd:
  def __init__(self, command, output, success, points):
    self.command = command
    self.output = output
    self.success = success
    self.points = int(points)
  def check(self):
    if Popen([self.command], shell=True, stdout=PIPE).stdout.read().decode('utf-8').strip() == self.output:
      return True
    return False

def check():

  correct = 0
  points = 0
  total = 0
  success = ''
  to_test = []
  checks = 0
  with open('scoringinfo', 'r') as file:
    for line in file.readlines():
      line = eval(line)
      if line.check():
        points += line.points
        correct += 1
        success += line.success + '\n'
      total += line.points
      checks += 1
  print(f'''
Current score {points} out of {total} possible points
Completed {correct} out of {checks} checks
{success}
''')
check()
