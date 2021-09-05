from pprint import pprint
import random

def sample_dict(target_dict, n=2):
    target_keys = list(target_dict.keys())
    random_keys = random.sample(target_keys,n)
    for key in random_keys:
        print (key)
        pprint (target_dict[key])
    return
