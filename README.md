# Prime Factor Codification

A converter and translator for the Prime Factor Writing System (or PFWS), a code I came up with for fun.

## How it works

The essence of PFWS is that each alphanumerical character (digit or letter) is to be shown as its equivalent non-ambiguous representation based on its prime factors. As such, it operates under the following ruleset:

- **Numbers:** Determining a number's equivalent in PFWS involves following these steps:
    1. Decompose the number in prime factors;
    1. Count how many times every prime factor up until the highest appears in the decomposition;
    1. Sort the counts (highest factor -> lowest factor) and separate them with a single prime character `'`.

    - Example:
    ```
    Turning 126 into PFWS:

    1. 126 = 7 * 3 * 3 * 2
    2. 7 appears one time. 5 appears zero times. 3 appears two times. 2 appears one time.
    3. 1 -> 0 -> 2 -> 1

    126 in PFWS is 1'0'2'1
    ```