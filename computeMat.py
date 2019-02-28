import numpy as np
import pandas as pd
import scipy.sparse

from src.utils import Photo, Slide, SlideShow, HashCodeProblem
from scipy.spatial.distance import cdist
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def myDist(x,y):
	return (x - y > 0)

def compute_mat(filename='a_example.txt'):

	hsh = HashCodeProblem()
	pics = hsh.parse_input(filename)
	n = pics[0]
	pics = pics[1]

	tags_set = set([tag for photo in pics for tag in photo.tags])
	tags = [photo.tags for photo in pics]

	label_encoder = LabelEncoder()
	tags_set_lo = label_encoder.fit_transform(list(tags_set))
	#tags_lo = np.ndarray([label_encoder.transform(t).tolist() for t in tags])
	tags_lo = [label_encoder.transform(t).tolist() for t in tags]

	# binary encode
	onehot_encoder = OneHotEncoder(sparse=False)
	#tags_lo = tags_lo.reshape(len(tags_lo), 1)
	#tags_oo = onehot_encoder.fit_transform(tags_lo)
	tags_set_oo = onehot_encoder.fit_transform(tags_set_lo.reshape(len(np.asarray(tags_set_lo)),1))
	tags_set_oo

	tags_oo = [onehot_encoder.transform(np.asarray(t).reshape(len(np.asarray(t)),1)) for t in tags_lo]
	tags_oo = np.concatenate(tags_oo)

	M_sc = np.dot(tags_oo,tags_oo.T)
	M_diff1 = cdist(tags_oo,tags_oo,myDist)

	return np.min((M_sc,M_diff1,M_diff1.T))