---
@Article{mantyla2015rapid,
  author    = {M{\"a}ntyl{\"a}, Mika V and Adams, Bram and Khomh, Foutse and Engstr{\"o}m, Emelie and Petersen, Kai},
  journal   = {Empirical Software Engineering},
  title     = {On rapid releases and software testing: a case study and a semi-systematic literature review},
  year      = {2015},
  number    = {5},
  pages     = {1384--1425},
  volume    = {20},
  groups    = {selected, start_set},
  publisher = {Springer},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a release every six weeks.

# RQ2. What are the implications of adopting a rapid release cycle?

  1. Rapid releases cycle performs more test executions per day, but these tests focus on a smaller subset of the test case corpus.

  2. Rapid release cycle use less testers, but that they have a higher workload.

  3. Rapid release cycle, test fewer builds than in traditional release cycle and in rapid release cycle the focus is on the larger builds.

  4. In rapid releae cycle, developers test fewer platforms, but the test ina supported platform are more complete.

  5. In Rapid release cycle, the tests have higher similarity than in traditional release cycles.

  6. In Rapid release cycle, the tests happens closer to the release date.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Number of tests executed per day;
  - Number of unique tests cases executed per day;
  - Number of testers per day;
  - Number of tested builds per day;
  - Number of tested locales per day; 
  - Number of operating systems tested per day;
  - Similarity of test suites and teams; and
  - Temporal distance between a test case execution and the release date.

# RQ4. How do the studies mine release information?

The authors mined:
  - The Firefox Litmus system to get the test cases and the execution data of the test cases; and
  - The Firefox Mercurial repository to extract the code revision history.

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Shapiro-Wilk test, Wilcoxon rank-sum test, and Cliff’s delta) to compare the metrics in traditional and rapid release cycles. They normalized some metrics for the project duration and used Cohen’s Kappa for correlation.

They also interviewed a Mozilla quality assurance engineering to validate their finding and help them understand why the fiding happened.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

 - Firefox releases from 2.0 to 13.0. (06/2006–06/2012), which includes five major TR versions (2.0, 3.0, 3.5, 3.6, and 4.0) with 147 smaller releases (20 alphas, 29 betas, 12 release candidates, and 86 minor), and nine RR versions (5.0 until 13.0) with 89 smaller releases (17 alphas, 56 betas, and 16 minor).
