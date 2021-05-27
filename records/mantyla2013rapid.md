---
@InProceedings{mantyla2013rapid,
  author       = {M{\"a}ntyl{\"a}, Mika V and Khomh, Foutse and Adams, Bram and Engstr{\"o}m, Emelie and Petersen, Kai},
  booktitle    = {2013 IEEE International Conference on Software Maintenance},
  title        = {On rapid releases and software testing},
  year         = {2013},
  organization = {IEEE},
  pages        = {20--29},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a release every six weeks.

# RQ2. What are the implications of adopting a rapid release cycle?

  1. The rapid release cycle performs almost twice as many tests per day compared to the traditional release cycle, but these tests focus on a smaller subset of the test case corpus instead of on the entire corpus.

  2. In the rapid release cycle, fewer contributors conduct testing. However, to keep up with the rapid releases, the number of testers has increased.
  
  3. Less rapid release cycle builds are being tested per day, but the rapid release cycle builds contain more commits per day than in traditional release cycles.

  4. Rapid release cycles perform the tests in fewer platforms but test each supported platform more thoroughly.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Number of tests executed per day;
  - Number of unique tests cases executed per day;
  - Number of testers per day;
  - Number of tested builds per day;
  - Number of commits to the repository per day;
  - Number of tested locales per day; and
  - Number of operating systems tested per day.

# RQ4. How do the studies mine release information?

The authors mined:
  - The Firefox Litmus system to get the test cases and the execution data of the test cases; and
  - The Firefox Mercurial repository to extract the code revision history.

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Shapiro-Wilk test, Wilcoxon rank-sum test, and Cliff’s delta) to compare the metrics in traditional and rapid release cycles. They normalized all metrics for the project duration.

They also interviewed a Mozilla quality assurance engineering to validate their finding and help them understand why the fiding happened.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Firefox releases from 2.0 to 13.0. The Firefox project made 249 releases, of which 213 releases (142 TR and 71 RR) reported their testing activity into the Litmus system.

  - 1,547 unique test cases (roughly 10% of them are automated) for a total of 312,502 test case executions across six years of testing (06/2006–06/2012), performed by 6,058 individuals on 2,009 software builds, 22 operating system versions and 78 locales.
