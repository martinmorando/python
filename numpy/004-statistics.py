'''
    Statistics
'''

import numpy as np

survey = [2, 4, 3, 3, 2, 1, 1, 4, 2, 3, 3]
survey_array = np.array(survey)

# Mean
print(np.mean(survey_array))    # Output: 2.5454545454545454

# Median
print(np.median(survey_array))  # Output: 3.0

# Sort
print(np.sort(survey_array))    # Output: [1 1 2 2 2 3 3 3 3 4 4]
