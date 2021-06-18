---
@InProceedings{ihara2017understanding,
  author       = {Ihara, Akinori and Fujibayashi, Daiki and Suwa, Hirohiko and Kula, Raula Gaikovina and Matsumoto, Kenichi},
  booktitle    = {IFIP International Conference on Open Source Systems},
  title        = {Understanding When to Adopt a Library: A Case Study on ASF Projects},
  year         = {2017},
  organization = {Springer, Cham},
  pages        = {128--138},
  groups       = {forward_1, mantyla2015rapid, selected, Other Studies},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors states that projects may release new versions in three months, but do not explicit define a rapid release cycle.

# RQ2. What are the implications of adopting a rapid release cycle?

  1. Software projects update earlier to rapid release cycle libraries than longer release cycle libraries.

  2. Software projects are more likely to adopt the latest version of a library that adopt rapid release cycle than libraries with a longer release cycle.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Time to adopt the new library release (days)

# RQ4. How do the studies mine release information?

The authors mined the project dependency defined in each Maven pom.xml.

# RQ5. How do the studies evaluate their findings?

The authors used the Scott-Knott test to group libraries into statistically distinct ranks according to their release periods but did not conduct a statistical test to validate their findings.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

The authors studied the release cycle of 23 libraries and how they were adopted by 415 Apache Software Foundation java software projects on July 21, 2016.
