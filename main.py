# Import the class
from src.utils import HashCodeProblem, Photo, Photo, SlideShow, Slide
import os

files = os.listdir("./data")

for f in files:
    # Instantiate
    print(f)
    problem = HashCodeProblem()
    problem.solve_instance(f)