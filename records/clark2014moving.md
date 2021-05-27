---
@InProceedings{clark2014moving,
  author    = {Clark, Sandy and Collis, Michael and Blaze, Matt and Smith, Jonathan M},
  booktitle = {Proceedings of the 2014 ACM SIGSAC Conference on Computer and Communications Security},
  title     = {Moving targets: Security and rapid-release in firefox},
  year      = {2014},
  pages     = {1256--1266},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors use Firefox rapid release cycle, which comprises a major release every six weeks.

# RQ2. What are the implications of adopting a rapid release cycle?

  1. The rate of vulnerability disclosure has not increased in the rapid release cycle.
  
  2. The majority of vulnerabilities discovered and disclosed are not in the new code.

  3. Vulnerabilities originating in the rapid release cycle are almost all not disclosed until newer releases have obsoleted that release.

  4. Rapid release cycle does not appear to produce more vulnerable software.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Line of code (LOC) and file counts per release
  - Number of vulnerabilities per release

# RQ4. How do the studies mine release information?

The author mined:
  - The Firefox Bugzilla bug database; 
  - Mozilla Foundation Security Advisory (MFSA); 
  - The National Vulnerability Database (NVD); and
  - The Firefox Mercurial repository.

They scraped the NVD database for all Firefox vulnerabilities and crossreferenced each vulnerability disclosed with its corresponding
MFSA and Bugzilla issue.

# RQ5. How do the studies evaluate their findings?

The author compared the metrics but did not run hypothesis tests.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

- 48 Firefox releases from 4.0 to 20.0.

617 new Bug IDs were issued, corresponding to new vulnerabilities
reported in the MFSAs [39] and CVE [22] database,