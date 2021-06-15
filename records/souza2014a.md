---
@InProceedings{souza2014a,
  author    = {Souza, R. and Chavez, C. and Bittencourt, R.A.},
  booktitle = {Proceedings of the brazilian symposium on software engineering (SBES). IEEE, Piscataway},
  title     = {Do rapid releases affect bug reopening? a case study of firefox},
  year      = {2014},
  pages     = {31–40},
  language  = {nl},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a release every six weeks.

# RQ2. What are the implications of adopting a rapid release cycle?

  1. The bug reopening rate increased 7% under the rapid release cycle.

  2. The number of bugs reopened due to failing automated tests did not change significantly in the rapid release cycle.

  3. The long-lived faulty bug fixes tended to be discovered earlier under the rapid release cycle.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Bug status
  - Proportion of bugs reopened
  - Time to fix bugs (days)
  - Time to reopen bugs (hours)

# RQ4. How do the studies mine release information?

The authors mined:
  
  - The Firefox Mercurial repository to extract the commit log
  - A SQL Database with the bug reports provided by a Mozilla engineering 

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests (Mann-Whitney nonparametric
test and Fisher’s exact test) to compare the metrics in traditional and rapid release cycles. 

They also contacted a Firefox engineer to explain the numbers according to their experience.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  -  Firefox releases 3.6, 4.0, and 5 through 27 (from 2009 to 2013)
  