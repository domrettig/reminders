import os
import argparse

FILE = os.path.expanduser('~/reminders.txt')

def update():
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-a')
  group.add_argument('-d',action='store_true')
  parser.add_argument('number',type=int,help='position in list to add or delete')
  args = parser.parse_args()
  
  with open(FILE,'r') as f:
    lines = f.readlines()

  if args.d:
    del lines[args.number]
  else:
    lines.insert(args.number,args.a+'\n')

  with open(FILE,'w') as f:
    for line in lines:
      f.write(line)

if __name__ == '__main__':
  update()