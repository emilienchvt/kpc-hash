from os import listdir

class Photo:
    def __init__(self, orientation, tags, photo_id):
        if orientation not in ['H', 'V']:
            raise ValueError("Unknown orientation")
        self.orientation = orientation
        self.tags = tags
        self.photo_id = photo_id

class Slide:
    def __init__(self, photos):
        if len(photos)==1:
            assert photos[0].orientation == "H"
        elif len(photos)==2:
            assert photos[0].orientation == "V" and photos[1].orientation == "V"
        else:
            raise ValueError("Bad photos in the same slides")
        self.photos = photos
        self.tags = self._get_tags()

    def _get_tags(self):
        if len(self.photos) == 1:
            return set(self.photos[0].tags)
        else:
            return set(self.photos[0].tags + self.photos[1].tags)

    def print_line(self):
        if len(self.photos)==1:
            return "{}\n".format(self.photos[0].photo_id)
        elif len(self.photos)==2:
            return "{} {}\n".format(self.photos[0].photo_id, self.photos[1].photo_id)
        else:
            raise ValueError("Bad photos in the same slides")

    def compute_score_with(self, next_slide):
        tags_in_common = self.tags.intersection(next_slide.tags)
        tags_left = self.tags.difference(next_slide.tags)
        tags_right = next_slide.tags.difference(self.tags)
        return min([len(tags_in_common), len(tags_left), len(tags_right)])

class SlideShow:
    def __init__(self, slides):
        assert type(slides) == list
        assert len(slides) > 0
        self.slides = slides

    def compute_score(self):
        score = 0
        for i in range(0, len(self.slides) - 1):
            slide = self.slides[i]
            next_slide = self.slides[i+1]
            score += slide.compute_score_with(next_slide)
        return score

    def write_output(self, filename):
        slides_count = len(self.slides)
        file = open(filename, 'w')
        file.write('{}\n'.format(slides_count))
        for slide in self.slides:
             file.write(slide.print_line())
        file.close()

class HashCodeProblem:
    def __init__(self, instance_folder='data', output_folder='output'):
        self.instance_folder = instance_folder
        self.instance_files = listdir(instance_folder)
        self.output_folder = output_folder
        self.output_files = {}
        for instance in self.instance_files:
            file = open('{}/{}'.format(self.output_folder, instance), 'w')
            file.write('')
            self.output_files[instance] = 0

    def parse_input(self, input_file):
        f = open('{}/{}'.format(self.instance_folder, input_file), 'r')
        first_line = f.readline()

        image_count = int(first_line)

        photos = []
        for i in range(image_count):
            l = f.readline()[:-1].split(' ')
            orientation = l[0]
            tag_count = l[1]
            tags = l[2:]
            photo_id = i
            photos.append(Photo(orientation, tags, photo_id))

        f.close()
        return image_count, photos

    def solve_instance(self, input_file):
        p_input = self.parse_input(input_file)
        photos = p_input[1]
        photos_h = [photo for photo in photos if photo.orientation=="H"]
        photos_v = [photo for photo in photos if photo.orientation=="V"]
        slides = [Slide([photo]) for photo in photos_h]
        for i in range(len(photos_v)//2):
            slide.append(Slide([photo_v[i], photo_v[i+1]]))
        slide_show = SlideShow(slides)
        score = slide_show.compute_score()
        slide_show.write_output("./output/"+input_file)
        return score
