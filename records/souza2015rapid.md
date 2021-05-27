---
@Article{souza2015rapid,
  author     = {Souza, Rodrigo and Chavez, Christina and Bittencourt, Roberto A},
  journal    = {IEEE Software},
  title      = {Rapid releases and patch backouts: A software analytics approach},
  year       = {2015},
  number     = {2},
  pages      = {89--96},
  volume     = {32},
  groups     = {selected, start_set},
  keywords   = {read},
  publisher  = {IEEE},
  readstatus = {read},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a major release every six weeks.

# RQ2. What are the implications of adopting a rapid release cycle?

 1. The number of bug fixes per day almost doubled under the rapid release cycle.
 
 2. The overall backout rate increased under the rapid releases cycle. However, the authors explain that the backout rate under traditional releases may have been underestimated because the backout culture became more prevalent after adopting rapid releases.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Number of bug fixes
  - Number of days
  - Average number of bug fixes per day
  - Number of committers
  - Number and percentage of fixes backed out
  - Average number of bugs backed out per day
  - Early backout rate (%)
  - Late backout rate (%)
  - Fixes backed out early (%)
  - Median time-to-backout (hrs.)

# RQ4. How do the studies mine release information?

The authors mined:
  
  - The Firefox Mercurial repository to extract the commit log
  - A SQL Database with the bug reports provided by a Mozilla engineering 
  - The Mozilla wiki

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests (Wilcoxon rank-sum test and Fisher’s exact test) to compare the metrics in traditional and rapid release cycles. They also contacted Firefox engineers, using
the firefox-dev mailing list and asked to explain the numbers according to their experience.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Firefox releases 3.6, 4.0, and 5 through 27.
