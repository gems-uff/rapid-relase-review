---
@InProceedings{khomh2012a,
  author          = {Khomh, Foutse and Dhaliwal, Tejinder and Zou, Ying and Adams, Bram},
  booktitle       = {Mining Software Repositories, 2012 9th Working Conference},
  title           = {Do Faster Releases Improve Software Quality? An Empirical Case Study of Mozilla Firefox},
  year            = {2012},
  address         = {Kingston, Ontario, Canada},
  month           = jun,
  citation-number = {33},
  groups          = {backward_1, daCosta2016impact, daCosta2018impact, mantyla2013rapid, clark2014moving, hemmati2015prioritizing, hemmati2017prioritizing, souza2015rapid, khomh2015understanding, mantyla2015rapid, selected, Firefox},
  language        = {en},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a release every six weeks.
# RQ2. What are the implications of adopting a rapid release cycle?

  1. There is no significant difference between the number of post-release bugs and median daily crashes of rapid release and traditional release. 

  2. The median uptime is significantly lower in the rapid release cycle.

  3. The proportion of bugs fixed is lower in the rapid release cycle than in the traditional release cycle. However, the bugs are fixed significantly faster under a rapid release cycle. 

  4. Users switch faster to newer releases on a rapid release cycle.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Number of bugs reported after the release date;
  – Median of the number of crashes per day;
  – Median uptime values of all the crashes that are reported;
  - Number of bugs that are closed with the status field set to FIXED and UNCONFIRMED;
  – The time spent to fix the bug;
  - The total number of lines of code of all files contained in a version. 
  - Mean of the McCabe Cyclomatic Complexity of all files. The McCabe Cyclomatic Complexity of a file counts the number of linearly independent paths through the source code contained in the file.
  - Duration in days of the development phase 
  - The number of days an old release is still in use after the release is available. 

# RQ4. How do the studies mine release information?

The authors mined:
  - The Mozilla wiki
  - Socorro crash report server
  - Post-release bug reports linked to the crash reports
  - Firefox Bugzilla issue tracker
  - The Firefox Mercurial repository

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Wilcoxon rank-sum test) to compare the metrics in traditional and rapid release cycles. 

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Firefox releases from 3.6, 4.0, 5.0. 6.0, 7.0, 8.0 and 9.0.

  - The crash report data for all versions of Firefox that were released from January 1, 2010, to December 21, 2011, i.e., 25 alpha versions, 25 beta versions, 29 minor versions, and seven major versions that were released within one year before and after the move to the rapid release model.
