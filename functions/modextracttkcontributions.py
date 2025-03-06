import numpy as np


def extract_tk_contributions(b_scan_amps, t_vector_us, x_vector_mm, v_vector_mpers, t_0_vector_us):
    # Find number of A-scans:
    n_a_scans = np.shape(x_vector_mm)[0]
    # Find number of t_0 values requested for the spectrum:
    n_t_0s = np.shape(t_0_vector_us)[0]
    # Find the number of wave speed values requested for the spectrum:
    n_vs = np.shape(v_vector_mpers)[0]

    # Sampling grid in v vs t_0 domain:
    vs_grid_mpers, t_0s_grid_us = np.meshgrid(v_vector_mpers, t_0_vector_us)

    # Calculate query times for all[vs and t_0s] for each value of x:
    # Pre - allocate output: 3D array of query times.
    # Each page has dimensions of the v / t_0 grid.
    # There is one page for each A - scan (i.e.each value of x):
    query_times_by_a_scan_3d_us = np.zeros((n_a_scans, n_t_0s, n_vs))

    # Pre-allocate space for the output v / t_0 spectrum array:
    spectrum_contributions_3d = np.zeros((n_a_scans, n_t_0s, n_vs))

    for i, x_value_mm in enumerate(x_vector_mm):
        # Fetch the A-scan for this iteration (this value of x):
        a_scan_i = b_scan_amps[:, i]
        # Calculate query times for this a_scan:
        query_times_by_a_scan_3d_us[i] = 10**6 * np.sqrt(
            ((x_value_mm * 10 ** -3 / vs_grid_mpers) ** 2) + ((t_0s_grid_us * 10 ** -6) ** 2))
        # Submit query times to A-scan:
        amplitudes_i = np.interp(query_times_by_a_scan_3d_us[i], t_vector_us, a_scan_i, 0, 0)
        # Save this as one page:
        spectrum_contributions_3d[i] = amplitudes_i

    return spectrum_contributions_3d, query_times_by_a_scan_3d_us
