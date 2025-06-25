# Gaussian Algorithm

Step 1. If the matrix consists entirely of zeros, stop—it is already in row-echelon form.

Step 2. Otherwise, find the first column from the left containing a nonzero entry (call it a),
and move the row containing that entry to the top position.

Step 3. Now multiply the new top row by 1/a to create a leading 1.

Step 4. By subtracting multiples of that row from rows below it, make each entry below the
leading 1 zero.

This completes the first row, and all further row operations are carried out on the remaining rows.

Step 5. Repeat steps 1–4 on the matrix consisting of the remaining rows.

The process stops when either no rows remain at step 5 or the remaining rows consist entirely of zeros.