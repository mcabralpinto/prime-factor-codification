# Prime Factor Codification

A converter and translator for the Prime Factor Writing System (or PFWS), a code I came up with for fun.

## How It Works

The essence of PFWS is that each alphanumerical character (digit or letter) is to be shown as its equivalent non-ambiguous representation based on its prime factors. As such, it operates under the following ruleset:

- **Numbers:** Determining the equivalent in PFWS involves following these steps:

    1. Decompose the number in prime factors;
    2. Count how many times every existing prime factor up until the highest appears in the decomposition;
    3. Sort the counts (highest factor -> lowest factor) and separate them with a single prime character `'`.
    4. For every group of *n* consecutive 0s, replace it with *n* in PFWS enclosed by brackets.

```
Turning 342 into PFWS:

1. 342 = 19 * 3 * 3 * 2
2. 19 appears one time. 17 appears zero times. 13 appears zero times. 11 appears zero times.
   7 appears zero times. 5 appears zero times. 3 appears two times. 2 appears one time.
3. 1 -> 0 -> 0 -> 0 -> 0 -> 0 -> 2 -> 1
4. 1'0'0'0'0'0'2'1 -> 1'(1'0'0)'2'1 -> 1'(1'(1))'2'1

342 in PFWS is 1'(1'(1))'2'1.
```
> **Note**: The single prime character separation is a way to avoid ambiguity. Without it, the number 10, coded in PFWS, could be interpreted as 3¹ * 2⁰ = 3 or 2¹⁰ = 1024!

- **Letters:** Determining the equivalent in PFWS involves following these steps:

    1. ;

  (To be continued)








