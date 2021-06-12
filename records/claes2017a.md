---
@InProceedings{Claes2017a,
  author    = {Claes, M. and M{\"a}ntyl{\"a}, M. and Kuutila, M. and Adams, B.},
  booktitle  = {2017 {{IEEE}}/{{ACM}} 14th {{International Conference}} on {{Mining Software Repositories}} ({{MSR}})},
  title      = {Abnormal {{Working Hours}}: {{Effect}} of {{Rapid Releases}} and {{Implications}} to {{Work Content}}},
  year       = {2017},
  month      = may,
  pages      = {243--247},
  doi        = {10.1109/MSR.2017.3},
  shorttitle = {Abnormal {{Working Hours}}},
  timestamp  = {2020-10-29T20:49:21Z},
}
---

# RQ1. What characterizes a rapid release cycle?


# RQ2. What are the implications of adopting a rapid release cycle?

  1. In the rapid release cycle, fewer comments were registered during weekend and night, which suggest that adopting the rapid elease cycle reduced weekend and night work.

  2. However, in the rapid release cycle the number of developers paid by Mozilla was increased.

  3. The results suggest that moving to rapid releases have positive impact on the work health and work-life-balance of software engineers.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  -  number of comments for each hour of the day.

# RQ4. How do the studies mine release information?

The authors extracted bug comments from Mozilla’s Bugzilla repository using the GrimoireLab tools2 and the Firefox Mercurial repositories to extract the code revision history.

# RQ5. How do the studies evaluate their findings?

The authors conducted statistical tests  (Mann–Whitney U test, Cliff’s delta) and calculated correlation (Cohen’s d) to compare the metrics in traditional and rapid release cycles.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Firefox and Firefox OS comments written between 2012-12-21 and 2016-01-03. These dates correspond to Firefox OS release 1.0 to 2.5.
