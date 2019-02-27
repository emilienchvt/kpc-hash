

from src.utils import HashCodeProblem

problem = HashCodeProblem()

input_name = 'd_big.in'
output_name = input_name[0] + '_submit.in'


input_ = problem.parse_input(input_name)
# input_ = (3, 5, 1, 6, ['TTTTT', 'TMMMT', 'TTTTT'])

a_divisors_pairs = [(1, 6), (2, 3), (3, 2), (6, 1)] # Hard Coded for H = 6
b_divisors_pairs = [(1, 5), (5, 1)] # Hard Coded for H = 5
c_divisors_pairs = [(1, 12), (2, 6), (3, 4), (4, 3), (6, 2), (12, 1)] # Hard Coded for H = 12
d_divisors_pairs = [(1, 14), (2, 7), (7, 2), (14, 1)] # Hard Coded for H = 14
divisors_pairs_dic = {'a' : a_divisors_pairs, 'b' : b_divisors_pairs, 'c' : c_divisors_pairs, 'd' : d_divisors_pairs}

pizza_dims = (input_[0], input_[1])
pizza_grid = input_[-1]
min_ingred = input_[2]
divisors_pairs = divisors_pairs_dic[input_name[0]]


def create_slices(pizza_dims, slice_dims):

	slices_toplefts = []
	i = 0

	while i <= pizza_dims[0]:

		j = 0

		while j <= pizza_dims[1]:

			slices_toplefts.append((i, j))
			j += slice_dims[1]

		i += slice_dims[0]

	return slices_toplefts

#print(create_slices(pizza_dims, slice_dims))

def score_slices(slices_toplefts, slice_dims, min_ingredients, pizza_grid):

	score = 0
	slices_kept = []

	for slice_topleft in slices_toplefts:

		potential_slice_score = 0
		count_ing = {'T' : 0, 'M' : 0}

		i, j = slice_topleft[0], slice_topleft[1]

		k = 0
		while k < (slice_dims[0]):

			l = 0
			while l < (slice_dims[1]):

				try:
					cell_ing = pizza_grid[i + k][j + l]
					count_ing[cell_ing] += 1
					potential_slice_score += 1
				except IndexError: # La part dépasse les limites de la pizza
					break

				l += 1

			k += 1

		if count_ing['T'] >= min_ingredients and count_ing['M'] >= min_ingredients:
			score += potential_slice_score
			slices_kept.append(str(slice_topleft[0]) + ' ' + str(slice_topleft[1]) + ' ' + str(slice_topleft[0] + slice_dims[0] - 1) + ' ' + str(slice_topleft[1] + slice_dims[1] - 1))

	return score, slices_kept


def get_results(pizza_dims, divisors_pairs, min_ingred, pizza_grid):

	best_score = 0
	best_slices = []

	for slice_dims in divisors_pairs:

		slices = create_slices(pizza_dims, slice_dims)
		score, slices_kept = score_slices(slices, slice_dims, min_ingred, pizza_grid) 

		if score > best_score:
			best_score, best_slices = score, slices_kept

	return best_score, best_slices


out_score, out_slices = get_results(pizza_dims, divisors_pairs, min_ingred, pizza_grid)

file = open(output_name, 'w')

# Write number of slices
n_slices = len(out_slices)
file.write('{}\n'.format(n_slices))
# Write slices coords
for out_slice in out_slices:
	file.write('{}\n'.format(out_slice))
file.close()
print('\nYou scored', out_score, 'on', input_name)
print('Submit file saved in {}'.format(output_name))




















