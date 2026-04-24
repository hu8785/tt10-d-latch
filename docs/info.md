## How it works

This project implements a D latch, also called a transparent latch.

The inputs are:
- d = data input
- e = enable input

The output is:
- q

When e = 1, the latch is transparent, so q follows d.  
When e = 0, the latch holds its previous value.

This makes the D latch a level-sensitive sequential circuit.

## How to test

Change d and e and observe q.

Expected behavior:
- If e = 1, q follows d.
- If e = 0, q keeps its previous value even if d changes.

## External hardware

None

## Pinout

### Inputs
- ui[0] = d
- ui[1] = e

### Outputs
- uo[0] = q
