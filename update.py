import os
import argparse

FILE = os.path.expanduser('~/reminders.txt')

def update(op, info):
  with open(FILE, 'r') as f:
    lines = f.readlines()

  if op == 'add':
    lines.append(info+'\n')
  else:
    del lines[int(info)]

  with open(FILE, 'w') as f:
    for line in lines:
      f.write(line)

def update_args():
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-a')
  group.add_argument('-d',action='store_true')
  parser.add_argument('number',type=int,help='position in list to add or delete')
  args = parser.parse_args()
  
  if args.number < 1:
    raise argparse.ArgumentTypeError('Enter a number greater than 0')

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