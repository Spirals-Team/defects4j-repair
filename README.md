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
Resuls of August 2016 on Defects4j version [0.1.0](https://github.com/rjust/defects4j/releases/tag/v0.1.0) (minus the Clojure bugs, discarded):

* Nopol: 35 bugs fixed 
* jGenprog/Astor: 27 bugs fixed
* jKali: 22 bugs fixed

Repair tools used
-----------------

* https://github.com/SpoonLabs/nopol
* https://github.com/SpoonLabs/astor (for jGenprog/jKali)

