# Modules Notes

## If A and B are matrices of the same size, their sum A + B is the matrix formed by adding corresponding entries, i.e. for the entries aᵢⱼ and bᵢⱼ in A and B, the entry in the matrix A + B will be aᵢⱼ + bᵢⱼ.

## If A is any matrix and k is any number, the scalar multiple kA is the matrix obtained from A by multiplying each entry of A by k, i.e. k·aᵢⱼ for all entries.

## Let A, B, and C denote arbitrary m×n matrices where m and n are fixed. Let k and p denote arbitrary real numbers. Then

1. A+B = B+A 
2. A+(B+C) = (A+B)+C 
3. There is an m×n matrix 0, such that 0+A = A for each A 
4. For each A there is an m×n matrix, −A, such that A+(−A) = 0 
5. k(A+B) = kA+kB 
6. (k+ p)A = kA+ pA 
7. (kp)A = k(pA) 
8. 1A = A 

## If A is an m×n matrix, the transpose of A, written Aᵀ, is the n×m matrix whose rows are just the columns of A in the same order.

## Let A and B denote matrices of the same size, and let k denote a scalar.

1. If A is an m×n matrix, then Aᵀ is an n×m matrix.  
2. (Aᵀ)ᵀ = A  
3. (kA)ᵀ = kAᵀ  
4. (A + B)ᵀ = Aᵀ + Bᵀ

## Let ℝ denote the set of all real numbers. The set of all ordered n-tuples from ℝ is denoted by ℝn

## Let A be an m×n matrix, and let x ∈ ℝⁿ.

Write A in terms of its columns: A = [a₁ a₂ ⋯ aₙ]
Write x as an n-vector:
x = [x₁
     x₂
      ⋮
     xₙ]

Define A·x to be the m-vector in ℝᵐ: A·x = x₁a₁ + x₂a₂ + ⋯ + xₙaₙ

## Let A and B be m×n matrices, and let x, y ∈ ℝⁿ.

1. A(x + y) = Ax + Ay  
2. A(a·x) = a(Ax) = (aA)x for all scalars a  
3. (A + B)x = Ax + Bx

## If (a₁, a₂, ..., aₙ) and (b₁, b₂, ..., bₙ) are two ordered n-tuples in ℝⁿ, then their dot product is defined to be the number:

a₁b₁ + a₂b₂ + ⋯ + aₙbₙ

Obtained by multiplying corresponding entries and adding the results

## Suppose x₁ is any particular solution to the system Ax = b of linear equations. Then every solution x₂ to Ax = b has the form

x₂ = x₀ + x₁

for some solution x₀ of the associated homogeneous system Ax = 0.

## Let Ax = b be a system of equations with augmented matrix [A | b ].  Let rank A = r.

1. rank [A | b ] is either r or r + 1
2. The system is consistent if and only if rank [A | b ] = r 
3. The system is inconsistent if and only if rank rank [A | b ] = r + 1

## Let A be an m×n matrix and x an n-vector in ℝⁿ. Each entry of the vector Ax is the dot product of the corresponding row of A with x.

## Let A and B be m×n matrices. If Ax = Bx for all x ∈ ℝⁿ, then A = B.

## TA is the matrix transformation induced by A. TA: ℝⁿ → ℝᵐ defined by TA(x) = Ax for all x ∈ ℝⁿ.

## Let A be an m×n matrix, let B = [b₁ b₂ ⋯ bₖ] be an n×k matrix, where bⱼ is column j of B for each j.  

The product matrix AB is the m×k matrix defined as follows:

AB = A[b₁ b₂ ⋯ bₖ] = [Ab₁ Ab₂ ⋯ Abₖ]

## Let A be an m×n matrix and let B be an n×k matrix.

Then the product matrix AB is m×k and satisfies:  

A(Bx) = (AB)x for all x ∈ ℝᵏ

## Let A and B be matrices of sizes m×n and n×k, respectively. Then the (i, j)-entry of AB is the dot product of row i of A with column j of B.

## Assume that α is any scalar, and that A, B, and C are matrices of sizes such that the indicated matrix products are defined, and I is an identity matrix. Then:

1. IA = A  and  AI = A  
2. A(BC) = (AB)C  
3. A(B + C) = AB + AC  
4. (B + C)A = BA + CA  
5. α(AB) = (αA)B = A(αB)  
6. (AB)ᵀ = BᵀAᵀ

