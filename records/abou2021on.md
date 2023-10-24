---
@Article{AbouKhalil2021,
  author    = {Abou Khalil, Zeinab and Constantinou, Eleni and Mens, Tom and Duchien, Laurence},
  journal   = {Journal of Systems and Software},
  title     = {On the impact of release policies on bug handling activity: A case study of Eclipse},
  year      = {2021},
  pages     = {110882},
  volume    = {173},
  groups    = {abou2019, forward_2, joshi2019, khomh2012, daCosta2016impact, forward_3, daCosta2018impact, khomh2015understanding, mantyla2015rapid, Others, selected},
  publisher = {Elsevier},
}
---

# RQ1. What characterizes a rapid release cycle?

Quarterly (i.e., every 12 to 13 weeks).

# RQ2. What are the implications of adopting a rapid release cycle?

One consulted maintainer stated that long release cycles lead to a higher amount
of bugs that are not important or relevant to the bug reporter anymore because
users found a workaround, or because the tooling has changed since. With shorter
cycles, this is no longer the case, so it becomes less relevant for maintainers
to distinguish between important and less important bugs.

There is no significant change in bug handling rate behavior after the switch in
quarterly releases. There is a tendency to resolve more non-severe than severe
bugs after the release. 

Bugs are triaged faster after the switch to quarterly releases.

Bugs are fixed faster after the transition to the quarterly releases.

More effort is spent on fixing bugs during the feature freeze period than during
the development period. This difference in effort appears to have increased for
quarterly releases.

Bugs of the current release that are triaged and fixed during the feature freeze
period have stayed open longer compared to those in the development period for
the annual releases while this is not the case anymore for the quarterly
releases.

Feature freeze periods impose extra stress during rapid releases, since they
tend to be relatively short and, in addition, they take away an important part
of the time that could otherwise be devoted to development of new features.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

 - Bug triaging time;
 - Bug fixing time;
 - Bug resolution rate;
 - Bug fixing rate;
 - Bug severity; and
 - Feature freeze period.

# RQ4. How do the studies mine release information?

The authors mined bug reports extracted from Bugzilla for each Eclipse release.
They used Disco to mine the bug reports, which is a tool that helps in the
mining process but not specific for releases. The authors used the time of the
release to separate the bugs.

# RQ5. How do the studies evaluate their findings?

Kolmogorov–Smirnov test to test normality
Two-sided t-test
Welch t-test
Wilcoxon rank-sum 
Mann–Whitney U test
Cliff’s delta d

Qualitative analysis: Feedback from 5 eclipse maintainers to confirm the findings.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

Releases from 3.0 and 4.15. Plus seven annual releases (4.2–4.8) against seven
quarterly releases (4.9–4.15) from eclipse project. 36K bug reports from
Bugzilla.
