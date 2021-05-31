---
@InProceedings{daCosta2016impact,
  author    = {da Costa, Daniel Alencar and McIntosh, Shane and Kulesza, Uir{\'a} and Hassan, Ahmed E},
  booktitle = {Proceedings of the 13th International Conference on Mining Software Repositories},
  title     = {The impact of switching to a rapid release cycle on the integration delay of addressed issues: an empirical study of the mozilla firefox project},
  year      = {2016},
  pages     = {374--385},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a release every six weeks.

# RQ2. What are the implications of adopting a rapid release cycle?

  - There is no signifficant difference between traditional and rapid releases issues' lifetime.
  
  - The issues are addressed triaged and fixed quickly in rapid releases, but they tend to wait longer time to be integrated and released to users when considering both minor and major traditional releases.

  - The minor traditional releases tend to have less integration delay than the major and minor rapid releases.

  - Traditional releases prioritize the integration of backlog issues, while rapid releases prioritize the integration of issues of the current release cycle.

  - The length of the release cycles are roughly the same between traditional and rapid releases when considering both minor and major releases, with medians of 40 and 42 days.


# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - The issue lifetime, triaging phase, fixing phase, and integration delay.
  - Other metrics related to the issues and the project to build their explanatory model (table 2 of the paper)
  
# RQ4. How do the studies mine release information?

The authors mined:
  - Firefox release history wiki;
  - The Firefox Mercurial and CVS repositories to extract the code revision history.
  - The Firefox Bugzilla bug database; 

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Mann-Whitney-Wilcoxon tests and Cliff's delta effect-size) to compare the metrics in traditional and rapid release cycles. They normalized all metrics for the project duration.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Firefox traditional releases 1.0 to 4.0.
  - Firefox rapid releases 5 to 27.
