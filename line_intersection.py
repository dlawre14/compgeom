import argparse

from my_modules.geom.segment import Segment
from my_modules.geom.point import Point

from my_modules.listeners.graphicslistener import GraphicsListener
from my_modules.listeners.delaylistener import DelayListener
from my_modules.geom.utils import utils as utils
from other_modules.RedBlackTree import RedBlackTree

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Line segment intersection solver using sweep line')
  parser.add_argument('-s', type=int, help='Number of segments to generate', required=True)
  parser.add_argument('--seed', type=int, help='Seed to use for generating segments')
  parser.add_argument ('-g', action='store_true', default=False, help='add a graphical output to the program')
  parser.add_argument ('-v', action='store_true', default=False, help='add a text output to the program')
  parser.add_argument ('-d', type=float, default=0, help='add a delay to the program, -1 is for manual advance, > 0 is for a timed delay')

  args = parser.parse_args()

  listeners = []

  if args.g:
    listeners.append(GraphicsListener())
  if args.d != 0:
    listeners.append(DelayListener(args.d))

  ps = utils.pointsInRectangle(300, 300, args.s * 2,Point(200,200), args.seed)
  segments = []
  for p in range(2, len(ps)+1, 2):
    segments.append(Segment(ps[p-2], ps[p-1]))
    for l in listeners: l.segmentAdded(segments[-1])
