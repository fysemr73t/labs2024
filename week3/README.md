Programs used in the discussion portion of Week 3.

` uc_0.py`: A demonstration of a Universal Constructor. You set the
variable `MAX_GEN` to some small integer. Set it to 1 if you just want
to run the program without generating any children. Children are named
with increasing integers in the filename. There are no loops and so
the program produces only one child.

`ucpoly_0.py`: Adds a polymorphic engine to `uc_0.py` so that you
cannot use a hash (e.g., `openssl md5 uc_0.py`) to recognize this
self-replicating program.

`calc.py`: A simple calculator that evaluates Python expressions, but
it doesn't check its input (beyond looking for no input and the quit
command). Running the following inputs will cause `calc` to turn into
the Universal Constructor:

-   exec('import uc_0')
-   exec('sys.argv[0] = "uc_0.py"')
-   exec('import uc_0')

**OLD**

`uc.0.py`: An old version of `uc_0.py` before I wrote `calc.py`.