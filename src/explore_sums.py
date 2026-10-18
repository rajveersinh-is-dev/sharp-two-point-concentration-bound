"""
Explore combinatorial sums for closed-form identities.

Computes several families of binomial sums for n = 0..N and prints
values so we can look for patterns / closed forms. All computations
are exact integer arithmetic.
"""
from math import comb


def seq_sum(formula, n_max):
    """Seq sum.
    
    Args:
        formula:
        n_max:
    
    Returns:
        The computed result
    
    """
    vals = []
    for n in range(n_max + 1):
        vals.append(formula(n))
    return vals


def fam1(n):
    # Sum_{k=0..n} (-1)^k C(n,k) (k+1)^n  = (-1)^n n!   (known, finite difference)
    """Fam1.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum((-1) ** k * comb(n, k) * (k + 1) ** n for k in range(n + 1))


def fam2(n):
    # Sum_{k=0..n} C(n,k) * C(n+k, k)   (central Delannoy-related)
    """Fam2.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum(comb(n, k) * comb(n + k, k) for k in range(n + 1))


def fam3(n):
    # Sum_{k=0..n} (-1)^k C(n,k)^2 * C(n+k, k)
    """Fam3.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum((-1) ** k * comb(n, k) ** 2 * comb(n + k, k) for k in range(n + 1))


def fam4(n):
    # Sum_{k=0..n} C(n,k)^2 * C(n+k, k)   (Franel-like / Apéry-relative)
    """Fam4.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum(comb(n, k) ** 2 * comb(n + k, k) for k in range(n + 1))


def fam5(n):
    # Sum_{k=0..n} (-1)^k C(n,k) * (2k choose k)
    """Fam5.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum((-1) ** k * comb(n, k) * comb(2 * k, k) for k in range(n + 1))


def fam6(n):
    # Sum_{k=0..n} C(n,k) * C(2k,k) * C(2(n-k), n-k)
    """Fam6.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum(comb(n, k) * comb(2 * k, k) * comb(2 * (n - k), n - k) for k in range(n + 1))


def fam7(n):
    # Sum_{k=0..floor(n/2)} C(n, 2k) * C(2k, k) * 2^(n-2k)
    """Fam7.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum(comb(n, 2 * k) * comb(2 * k, k) * 2 ** (n - 2 * k)
               for k in range(n // 2 + 1))


def fam8(n):
    # Sum_{k=0..n} (-1)^k C(n,k) * C(2n - 2k, n - k)   (signed)
    """Fam8.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return sum((-1) ** k * comb(n, k) * comb(2 * n - 2 * k, n - k) for k in range(n + 1))


FAMILIES = [fam1, fam2, fam3, fam4, fam5, fam6, fam7, fam8]
NAMES = ["fam1", "fam2", "fam3", "fam4", "fam5", "fam6", "fam7", "fam8"]

if __name__ == "__main__":
    N = 16
    for name, f in zip(NAMES, FAMILIES):
        vals = seq_sum(f, N)
        print(name, ":", vals)
