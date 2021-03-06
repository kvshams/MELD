# Copyright (C) 2020 Krishnaswamy Lab, Yale University

import warnings
import numpy as np
from nose.tools import assert_raises_regex, assert_warns_regex
import re


def assert_warns_message(expected_warning, expected_message, *args, **kwargs):
    expected_regex = re.escape(expected_message)
    return assert_warns_regex(expected_warning, expected_regex, *args, **kwargs)


def assert_raises_message(expected_warning, expected_message, *args, **kwargs):
    expected_regex = re.escape(expected_message)
    return assert_raises_regex(expected_warning, expected_regex, *args, **kwargs)


def reset_warnings():
    warnings.resetwarnings()
    warnings.simplefilter("error")
    ignore_numpy_warning()


def ignore_numpy_warning():
    warnings.filterwarnings(
        "ignore",
        category=PendingDeprecationWarning,
        message="the matrix subclass is not the recommended way to represent "
        "matrices or deal with linear algebra ",
    )


reset_warnings()


def make_batches(n_pts_per_cluster=5000):
    datas = []
    labels = []

    def make(x, y, s):
        data = np.concatenate(
            [
                np.random.normal(x, s, (n_pts_per_cluster, 1)),
                np.random.normal(y, s, (n_pts_per_cluster, 1)),
            ],
            axis=1,
        )
        return data

    # batch 1
    data = [make(0, 0, 0.1), make(1, 1, 0.1), make(0, 1, 0.1)]
    label = np.zeros(len(data) * n_pts_per_cluster)
    data = np.concatenate(data, axis=0)

    datas.append(data)
    labels.append(label)

    # batch 2
    data = [make(1, -1, 0.1), make(2, 0, 0.1), make(-2, -1, 0.1)]
    label = np.ones(len(data) * n_pts_per_cluster)
    data = np.concatenate(data, axis=0)

    datas.append(data)
    labels.append(label)

    datas = np.concatenate(datas, axis=0)
    labels = np.concatenate(labels, axis=0)
    labels = np.array(["expt" if label else "ctrl" for label in labels])

    return datas, labels
