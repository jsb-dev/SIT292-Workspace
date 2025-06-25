# Definitions

## Chapter 4

### 4.1 Geometric Vectors

Suppose that A and B are any two points in R3. In Figure 4.1.4 the line segment from A to B is
denoted −→ AB and is called the geometric vector from A to B. Point A is called the tail of −→ AB, B is
called the tip of −→ AB, and the length of −→ AB is denoted:

```
  −→
 ‖AB‖
```

#### The Parallelogram Law

In the parallelogram determined by two vectors v and w, the vector v+w is the diagonal with the same tail as v and w.

#### Scalar Multiple Law

If a is a real number and v != 0 is a vector then:

1. The length of av is ‖av‖= |a|‖v‖.
2. If av != 0, the direction of av is:

```
av  {
        { the same as v if a > 0 }
        { opposite to v if a < 0 }
    }
```

### 4.2 Parallel Vectors in R3

Two nonzero vectors are called parallel if they have the same or opposite direction.

### 4.3 Direction Vector of a Line

With this in mind, we call a nonzero vector d != 0 a direction vector for the line if it is parallel to

```
 −→
 AB
```

for some pair of distinct points A and B on the line.

#### Vector Equation of a Line

The line parallel to d != 0 through the point with vector p0 is given by:

p = p0 +td where t is any scalar

In other words, the point P with vector p is on this line if and only if a real number t exists such that:

p = p0 +td

### Parametric Equations of a Line

The line through P0(x0, y0, z0) with direction vector

```
d = [ a ]
    [ b ]
    [ c ]

d != 0
```

is given by:

```
x = x0 +ta
y = y0 +tb (t is any scalar)
z = z0 +tc
```

### 4.4 Dot Product in R3

Given vectors:

```
v = [ x1 ]
    [ y1 ]
    [ z1 ]
```

and

``` 
w = [ x2 ]
    [ y2 ]
    [ z2 ]
```

their dot product v·w is a number defined

```
v·w = x1x2 +y1y2 +z1z2 = vT w
```

#### Law of Cosines

If a triangle has sides a, b, and c, and if θ is the interior angle opposite c then:

```
c2 = a2 +b2 −2abcosθ
```

### 4.5 Orthogonal Vectors in R3

Two vectors v and w are said to be orthogonal if v = 0 or w = 0 or the angle between them is π/2.

### 4.6 Projection in R3

The vector 

```
u1 = −→
     QP1 
``` 

in Figure 4.2.5 is called the projection of u on d. It is denoted u1 = projd u.

### 4.7 Normal Vector in a Plane

A nonzero vector n is called a normal for a plane if it is orthogonal to every vector in the plane.

#### Scalar Equation of a Plane

The plane through P0(x0, y0, z0) with normal

```
n = [ a ]
    [ b ]
    [ c ]

n != 0 
```

as a normal vector is given by

```
a(x−x0)+b(y−y0)+c(z−z0) = 0
```

In other words, a point P(x, y, z) is on this plane if and only if x, y, and z satisfy this equation.

### Vector Equation of a Plane

The plane with normal n != 0 through the point with vector p0 is given by

```
n·(p−p0) = 0
```

In other words, the point with vector p is on the plane if and only if p satisfies this condition.

### 4.8 Cross Product

Given vectors 

```
v1 = [ x1 ]
     [ y1 ]
     [ z1 ]
```

and

```
v2 = [ x2 ]
     [ y2 ]
     [ z2 ]
```

define the cross product v1 × v2 by

```
v1 × v2 = [     y1z2 −z1y2  ]
          [   −(x1z2 −z1x2) ]
          [     x1y2 −y1x2  ]
```

#### Determinant Form of the Cross Product

Consider the following, if:

```
v1 = [ x1 ]
     [ y1 ]
     [ z1 ]
```

and

```
v2 = [ x2 ]
     [ y2 ]
     [ z2 ]
```

are two vectors, then:

```
v1 × v2 = det [ i x1 x2 ]
              [ j y1 y2 ]
              [ k z1 z2 ]

                    = ∣ y1 y2 |
                      ∣ z1 z2 | i

                      -

                      | x1 x2 |
                      | z1 z2 | j

                      +

                      | x1 x2 |
                      | y1 y2 | k
```

where the determinant is expanded along the first column.

#### Right-hand Rule

If the vector u×v is grasped in the right hand and the fingers curl around from u to v through the angle θ, the thumb points in the direction for u × v.

### 4.9 Linear Operator on R3

A linear transformation

```
T : Rn → Rn
```

is called a linear operator on Rn.