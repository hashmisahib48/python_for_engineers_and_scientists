"""Weibull analysis of fracture strengths (Chapter 13)."""
import numpy as np


def rank_prob(n):
    """Failure probabilities (i - 0.5)/n, i = 1..n (ASTM C1239)."""
    return (np.arange(1, n + 1) - 0.5) / n


def weibull_fit(strength):
    """Return modulus m and characteristic strength s0.

    Least-squares line through the Weibull plot,
    y = ln(ln(1/(1 - F))) against x = ln(strength).
    """
    s = np.sort(np.asarray(strength))
    x = np.log(s)
    y = np.log(-np.log(1 - rank_prob(len(s))))
    m, c = np.polyfit(x, y, 1)          # slope m, intercept c
    return m, np.exp(-c / m)


def p_fail(stress, m, s0):
    """Weibull probability of failure at a stress (MPa)."""
    return 1 - np.exp(-(stress / s0)**m)
