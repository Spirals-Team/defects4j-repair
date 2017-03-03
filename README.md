# Defects4j-Repair

This repository contains the raw experimental results of the experiments done at INRIA Lille on the automatic repair of the bugs of the Defects4J dataset. They are discussed in [Automatic Repair of Real Bugs in Java: A Large-Scale Experiment on the Defects4J Dataset (Matias Martinez, Thomas Durieux, Romain Sommerard, Jifeng Xuan and Martin Monperrus), In Springer Empirical Software Engineering, 2016.](https://hal.archives-ouvertes.fr/hal-01387556/document)

```
@article{martinez2016,
 title = {{Automatic Repair of Real Bugs in Java: A Large-Scale Experiment on the Defects4J Dataset}},
 author = {Matias Martinez and Thomas Durieux and Romain Sommerard and Jifeng Xuan and Martin Monperrus},
 journal = {Springer Empirical Software Engineering},
 year = {2016},
 url = {https://hal.archives-ouvertes.fr/hal-01387556/document},
 doi = {10.1007/s10664-016-9470-4},
}
```

Warning: this repo contains more than 8GB of data.

[Results of March 2017](https://github.com/Spirals-Team/defects4j-repair/tree/master/results/2017-march) on 395 bugs of [Defects4j](https://github.com/rjust/defects4j) version [1.1.0](https://github.com/rjust/defects4j/releases/tag/v1.1.0) (all projects considered). See [The Patches of the Nopol Automatic Repair System on the Bugs of Defects4J version 1.1.0](https://hal.archives-ouvertes.fr/hal-01480084)

* Nopol-SMT: 103 bugs repaired with one test-suite adequate patch
    * Chart: 9 bugs repaired with one test-suite adequate patch
    * Closure: 56 bugs repaired with one test-suite adequate patch
    * Lang: 4 bugs repaired with one test-suite adequate patch
    * Math: 24 bugs repaired with one test-suite adequate patch
    * Mockito: 2 bugs repaired with one test-suite adequate patch
    * Time: 8 bugs repaired with one test-suite adequate patch


[Results of August 2015](https://github.com/Spirals-Team/defects4j-repair/tree/master/results/2015-august) on 224 bugs of [Defects4j](https://github.com/rjust/defects4j) version [0.1.0](https://github.com/rjust/defects4j/releases/tag/v0.1.0) (minus the Clojure bugs, discarded):

* Nopol: 35 bugs with one test-suite adequate patch 
* jGenprog/Astor: 27 bugs  with one test-suite adequate patch
* jKali: 22 bugs  with one test-suite adequate patch
* Total: 47/224 bugs (20%) with at least one test-suite adequate patch

[Results of May 2015](https://github.com/Spirals-Team/defects4j-repair/tree/master/results/2015-may), used for for [Automatic Repair of Real Bugs: An Experience Report on the Defects4J Dataset](http://arxiv.org/pdf/1505.07002), Technical report 1505.07002, Arxiv, 2015.

Repair tools used
-----------------

* https://github.com/SpoonLabs/nopol
* https://github.com/SpoonLabs/astor (for jGenprog/jKali)

