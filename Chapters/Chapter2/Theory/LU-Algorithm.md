# LU-Algorithm

Let A be an m×n matrix of rank r, and suppose that A can be lower reduced to a row-echelon matrix U. Then A = LU where the lower triangular, invertible matrix L is constructed as follows:

1. If A = 0, take L = Im and U = 0.
2. If A 6= 0, write A1 = A and let c1 be the leading column of A1. Use c1 to create the first leading 1 and create zeros below it (using lower reduction). When this is completed, let A2 denote the matrix consisting of rows 2 to m of the matrix just created.
3. If A2 6= 0, let c2 be the leading column of A2 and repeat Step 2 on A2 to create A3.
4. Continue in this way until U is reached, where all rows below the last leading 1 consist of
zeros. This will happen after r steps.
5. Create L by placing c1, c2, ..., cr at the bottom of the first r columns of Im.
