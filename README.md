# kpc-hash

## Clone the repo

And then cd inside

```bash
git clone git@github.com:emilienchvt/kpc-hash.git
cd kpc-hash
```

## Create and install the env

### Python virtualenv

First chose your python interpretor (python > 3) and create your virtualenv.

```bash
virtualenv -p /usr/local/bin/python3.7 hashcode
```

Then activate it

```bash
source hashcode/bin/activate
```

Intstall the requirements

```
pip install -r requirements.txt
```


### Anaconda

## Start the notebook

To open the notebook:

```bash
jupyter notebook data_analysis.ipynb
```

## Schedule

### Discover the subject

45 minutes top (15 minutes by ourselves + 30 minutes discussion)

#### General Stuff
* What is the problem?
* What is the metric?
* What are the variables?

#### Technical Stuff
* How to load the data?
* How to write submissions?
* What objects can we build? (Cars/ rides/ Slices)
* What methods we want for these objects?
* How to compute the evaluation metric from the previous?
* What are the metrics to monitor in our solution (Number of missed rides, Number of slides)?

#### Greedy Solution
* Is there an easy way to get a benchmark (Quick estimation of the complexity)?

### First implementation

Pairs of two.
45 minutes top

#### Tech
* Create the ojects
* Loading and writing the data
* First easy solution
* Evaluation of this solution

#### Data
* Look at the data and try to find insights
* Are there bonuses? In which case are they importants.
* What are the metrics to monitor in our solution?


### Exchanges:

30 minutes top

## Soft
* Are there quickwins to make the solution better/ faster?
* What strategies can we think of to increase the metric?


## Data
* What did we miss when creating the first solution?
* Are there clever strategies we can apply (only long rides, leave outliers out of the algorithms)?
* Are there clusterings ta can help make the algorithm faster?

### YOLO

2h