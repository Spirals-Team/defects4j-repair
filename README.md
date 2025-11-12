# Defects4j-Repair: open-science data for automatic repair on Defects4J

This repository contains the raw experimental results of the experiments done at INRIA Lille on the automatic repair of the bugs of the Defects4J dataset. They are discussed in [Automatic Repair of Real Bugs in Java: A Large-Scale Experiment on the Defects4J Dataset](https://hal.archives-ouvertes.fr/hal-01387556/document) (Matias Martinez, Thomas Durieux, Romain Sommerard, Jifeng Xuan and Martin Monperrus), In Springer Empirical Software Engineering, 2016.

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

## Content of the repository 

### Repair results

[Results of March 2017](https://github.com/Spirals-Team/defects4j-repair/tree/master/results/2017-march) on 395 bugs of [Defects4j](https://github.com/rjust/defects4j) version [1.1.0](https://github.com/rjust/defects4j/releases/tag/v1.1.0) (all projects considered). See [The Patches of the Nopol Automatic Repair System on the Bugs of Defects4J version 1.1.0](https://hal.archives-ouvertes.fr/hal-01480084)

* Nopol-SMT: 103 bugs repaired with one test-suite adequate patch
    * Chart: 9 bugs repaired with one test-suite adequate patch
    * Closure: 56 bugs repaired with one test-suite adequate patch
    * Lang: 4 bugs repaired with one test-suite adequate patch
    * Math: 24 bugs repaired with one test-suite adequate patch
    * Mockito: 2 bugs repaired with one test-suite adequate patch
    * Time: 8 bugs repaired with one test-suite adequate patch


[Results of August 2015](https://github.com/Spirals-Team/defects4j-repair/tree/master/results/2015-august) on 224 bugs of [Defects4j](https://github.com/rjust/defects4j) version [0.1.0](https://github.com/rjust/defects4j/releases/tag/v0.1.0) (minus the Clojure bugs, discarded), used for [Automatic Repair of Real Bugs in Java: A Large-Scale Experiment on the Defects4J Dataset](https://hal.archives-ouvertes.fr/hal-01387556/document)

* Nopol: 35 bugs with one test-suite adequate patch 
* jGenprog/Astor: 27 bugs  with one test-suite adequate patch
* jKali: 22 bugs  with one test-suite adequate patch
* Total: 47/224 bugs (20%) with at least one test-suite adequate patch

[Results of May 2015](https://github.com/Spirals-Team/defects4j-repair/tree/master/results/2015-may), used for for [Automatic Repair of Real Bugs: An Experience Report on the Defects4J Dataset](http://arxiv.org/pdf/1505.07002), Technical report 1505.07002, Arxiv, 2015.

### Branches for each Defects4j bug

The `master` branch contains the repair results. There is also one branch per buggy version of Defects4j, for instance https://github.com/Spirals-Team/defects4j-repair/tree/Time9 contains the buggy version of `Time 9`.

See https://github.com/Spirals-Team/defects4j-repair/branches for all branches

### Scripts

https://github.com/Spirals-Team/defects4j-repair/tree/master/src contains scripts we use to run the repair tools on all bugs.

## Branches with Maven pom.xml

```
Lang1 Lang10 Lang11 Lang12 Lang13 Lang14 Lang15 Lang16 Lang17 Lang18 Lang19 Lang2 Lang20 Lang21 Lang22 Lang23 Lang24 Lang25 Lang26 Lang27 Lang28 Lang29 Lang3 Lang30 Lang31 Lang32 Lang33 Lang34 Lang35 Lang36 Lang37 Lang38 Lang39 Lang4 Lang40 Lang41 Lang42 Lang43 Lang44 Lang44-Java6 Lang45 Lang46 Lang47 Lang48 Lang49 Lang5 Lang50 Lang51 Lang51-Java6 Lang52 Lang53 Lang53-Java6 Lang54 Lang55 Lang56 Lang57 Lang58 Lang58-Java6 Lang59 Lang6 Lang7 Lang8 Lang9 Math1 Math10 Math100 Math101 Math102 Math103 Math104 Math11 Math12 Math13 Math14 Math15 Math16 Math17 Math18 Math19 Math2 Math20 Math21 Math22 Math23 Math24 Math25 Math26 Math27 Math28 Math29 Math3 Math30 Math31 Math32 Math33 Math34 Math35 Math36 Math37 Math38 Math39 Math4 Math40 Math41 Math42 Math43 Math44 Math45 Math46 Math47 Math48 Math49 Math5 Math50 Math51 Math52 Math53 Math54 Math55 Math56 Math57 Math58 Math59 Math6 Math60 Math61 Math62 Math63 Math64 Math65 Math66 Math67 Math68 Math69 Math7 Math70 Math71 Math72 Math73 Math74 Math75 Math76 Math77 Math78 Math79 Math8 Math80 Math81 Math82 Math83 Math84 Math85 Math86 Math87 Math88 Math89 Math9 Math90 Math91 Math92 Math93 Math94 Math95 Math96 Math97 Math98 Math99 Time1 Time10 Time11 Time12 Time13 Time14 Time15 Time16 Time17 Time18 Time19 Time2 Time20 Time21 Time22 Time23 Time24 Time25 Time26 Time27 Time3 Time4 Time5 Time6 Time7 Time8 Time9
```
