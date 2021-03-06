###FUNCTION START
def dictionary_of_metrics(items):
        ''' 
        Returns the dictionary of calculated metrics, these include the mean,
        median, varience, standard deviation, the minimum and maximum
        for the given numerical list. All returned values are
        rounded to 2 decimal places.

        Args:
            items (int or float):List of intergers or floats.


        Returns:
            dict:
            dictionary of calculated metrics for the given numerical list,
            rounded to 2 decimal places.

        Examples:
            >>>dictionary_of_metrics([5, 10.7, 25.3, 32, -1])
            {'max': 32,
            'mean': 14.4,
            'median': 10.7,
            'min': -1,
            'std': 13.85,
            'var': 191.95}
        '''

    total = 0
    count = 0
    for value in items:
        total = total + value
        count = count + 1
        the_mean = round(total / count, 2)
    sorted_items = sorted(items)
    if count % 2 == 1:
        the_median = sorted_items[int(round(count+1)/2-1)]
    else:
        lower_median = sorted_items[int(round(count/2-1))]
        upper_median = sorted_items[int(round(count/2))]
        the_median = (lower_median + upper_median) / 2
    sum_of_sqz = 0  # Calculate Sum of squares for Varience
    for j in items:
        sqrz_calc = (j - the_mean)**2
        sum_of_sqz = sum_of_sqz + sqrz_calc
    the_varience = round(sum_of_sqz / (count - 1), 2)
    the_standard_dev = round((the_varience)**(1/2), 2)
    the_min = sorted_items[0]
    the_max = sorted_items[count - 1]
    dict = {
        'mean': the_mean,
        'median': the_median,
        'var': the_varience,
        'std': the_standard_dev,
        'min': the_min,
        'max': the_max
        }
    return dict

### FUNTION END
