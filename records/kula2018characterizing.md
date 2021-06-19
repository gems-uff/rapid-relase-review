---
@InProceedings{kula2018characterizing,
  author    = {Kula, Elvan and Rastogi, Ayushi and Huijgens, Hennie and van Deursen, Arie},
  booktitle = {BENEVOL},
  title     = {Characterizing Rapid Releases in a Large Banking Company: A Case Study.},
  year      = {2018},
  pages     = {56--60},
  groups    = {forward_1, daCosta2016impact, mantyla2015rapid, selected, Other Studies},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors used the mean of the distribution of release frequencies of the projects in ING, a large multinational financial organization with about 54,000 employees and over 37 million customers. They consider 3.56 weeks a rapid release.

# RQ2. What are the implications of adopting a rapid release cycle?

 1. The teams that adopt rapid release cycle are always more delayed than their traditional counterparts;
 
 2. The dependencies and infrastructure are the most common factors that are perceived to cause a delay in rapid teams.

 3. The majority of developers perceive that the small changes in code and rapid feedback improve software quality.
 
 4. The developers reported experiencing an increased deadline pressure in rapid release, which negatively affects the code quality, leads to an increase in workarounds and poor implementation choices. They also reported that rapid release cut the overall time spent on refactoring and regression testing.

 5.The cyclomatic complexity and coding issues are significantly lower in the rapid release cycle, which corresponds with the perception of developers that it gets easier to review and refactor code in a rapid release cycle.

 6. The branch coverage is significantly higher in the rapid release cycle. This result corresponds with the perception that the test process becomes more continuous and allows for more complete testing of new features.
   
 7.  The code churn is significantly higher for the rapid release cycle, indicating that there is a higher coding activity in rapid teams than in traditional teams.
   
 8. There is no significant difference between the comment density and SLOC of RRs and TRs.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Coding Standard Violations Density
  - Cyclomatic Complexity
  - Branch Coverage
  - Comment Density
  - Code Churn
  - SLOC

# RQ4. How do the studies mine release information?

The authors extracted the SonarQube measurements of releases. They classified the releases as traditional or rapid based on the time interval between their release date and the start date of the development phase.

# RQ5. How do the studies evaluate their findings?

The authors conducted a mixed-methods study, consisting of a survey with 461 engineers, and a statistical analysis of 2 years (2016-2018) of code quality data for 611 teams.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Survey with 461 engineers from ING;
  - 2 years of code quality data for 611 teams from ING.
  - Major releases of 3048 software projects.
