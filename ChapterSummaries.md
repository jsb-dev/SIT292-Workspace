# Chapter Summaries

## Chapter 1: Systems of LinearEquations

A standard treatment of gaussian elimination is given. The rank of a matrix is introduced via the row-
echelon form, and solutions to a homogeneous system are presented as linear combinations of basic solu-
tions. Applications to network flows, electrical networks, and chemical reactions are provided.

## Chapter 2: Matrix Algebra

After a traditional look at matrix addition, scalar multiplication, and transposition in Section 2.1, matrix-
vector multiplication is introduced in Section 2.2 by viewing the left side of a system of linear equations
as the product Ax of the coefficient matrix A with the column x of variables. The usual dot-product
definition of a matrix-vector multiplication follows. Section 2.2 ends by viewing an m ×n matrix A as a
transformation Rn →Rm. This is illustrated for R2 →R2 by describing reflection in the x axis, rotation of
R2 through π2 , shears, and so on. In Section 2.3, the product of matrices A and B is defined by:

### AB = [ Ab1 Ab2 ··· Abn]

where the bi are the columns of B. A routine computation shows that this is the matrix of the transformation B
followed by A. This observation is used frequently throughout the book, and leads to simple, conceptual
proofs of the basic axioms of matrix algebra. Note that linearity is not required—all that is needed is some
basic properties of matrix-vector multiplication developed in Section 2.2. Thus the usual arcane definition
of matrix multiplication is split into two well motivated parts, each an important aspect of matrix algebra.
Of course, this has the pedagogical advantage that the conceptual power of geometry can be invoked to
illuminate and clarify algebraic techniques and definitions.
In Section 2.4 and 2.5 matrix inverses are characterized, their geometrical meaning is explored, and
block multiplication is introduced, emphasizing those cases needed later in the book. Elementary ma-
trices are discussed, and the Smith normal form is derived. Then in Section 2.6, linear transformations
Rn →Rm are defined and shown to be matrix transformations. The matrices of reflections, rotations, and
projections in the plane are determined. Finally, matrix multiplication is related to directed graphs, matrix
LU-factorization is introduced, and applications to economic models and Markov chains are presented.

## Chapter 3: Determinants and Diagonalization

The cofactor expansion is stated (proved by induction later) and used to define determinants inductively
and to deduce the basic rules. The product and adjugate theorems are proved. Then the diagonalization
algorithm is presented (motivated by an example about the possible extinction of a species of birds). As
requested by our Engineering Faculty, this is done earlier than in most texts because it requires only deter-
minants and matrix inverses, avoiding any need for subspaces, independence and dimension. Eigenvectors
of a 2×2 matrix A are described geometrically (using the A-invariance of lines through the origin). Di-
agonalization is then used to study discrete linear dynamical systems and to discuss applications to linear
recurrences and systems of differential equations. A brief discussion of Google PageRank is included.

## Chapter 4: Vector Geometry

Vectors are presented intrinsically in terms of length and direction, and are related to matrices via coordi-
nates. Then vector operations are defined using matrices and shown to be the same as the corresponding
intrinsic definitions. Next, dot products and projections are introduced to solve problems about lines and
planes. This leads to the cross product. Then matrix transformations are introduced in R3, matrices of pro-
jections and reflections are derived, and areas and volumes are computed using determinants. The chapter
closes with an application to computer graphics.

## Chapter 5: The Vector Space Rn

Subspaces, spanning, independence, and dimensions are introduced in the context of Rn in the first two
sections. Orthogonal bases are introduced and used to derive the expansion theorem. The basic properties
of rank are presented and used to justify the definition given in Section 1.2. Then, after a rigorous study of
diagonalization, best approximation and least squares are discussed. The chapter closes with an application
to correlation and variance.
This is a “bridging” chapter, easing the transition to abstract spaces. Concern about duplication with
Chapter 6 is mitigated by the fact that this is the most difficult part of the course and many students
welcome a repeat discussion of concepts like independence and spanning, albeit in the abstract setting.
In a different direction, Chapter 1–5 could serve as a solid introduction to linear algebra for students not
requiring abstract theory.

## Chapter 6: Vector Spaces

Building on the work on Rn in Chapter 5, the basic theory of abstract finite dimensional vector spaces is
developed emphasizing new examples like matrices, polynomials and functions. This is the first acquain-
tance most students have had with an abstract system, so not having to deal with spanning, independence
and dimension in the general context eases the transition to abstract thinking. Applications to polynomials
and to differential equations are included.

## Chapter 7: Linear Transformations

General linear transformations are introduced, motivated by many examples from geometry, matrix theory,
and calculus. Then kernels and images are defined, the dimension theorem is proved, and isomorphisms
are discussed. The chapter ends with an application to linear recurrences. A proof is included that the
order of a differential equation (with constant coefficients) equals the dimension of the space of solutions.

## Chapter 8: Orthogonality

The study of orthogonality in Rn, begun in Chapter 5, is continued. Orthogonal complements and pro-
jections are defined and used to study orthogonal diagonalization. This leads to the principal axes theo-
rem, the Cholesky factorization of a positive definite matrix, QR-factorization, and to a discussion of the
singular value decomposition, the polar form, and the pseudoinverse. The theory is extended to Cn in
Section 8.7 where hermitian and unitary matrices are discussed, culminating in Schur’s theorem and the
spectral theorem. A short proof of the Cayley-Hamilton theorem is also presented. In Section 8.8 the field
Zp of integers modulo p is constructed informally for any prime p, and codes are discussed over any finite
field. The chapter concludes with applications to quadratic forms, constrained optimization, and statistical
principal component analysis.

## Chapter 9: Change of Basis

The matrix of general linear transformation is defined and studied. In the case of an operator, the rela-
tionship between basis changes and similarity is revealed. This is illustrated by computing the matrix of a
rotation about a line through the origin in R3. Finally, invariant subspaces and direct sums are introduced,
related to similarity, and (as an example) used to show that every involution is similar to a diagonal matrix
with diagonal entries ±1.

## Chapter 10: Inner Product Spaces

General inner products are introduced and distance, norms, and the Cauchy-Schwarz inequality are dis-
cussed. The Gram-Schmidt algorithm is presented, projections are defined and the approximation theorem
is proved (with an application to Fourier approximation). Finally, isometries are characterized, and dis-
tance preserving operators are shown to be composites of a translations and isometries.

## Chapter 11: Canonical Forms

The work in Chapter 9 is continued. Invariant subspaces and direct sums are used to derive the block
triangular form. That, in turn, is used to give a compact proof of the Jordan canonical form. Of course the
level is higher
