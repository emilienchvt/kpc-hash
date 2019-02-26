from os import listdir

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

        row_count, column_count, min_ingredients, max_area = tuple(map(int, first_line.split(' ')))

        grid = []
        for i in range(row_count):
            grid.append(f.readline().rstrip())

        f.close()
        return row_count, column_count, min_ingredients, max_area, grid

    def solve_instance(self, row_count, column_count, min_ingredients, max_area, grid, debug=False):
        result_slices = []
        for r in range(row_count):
            if debug:
                print('Column {}'.format(r))
            counts = {
                "T":0,
                "M":0,
            }
            beg=0
            i=0
            while i<column_count:
                if debug:
                    print('Cursor {}'.format(i))
                counts[grid[r][i]]+=1
                if counts['T'] > min_ingredients and counts['M'] > min_ingredients and i-beg+1<=max_area:
                    result_slices.append((r, beg, r, i))
                    beg=i+1
                    counts = {
                        "T":0,
                        "M":0,
                    }
                i+=1
        return result_slices

    def compute_score(self, result_slices):
        return sum([(c2-c1+1) * (r2-r1+1) for ((r1, c1, r2, c2)) in result_slices])

    def format_output(self, result_slices, output_name, test=False):
        file = open(output_name, 'w')
        n_slices = len(result_slices)
        score = self.compute_score(result_slices)
        if score > self.output_files[output_name]:
            self.output_files[output_name] = score
            file.write('{}\n'.format(n_slices))
            if test:
                print('{}\n'.format(n_slices))
            else:
                print('You scored {}'.format(score))
            for result_slice in result_slices:
                r1, c1, r2, c2 = result_slice
                file.write('{} {} {} {}\n'.format(r1, c1, r2, c2))
                if test:
                    print('{} {} {} {}\n'.format(r1, c1, r2, c2))
            file.close()
            print('Saved in {}'.format(output_name))
        else:
            print('Scored {}, less than current score {}'.format(score, self.output_files[output_name]))

    def solve_instances(self, instances):
        for instance in instances:
            instance_data = self.parse_input(instance)
            slices = self.solve_instance(*instance_data)
            self.format_output(slices, instance)

    def solve_all_instances(self):
        self.solve_instances(self.instance_files)
