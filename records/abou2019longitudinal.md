---
@InProceedings{abou2019longitudinal,
  author       = {Abou Khalil, Zeinab and Constantinou, Eleni and Mens, Tom and Duchien, Laurence and Quinton, Cl{\'e}ment},
  booktitle    = {2019 IEEE International Conference on Software Maintenance and Evolution (ICSME)},
  title        = {A longitudinal analysis of bug handling across Eclipse releases},
  year         = {2019},
  organization = {IEEE},
  pages        = {1--12},
  groups       = {forward_1, daCosta2016impact, daCosta2018impact, selected, Other Studies},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Eclipse rapid release cycle, which comprises a release every quarterly (13-week).

# RQ2. What are the implications of adopting a rapid release cycle?

 1. The bug triaging time is similar on rapid and traditional release cycles.

 2. The bug fixing rate has improved on the rapid release cycle.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

 - Bug triaging time;
 - Byg fixing time;
 - Bug resolution rate; and
 - Bug fixing rate.

# RQ4. How do the studies mine release information?

The authors mined bug reports extracted from Bugzilla for each Eclipse release. They used Disco to mine the bug reports, which is a tool that helps in the mining process but not specific for releases.

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Wilcoxon rank-sum test and  Cliff’s delta) to compare the metrics in traditional and rapid release cycles. 

# RQ6. What corpus do the studies use to compare rapid and traditional releases?
 
 - 18 Eclipse major releases over a 15-year, comprising 16 annual and two quarterly releases, starting with release 3.0 (the first release shipped by the independent Eclipse Foundation).
 - 138,445 bug reports
