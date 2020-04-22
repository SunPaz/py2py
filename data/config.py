"""
	Configuration
"""
""" Byte length """
id_length = 4
""" Node ID length correpsonding to prefix (used to compute distance) """
group_prefix = 10
""" kbuckets max length (peers count per bucket) """
max_contact = 20
""" kbuckets min length (peers count per bucket), used to maintain a minimum peers count for farther distance """
min_contact = 5