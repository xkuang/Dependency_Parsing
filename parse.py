import sys
from providedcode.transitionparser import TransitionParser
from featureextractor import FeatureExtractor
from transition import Transition
from providedcode.dependencygraph import DependencyGraph

files = sys.stdin.readlines()
tp = TransitionParser.load(sys.argv[1])

for sentence in files:
	dg = DependencyGraph.from_sentence(sentence)
	parsed = tp.parse([dg])
	print parsed[0].to_conll(10).encode('utf-8')
