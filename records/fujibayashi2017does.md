---
@InProceedings{fujibayashi2017does,
  author       = {Fujibayashi, Daiki and Ihara, Akinori and Suwa, Hirohiko and Kula, Raula Gaikovina and Matsumoto, Kenichi},
  booktitle    = {2017 IEEE 24th International Conference on Software Analysis, Evolution and Reengineering (SANER)},
  title        = {Does the release cycle of a library project influence when it is adopted by a client project?},
  year         = {2017},
  organization = {IEEE},
  pages        = {569--570},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors do not define a rapid release cycle.

# RQ2. What are the implications of adopting a rapid release cycle?

  1. Software projects update earlier to rapid release cycle libraries than longer release cycle libraries.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Time to adopt the new library release (days)

# RQ4. How do the studies mine release information?

The authors mined the project dependency defined in each Maven pom.xml.

# RQ5. How do the studies evaluate their findings?

The authors used the Scott-Knott test to group libraries into statistically distinct ranks according to their release periods but did not conduct a statistical test to validate their findings.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

The authors studied the release cycle of 23 libraries and how they were adopted by 415 Apache Software Foundation java software projects.
