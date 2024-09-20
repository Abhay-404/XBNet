import setuptools

with open("READ.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="XBNet",

	version="1.4.6",

	author="Tushar Sarkar",

	author_email="tushar.sarkar@somaiya.edu",

	# #Small Description about module
	description="XBNet is an open source project which is built with PyTorch that works as a Boosted neural network for tabular data",

	long_description=long_description,
	long_description_content_type="text/markdown",

	url="https://github.com/tusharsarkar3/",
	packages=setuptools.find_packages(),


	# if module has dependecies i.e. if your package rely on other package at pypi.org
	# then you must add there, in order to download every requirement of package



		 install_requires=[
	    "scikit-learn",  # Latest version of sklearn is part of scikit-learn
	    "numpy",        # Latest stable version of numpy
	    "pandas",        # Latest stable version of pandas
	    "matplotlib",    # Latest stable version of matplotlib
	    "torch",         # Latest stable version of PyTorch
	    "xgboost",       # Latest stable version of XGBoost
	    "tqdm"          # Latest stable version of tqdm
	],



	license="MIT",

	# classifiers like program is suitable for python3, just leave as it is.
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
