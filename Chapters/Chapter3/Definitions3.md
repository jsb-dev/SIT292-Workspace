# Definitions

## Chapter 3

### 3.1 Cofactors of a Matrix

Assume that determinants of (n−1)×(n−1) matrices have been defined. Given the n×n matrix A, let:

Ai j denote the (n−1)×(n−1) matrix obtained from A by deleting row i and column j.

Then the (i, j)-cofactor ci j(A) is the scalar defined by:

```
ci j(A) = (−1)i+j det(Ai j)
```

Here (−1)i+j is called the sign of the (i, j)-position.

### 3.2 Cofactor expansion of a Matrix

Assume that determinants of (n−1)×(n−1) matrices have been defined. If A = [ai j] is n×n, define:

```
det A = a11c11(A)+a12c12(A)+···+a1nc1n(A)
```

This is called the cofactor expansion of det A along row 1.

### 3.3 Adjugate of a Matrix

The adjugate4of A, denoted adj(A), is the transpose of this cofactor matrix; in symbols,

```
adj(A) = [ci j(A)]T
```

### 3.4 Eigenvalues and Eigenvectors of a Matrix

If A is an n×n matrix, a number λ is called an eigenvalue of A if:

```
Ax = λ x for some column x != 0 in Rn
```

In this case, x is called an eigenvector of A corresponding to the eigenvalue λ , or a λ -eigenvector
for short.

### 3.5 Characteristic Polynomial of a Matrix

If A is an n×n matrix, the characteristic polynomial cA(x) of A is defined by:

```
cA(x) = det(xI − A)
```

### 3.6 Diagonalizable Matrices

An n×n matrix A is called diagonalizable if:

P−1AP is diagonal for some invertible n×n matrix P

Here the invertible matrix P is called a diagonalizing matrix for A.

### Multiplicity of an Eigenvalue

An eigenvalue λ of a square matrix A is said to have multiplicity m if it occurs m times as a root of the characteristic polynomial cA(x).

### 3.8 Linear Dynamical System

If A is an n×n matrix, a sequence v0, v1, v2, ... of columns in Rn is called a linear dynamical system if v0 is specified and v1, v2, ... are given by the matrix recurrence vk+1 = Avk for each k ≥0. We call A the migration matrix of the system.

#### Lemma 3.6.1

Let A, B, and C be n×n matrices that are identical except that the pth row of A is the sum of the pth rows of B and C. Then:

```
det A = det B+ det C
```

#### Lemma 3.6.2

Let A = [ai j] denote an n×n matrix.

1. If B = [bi j] is formed from A by multiplying a row of A by a number u, then det B = u det A.
2. If A contains a row of zeros, then det A = 0.
3. If B = [bi j] is formed by interchanging two rows of A, then det B = −det A.
4. If A contains two identical rows, then det A = 0.
5. If B = [bi j] is formed by adding a multiple of one row of A to a different row, then
det B = det A.
