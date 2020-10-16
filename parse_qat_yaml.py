###################################################################################################
#
# Copyright (C) Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
#
###################################################################################################
"""
Parses yaml file used to define Quantization Aware Training
"""

import yaml

def parse(yaml_file):
    """Parses yaml file
    """
    policy = None
    with open(yaml_file, 'r') as stream:
        try:
            policy = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    print(policy)

    if policy:
        if 'start_epoch' not in policy:
            assert False, '`start_epoch` must be defined in QAT policy'
        if 'bits_weights' not in policy:
            assert False, '`bits_weights` must be defined in QAT policy'

    return policy
