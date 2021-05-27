---
@Article{khomh2015understanding,
  author    = {Khomh, Foutse and Adams, Bram and Dhaliwal, Tejinder and Zou, Ying},
  journal   = {Empirical Software Engineering},
  title     = {Understanding the impact of rapid releases on software quality},
  year      = {2015},
  number    = {2},
  pages     = {336--373},
  volume    = {20},
  groups    = {selected, start_set},
  publisher = {Springer},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a release every six weeks.


# RQ2. What are the implications of adopting a rapid release cycle?

  1. There is only a negligible difference in the number of post-release bugs between rapid and traditional release cycles. 
  
  2. Under rapid release cycles, the crash is detected significantly faster at run-time.

  3. The bugs are fixed significantly faster under a rapid release cycle. 

  4. Proportionally, fewer bugs are being fixed under the rapid release cycle, and more complex bugs are propagated to later releases.

  5. More developers are working on each rapid release, resulting in fewer changes per developer, but those changes touch more files. 
  
  6. Like traditional minor releases, the focus has shifted to continuous maintenance, i.e., most changes fix bugs instead of adding new features.
  

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Number of bugs linked to a crash report and reported after the release date
  – Median of the number of crashes per day
  – Median uptime values of all the crashes that are reported
  - Number of pre-release and post-release bugs that are closed with the status field set to FIXED
  – The duration of the fixing period of a FIXED post-release bug, i.e., the difference between the bug open time and the last modification time 
  - The total number of lines of code of all files contained in a version. 
  - Mean of the McCabe Cyclomatic Complexity of all files. The McCabe Cyclomatic Complexity of a file counts the number of linearly independent paths through the source code contained in the file.
  – Duration in days of the development phase
Monthly Active Developers: the mean number of developers changing the code per
month.
  – The mean number of commits authored per developer per
month.
  – The mean number of files modified in a commit per month.
  – The total number of new lines of code added, divided by the Development Time.


# RQ4. How do the studies mine release information?

The authors mined:
  - The Mozilla wiki
  - Socorro crash report server
  - Post-release bug reports linked to the crash reports
  - Firefox Bugzilla issue tracker
  - The Firefox Mercurial repository


# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Wilcoxon rank-sum test) to compare the metrics in traditional and rapid release cycles. 

They also interviewed a Mozilla quality assurance engineering to validate their finding and help them understand why the fiding happened.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Firefox releases from 3.0 to 13.0.

  - The crash report data for all versions of Firefox that were released from January 1, 2010, to December 21, 2011, i.e., 25 alpha versions, 25 beta versions, 29 minor versions, and seven major versions that were released within one year before and after the move to the rapid release model.

  - The version control data up to release 13
