# End to End with RFCI Fault Localization

## Executing examples in this repo

1. Clone the repo
2. In MoreBuggyFcns.py, scroll to the bottom of the file where test_function is called. Replace the first and second arguments with the good and bad program of your choice from the above examples, respectively.
3. Replace the third argument with the number of program executions you would like to run.
4. If inclined, add arguments `arg_min` and `arg_max` to create new bounds for the input values to the good and bad functions being tested.
5. Run `python fault_localizer.py` in your command line.

## Adding a new example program to this repo

1. Convert example program to SSA form and obtain causal map.
2. Rename SSA form of the program to `bad_{original program name}` and name the causal map bad\_{original program name}\_causal_map.
3. Insert bug (that occurs with probability greater than zero and less than one) into the SSA form of the program at some assignment.
4. Before every return statement in the SSA form of the program, make a call to `record_locals(locals(), bad_{original program name}_causal_map)`.
5. To execute a test of the program, follow the steps outlined in "Executing examples in this repo"

## More precise steps for testing a general numerical program

1. Find some "correct" program <i>P</i>.
2. Rewrite program <i>P</i> with a bug in <i>x<sub>i</sub></i>, the <i>i<sup>th</sup></i> assignment of a variable <i>x</i> in <i>P</i>. We will call this buggy version <i>P'</i>.
3. Pass <i>P'</i> into the SSA form converter to receive SSA form of P', which will be called <i>P'<sub>SSA</sub></i>.
4. Create a set <i>T</i> of test inputs for <i>P'<sub>SSA</sub></i>.
5. For every test input t in T, execute both <i>P</i> and <i>P'</i> and compare the results, record 1 if the output of <i>P'</i> differed from <i>P</i>.
