#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

#e ^ (x - max(x)) / sum(e^(x - max(x))
#By using the fact that a^(b - c) = (a^b)/(a^c) we have
#	= e ^ x / (e ^ max(x) * sum(e ^ x / e ^ max(x)))
#	= e ^ x / sum(e ^ x)


def softmax(x):
	return np.exp(x)/np.sum(np.exp(x), axis=0)

##Example
print softmax([1,-2,0.5])
