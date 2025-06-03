from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import stats

import pickle
import numpy as np
import re

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


# a z-score (also called a standard score) gives you an idea of how far from the mean a data point is. 
# But more technically it’s a measure of how many standard deviations below or above the population mean a raw score is.
def scaler(data):
	return stats.zscore(np.array(d), ddof=1)


# re.sub(pattern, repl, string, count=0, flags=0)
def term_vectorizer_fit(data):
	tf = TfidfVectorizer(stop_words='english')
	clean = [re.sub("[^A-Za-z,.']", " ", x) for x in data]

	tf.fit(clean)
	return tf

def vectorizer_transform(data, file):
	vectorizer = pickle.load(open(dir_path + "\\" + file, "rb"))
	clean = [re.sub("[^A-Za-z,.']", " ", x) for x in data]

	return vectorizer.transform(clean)
