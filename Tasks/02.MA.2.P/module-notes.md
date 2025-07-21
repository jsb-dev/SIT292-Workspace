# Modules Notes

## If A and B are matrices of the same size, their sum A + B is the matrix formed by adding corresponding entries, i.e. for the entries aᵢⱼ and bᵢⱼ in A and B, the entry in the matrix A + B will be aᵢⱼ + bᵢⱼ.

Matrix addition is only compatible with matrices of matching dimmensions. They can be added together entry-wise, so each corresponding entry is added together.



## If A is any matrix and k is any number, the scalar multiple kA is the matrix obtained from A by multiplying each entry of A by k, i.e. k·aᵢⱼ for all entries.

Scalar multiplication is more or less how it sounds, scale the entire matrix linearly by scalar k. For this, multiply each entry in the matrix by the scalar.



## Let A, B, and C denote arbitrary m×n matrices where m and n are fixed. Let k and p denote arbitrary real numbers. Then

1. A+B = B+A 
2. A+(B+C) = (A+B)+C 
3. There is an m×n matrix 0, such that 0+A = A for each A 
4. For each A there is an m×n matrix, −A, such that A+(−A) = 0 
5. k(A+B) = kA+kB 
6. (k+ p)A = kA+ pA 
7. (kp)A = k(pA) 
8. 1A = A 

These are the rules governing valid matrix arithmetic.

1) Commutativity with addition: The order of matrices added doesn't alter the outcome.
2) Associativity with addition: Any grouping of matrices for addition won't alter the result
3) Addititve 0 matrix: 0, representing a matrix of all 0s, can be added to another wmatrix ith the same dimensions, leaving it unchanged
4) Additive inverse: There's an inverse of matrix A, denoted -A, which negates the matrix A when added to it
5) Distribution with matrix addition: Scalar multiplication of a sum of matrices A and B is the same as scaling A and B individually before adding
6) Distribution with scalar addition: A scalar sum of p + k multiplied by a matrix A is the same as scaling matrix A by p and k individually, and adding those together
7) Associativity with scalar multiplication: Multiplying a matrix A by a scalar product of pk, scaling the matrix by the product is the same as applying scalar multiplication with p to a matrix scaled by k
8) Scale by 1: Scaling a matrix by 1 leaves the matrix unchanged 



## If A is an m×n matrix, the transpose of A, written Aᵀ, is the n×m matrix whose rows are just the columns of A in the same order

The transpose of a matrix is the original matrix that's had its row and col dimensions swapped. Each row is made a column and vice versa. Transposing a transposed matrix returns the original matrix.



## Let A and B denote matrices of the same size, and let k denote a scalar.

1. If A is an m×n matrix, then Aᵀ is an n×m matrix.  
2. (Aᵀ)ᵀ = A  
3. (kA)ᵀ = kAᵀ  
4. (A + B)ᵀ = Aᵀ + Bᵀ

1) Described above, matrix transposition swaps row and col dimensions
2) The transpose of a transposed matrix is the same as the original matrix
3) If you scale a matrix A by k, and then transpose the result, this is the same as scaling the transposed matrix by k



## Let ℝ denote the set of all real numbers. The set of all ordered n-tuples from ℝ is denoted by ℝn

Where ordered n-tuples are sets of n elements ordered specifically, Rn denotes all ordered n-tuples in the space of real numbers. Rn denotes the whole set of all possible ordered n-tuples with each element existing in the space of real numbers.



## Let A be an m×n matrix, and let x ∈ ℝⁿ.

Write A in terms of its columns: A = [a₁ a₂ ⋯ aₙ]
Write x as an n-vector:
x = [x₁
     x₂
      ⋮
     xₙ]

Define A·x to be the m-vector in ℝᵐ: A·x = x₁a₁ + x₂a₂ + ⋯ + xₙaₙ

The process for multiplying a row vector A by column vector x, where the dot product is calculated by multiplying corresponding entries in each and adding them together.



## Let A and B be m×n matrices, and let x, y ∈ ℝⁿ.

1. A(x + y) = Ax + Ay  
2. A(a·x) = a(Ax) = (aA)x for all scalars a  
3. (A + B)x = Ax + Bx

1) Distribution with matrix and vector addition: Scaling a matrix A by the addition of two vectors x and y is the same as scaling A by each vector individually before adding them together.
2) Scalar multiplication with vector/matrix mult: 

- Multiplying matrix A by the product of a scalar a and vector x
- Multiplying matrix A by vector x and scaling the result by scalar a

