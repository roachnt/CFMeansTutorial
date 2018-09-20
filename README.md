# End to End with RFCI Fault Localization

1. Find some "correct" program <i>P</i>.
2. Rewrite program <i>P</i> with a bug in <i>x<sub>i</sub></i>, the <i>i<sup>th</sup></i> assignment of a variable <i>x</i> in <i>P</i>. We will call this buggy version <i>P'</i>.
3. Pass <i>P'</i> into the SSA form converter to receive SSA form of P', which will be called <i>P'<sub>SSA</sub></i>.
4. Create a set <i>T</i> of test inputs for <i>P'<sub>SSA</sub></i>.
5.
