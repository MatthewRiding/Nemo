import numpy as np


def compute_t_hyp_us(x_vector_mm, v_mpers, t_0_us):
    t_hyp_us = 10**6 * np.sqrt(((x_vector_mm * 10**-3) / v_mpers) ** 2 + (t_0_us * 10 ** -6) ** 2)
    return t_hyp_us