Both would be the same as scaling A by scalar a, and then multiplying the result by vector x.



## If (a₁, a₂, ..., aₙ) and (b₁, b₂, ..., bₙ) are two ordered n-tuples in ℝⁿ, then their dot product is defined to be the number:

a₁b₁ + a₂b₂ + ⋯ + aₙbₙ

Obtained by multiplying corresponding entries and adding the results

Where two ordered 1D sets exist with the same length, the dot product is obtained by multiplying each corresponding entry in each set, and adding all the resulting products together.



## Suppose x₁ is any particular solution to the system Ax = b of linear equations. Then every solution x₂ to Ax = b has the form

x₂ = x₀ + x₁

for some solution x₀ of the associated homogeneous system Ax = 0.

For a particular solution x1, a vector which satisfies Ax = b for a system, and a solution of the corresponding homogeneous system x0, every solution x2 to the original system can be expressed as the sum of x0 and x1



## Let Ax = b be a system of equations with augmented matrix [A | b ].  Let rank A = r.

1. rank [A | b ] is either r or r + 1
2. The system is consistent if and only if rank [A | b ] = r 
3. The system is inconsistent if and only if rank rank [A | b ] = r + 1

1) The rank of an augmented matrix [A | b] will either be the same as the rank of matrix A, or 1 greater
2) If the rank is the same, the system is consistent and has a solution
3) If the rank is one greater, then a row of the RREF matrix will present a contradiction, inconsistent



## Let A be an m×n matrix and x an n-vector in ℝⁿ. Each entry of the vector Ax is the dot product of the corresponding row of A with x.

Multiplying matrix A by n-vector x will result in an n-vector where each entry is achieved by multiplying each element from the corresponding row in A, with their corresponding column value in x, and adding the products together.



## Let A and B be m×n matrices. If Ax = Bx for all x ∈ ℝⁿ, then A = B.

If mult-compatible matrices A and B have the property that Ax = Bx for any vector x in the set of real numbers, then the matrices A and B must be the same



## TA is the matrix transformation induced by A. TA: ℝⁿ → ℝᵐ defined by TA(x) = Ax for all x ∈ ℝⁿ.

Matrices can be applied to vectors to transform them. Take a vector in n-dimensional space (1 column of rows). Applying the transformation induced by A reshapes the vector into m-dimensional space (1 row of columns). Where Ax is the notation for matrix A multiplied by vector x, TA(x) denotes the linear transformation A applies to x.



## Let A be an m×n matrix, let B = [b₁ b₂ ⋯ bₖ] be an n×k matrix, where bⱼ is column j of B for each j.  

The product matrix AB is the m × k matrix defined as follows:

AB = A[b₁ b₂ ⋯ bₖ] = [Ab₁ Ab₂ ⋯ Abₖ]

Regarding matrix multiplication, the dot product of a row from A with corresponding column from B will be the result for each entry.



## Let A be an m×n matrix and let B be an n×k matrix.

Then the product matrix AB is m × k and satisfies:  

A(Bx) = (AB)x for all x ∈ ℝᵏ

This highlights the structure of the resulting matrix where an m*n matrix is multiplied by an n*k matrix. The resulting matrix will be m*k dimensions. This matrix always satisfies A(Bx) = (AB)x for all real x.



## Let A and B be matrices of sizes m×n and n×k, respectively. Then the (i, j)-entry of AB is the dot product of row i of A with column j of B.


Each entry of row i column j in AB is achieved by adding all corresponding products of row i in A with column j in B. 

## Assume that α is any scalar, and that A, B, and C are matrices of sizes such that the indicated matrix products are defined, and I is an identity matrix. Then:

1. IA = A  and  AI = A  
2. A(BC) = (AB)C  
3. A(B + C) = AB + AC  
4. (B + C)A = BA + CA  
5. α(AB) = (αA)B = A(αB)  
6. (AB)ᵀ = BᵀAᵀ

1) Multiplying a matrix A by its identity I results in A unchanged, regardless of multiplication order
2) Multiplying any 3 matrices together with grouping, the order in which matrices are grouped together doesn't alter the outcome
3) Multiplying matrix A by the sum of matrices B and C yields the same result as scaling B and C by A individually, then adding together
4) Taking the sum of matrices B and C, then multiplying the result by matrix A, is the same as the sum of B and C scaling A individually
5) Scaling a matrix product AB by scalar a can be expressed as either scaling A by a, and multiplying by B, or scaling B by a, and multiplying A by the result
6) The transpose of the resulting product matrix from A * B is the same as multiplying the transposes of B * A