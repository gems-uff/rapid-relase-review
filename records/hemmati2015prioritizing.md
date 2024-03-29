---
@InProceedings{hemmati2015prioritizing,
  author       = {Hemmati, Hadi and Fang, Zhihan and Mantyla, Mika V},
  booktitle    = {2015 IEEE 8th International Conference on Software Testing, Verification and Validation (ICST)},
  title        = {Prioritizing manual test cases in traditional and rapid release environments},
  year         = {2015},
  organization = {IEEE},
  pages        = {1--10}
 }
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a release every six weeks.

# RQ2. What are the implications of adopting a rapid release cycle?

The best approaches to prioritize tests are different in traditional and rapid release cycles. In the rapid release cycle, the risk-driven approaches are far more effective than the other evaluated approaches. In the traditional release cycle, the risk-driven approaches perform better in some releases. However, in other releases, the topic coverage and the text diversity approaches perform better.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?
  
  - The effectiveness of each test approaches to prioritize tests.

# RQ4. How do the studies mine release information?

The authors mined the Mozilla Litmus system, which contains the test cases and execution results from the complete functional test suites.

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Mann-Whitney U test and Vargha-Delaney A - effect size) to compare the metrics in traditional and rapid release cycles. 

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - 4 firefox traditional releases: 3.0, 3.5, 3.6, and 4.0.
  - 9 firefox rapid releases: 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, and 13,
  - 1,547 unique test cases for a total of 312,502 tests
  