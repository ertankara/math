print('Finding greatest common factor...')
print('Enter numbers, when done say "done"')

num_list = []
current_num = -1
input_num = ''

while input_num != 'done':
    input_num = input('num: ')
    try:
        current_num = int(input_num)
        if current_num in num_list:
            print('no duplicates necessary')
        else:
            num_list.append(current_num)
    except:
        if input_num != 'done':
            print('skipping invalid number...')
        continue

factor_sets = []

for index, num in enumerate(num_list):
    factor_sets.append([])
    for factor in range(1, num + 1):
        if num % factor == 0:
            factor_sets[index].append(factor)


common_factors = []
flat_factors = []

for factor_set in factor_sets:
    for num in factor_set:
        if num not in flat_factors:
            flat_factors.append(num)

greatest_factor = max(*flat_factors)

for num in range(greatest_factor + 1):
    match_count = 0
    for factor_set in factor_sets:
        if num in factor_set:
            match_count += 1

    if match_count == len(factor_sets):
        common_factors.append(num)

print('common_factors', common_factors)
print('greatest common factor is', 'not found' if len(common_factors) ==
      0 else common_factors[0] if len(common_factors) == 1 else max(*common_factors))
