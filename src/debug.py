from utils import HashCodeProblem
from utils import Photo
from utils import Slide
from utils import SlideShow

problem = HashCodeProblem(instance_folder='test_data', output_folder='test_output')
example_in = problem.parse_input('a_example.txt')
example_photos = example_in[1]
print("orientations:")
print([p.orientation for p in example_photos])

slide_1 = Slide([example_photos[0]])
slide_2 = Slide([example_photos[3]])
slide_3 = Slide([example_photos[1], example_photos[2]])

slideshow = SlideShow([slide_1, slide_2, slide_3])
print(slideshow.compute_score())
assert slideshow.compute_score() == 2

slideshow.write_output('coucou.txt')
