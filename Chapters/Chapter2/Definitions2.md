# Definitions

## Chapter 2

### 2.1 Matrix Addition

If A and B are matrices of the same size, their sum A+B is the matrix formed by adding corresponding entries

### 2.2  Matrix Scalar Multiplication

More generally, if A is any matrix and k is any number, the scalar multiple kA is the matrix obtained from A by multiplying each entry of A by k.

### 2.3 Transpose of a Matrix

If A is an m×n matrix, the transpose of A, written AT , is the n×m matrix whose rows are just the columns of A in the same order.

### 2.4 The set Rn of ordered n-tuples of real numbers

Let R denote the set of all real numbers. The set of all ordered n-tuples from R has a special notation:

Rn denotes the set of all ordered n-tuples of real numbers.

### 2.5  Matrix-Vector Multiplication

Let A = [ a1 a2 ··· an] be an m×n matrix, written in terms of its columns a1, a2, ..., an.

```
If x =  [   x1  ]
        [   x2  ]
        [   ... ]
        [   xn  ]
```

is any n-vector, the product Ax is defined to be the m-vector given by:

```
Ax = x1a1 +x2a2 +···+xnan
```

### 2.6 Dot Product in Rn

If (a1, a2, ..., an) and (b1, b2, ..., bn) are two ordered n-tuples, their dot product is defined to be the number a1b1 +a2b2 +···+anbn
obtained by multiplying corresponding entries and adding the results.

### 2.7 The Identity Matrix

For each n > 2, the identity matrix In is the n×n matrix with 1s on the main diagonal (upper left to lower right), and zeros elsewhere.

### 2.8  Matrix Transformation TA

TA is called the matrix transformation induced by A.

### 2.9 Matrix Multiplication

Let A be an m×n matrix, let B be an n×k matrix, and write
B = [ b1 b2 ··· bk ] where bj is column j of B for each j.

The product matrix AB is the m×k matrix defined as follows:

```
AB = A[ b1 b2 ··· bk ]= [ Ab1 Ab2 ··· Abk ].
```

### 2.10 Block Partition of a Matrix

It is often useful to consider matrices whose entries are themselves matrices (called blocks). A matrix viewed in this way is said to be partitioned into blocks.

### 2.11 Matrix Inverses

If A is a square matrix, a matrix B is called an inverse of A if and only if AB = I and BA = I. A matrix A that has an inverse is called an invertible matrix.

#### Corollary 2.4.1

A square matrix A is invertible if and only if AT is invertible.

#### Corollary 2.4.2

An n×n matrix A is invertible if and only if rank A = n.

### 2.12 Elementary Matrices

An n×n matrix E is called an elementary matrix if it can be obtained from the identity matrix In by a single elementary row operation (called the operation corresponding to E). We say that E is of type I, II, or III if the operation is of that type (see Definition 1.2).

#### Lemma 2.5.1

If an elementary row operation is performed on an m×n matrix A, the result is EA where E is the elementary matrix obtained by performing the same operation on the m×m identity matrix.

#### Lemma 2.5.2

Every elementary matrix E is invertible, and E−1 is also a elementary matrix (of the same type). Moreover, E−1 corresponds to the inverse of the row operation that produces E.

Type Operation Inverse Operation

```
Type    Operation

I.      Interchange rows p and q

II.     Multiply row p by k != 0

III.    Add k times row p to row q != p

        Inverse

I.      Interchange rows p and q

II.     Multiply row p by 1/k, k != 0

III.    Subtract k times row p from   row q, q != p
```

### Linear Transformation Rn → Rm

A transformation T : Rn → Rm is called a linear transformation if it satisfies the following two conditions for all vectors x and y in Rn and all scalars a:

```
T1 T(x+y) = T(x)+T(y)

T2 T(ax) = aT(x)
```

#### Lemma 2.7.1

Let A and B denote matrices.

1. If A and B are both lower (upper) triangular, the same is true of AB.
2. If A is n×n and lower (upper) triangular, then A is invertible if and only if every main diagonal entry is nonzero. In this case A−1 is also lower (upper) triangular.

### 2.14 LU-factorization

A factorization A = LU as in Theorem 2.7.1 is called an  LU-factorization of A.

#### Corollary 2.8.1

Let E ≥0 be a square matrix. In each case, I −E is invertible and
(I −E)−1 ≥0:

1. All row sums of E are less than 1.
2. All column sums of E are less than 1.
