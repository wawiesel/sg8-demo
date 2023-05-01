Instructions
------------

If you are a criticality safety expert who has used ICSBEP benchmarks, please
help us and participate in this activity! If you are not, please forward this 
to criticality safety experts in your organization.

Download the [sg8-v1.0-feedback-form.xlsx](sg8-v1.0-feedback-form.xlsx) and add your ratings, comments,
and suggestions for improvement for ICSBEP benchmarks you have used. Additional
instructions are inside the excel sheet.

Send the form to Will Wieselquist (SG-8 lead) at ww5@ornl.gov to be 
incorporated into this repository.

Forms may be updated numerous times. Please don't hesitate to send me numerous
updates. Any updates can be reincorporated. 


Contents
--------

This repository will contain the data by individual in the `feedback` and then
combined into one `summary.csv` file for analysis via `scripts/sg8-v1-post.py`.

For example, to add the contents of two feedback forms to the summary.csv,
one wold execute:

```
python3 scripts/sg8-v1-post.py feedback/Marshall.xlsx summary.csv
python3 scripts/sg8-v1-post.py feedback/Percher.xlsx summary.csv
```

There is a directory with some test files at `scripts/tests` to practice
using the sg-v1-post.py script.

```
$ python3 ../sg8-v1-post.py example.xlsx example.csv
Reading data from: example.xlsx
Scanning for all cases: 4952it [00:00, 14284.15it/s]
Processing rows: 4952it [00:00, 15314.38it/s]
Done.
```

This produces a CSV [example.csv](scripts/tests/example.csv), excerpt shown 
below.

```
"Case","Rev","Author","Rating","ModelIssue","BiasIssue","UncertaintyIssue","ImprovementsRecommended","AdditionalNotes"
"HEU-MET-FAST-003-001",0,"J. Doe","4.0",False,False,False,"","In this series, it seems that experiments involving a tungsten carbide reflector calculate high by more than 1 % for some of them. This overestimation standing outside the 3σ, being not observed for other other HMF experiments and being the same whatever the code that is used, it could be due to the nuclear data of tungsten. It has been checked that the trend increases witht the reflector thickness, showing that keff is sensitive to the nuclear data of tungsten."
"LEU-COMP-THERM-078-001",0,"J. Doe","4.0",False,False,False,"","The tight grouping of the results indicates low uncertainty and low variability from one case to another. The layout differeces are small, so the results may be highly correlated, but even if examined simply as reproducability measurements they demonstrate high precision."
"LEU-COMP-THERM-027-004",2,"J. Doe","3.0",False,True,False,"Some overestimation (outside the 3 σ of the experimental uncertainties) appears for some cases depending on the gap thickness between the lattice of rods and the lead reflector screen and also depending of the lead reflector screen thickness. ","It is observed for all codes and is more or less significant depending of the nuclear data. An improvement of the lead nuclear data (angular distributions and cross sections) could lead to an improvement of results."
"PU-MET-FAST-001-001",4,"J. Doe","2.0",False,False,True,"Density of the plutonium parts is not specified and thus experimental uncertainties are too small. ","While the fourth revision to PMF-001 included much new geometry data and significantly revised the original evaluation, since this is a fast, bare plutonium assembly, the density has a very large effect on keff. Given the density is not precisely known, the experimental uncertainties are too small."
"PU-MET-FAST-008-001",2,"J. Doe","2.0",False,False,True,"Uncertainty of 0.0006- way too small, especially considering the model is an idealized sphere. All uncertainties were experimentally determined and no composition or geometry uncertainties were anlayzed. No room return or machine uncertainties included. ",""
"PU-SOL-THERM-033-001",0,"J. Doe","2.0",False,True,False,"This series of experiments exhibits an overall underestimation of keff that can be strong and that is not consistent with other PST series. ","Pyrex tubes or Rashig rings are involved in the configurations; however it is not sure that such discrepancies can be explained by the pyrex tubes or Rashig rings all the more that some discrepancies are observed even without these absorbers. As a consequence, the composition of the plutonium nitrate solution could be responsible for that tendency and in particular the stoichiometry in nitrate that has been found erroneous for other series."
"PU-SOL-THERM-033-025",0,"J. Doe","2.0",False,True,False,"This series of experiments exhibits an overall underestimation of keff that can be strong and that is not consistent with other PST series. ","Pyrex tubes or Rashig rings are involved in the configurations; however it is not sure that such discrepancies can be explained by the pyrex tubes or Rashig rings all the more that some discrepancies are observed even without these absorbers. As a consequence, the composition of the plutonium nitrate solution could be responsible for that tendency and in particular the stoichiometry in nitrate that has been found erroneous for other series."
"LEU-COMP-THERM-033-028",0,"J. Doe","2.0",False,True,False,"Calculations using various librairies higlighted relatively higher keff values for the 3%-enriched uranium (Cases 17 to 22 and 47 to 52). Experimental keff uncertainties are of the same order whatever the U235 enrichment. Need to check information about the 3% enriched UF4 powder.","Homogeneous mixtures of divided uranium fluoride (UF4) dispersed in paraffin. The uranium fluoride was dispersed in the paraffin to produce essentially homogeneous mixtures with H/U atomic ratios ranging from 4 to 20. The uranium in the fuel mixtures contained either 2 or 3 wt.% 235U."
"LEU-COMP-THERM-033-045",0,"J. Doe","2.0",False,True,False,"Calculations using various librairies higlighted relatively higher keff values for the 3%-enriched uranium (Cases 17 to 22 and 47 to 52). Experimental keff uncertainties are of the same order whatever the U235 enrichment. Need to check information about the 3% enriched UF4 powder.","Homogeneous mixtures of divided uranium fluoride (UF4) dispersed in paraffin. The uranium fluoride was dispersed in the paraffin to produce essentially homogeneous mixtures with H/U atomic ratios ranging from 4 to 20. The uranium in the fuel mixtures contained either 2 or 3 wt.% 235U."
"MIX-SOL-THERM-010-007",0,"J. Doe","2.0",False,True,False,"The uncertainty in Fe and other impurities discussed in Section 2.1.8 is treated as a bias and not an uncertainty. It seems that this should be treated as an uncertainty. ","If these biases are treated as uncertainties, calculated and expected results agree better for a number of codes and cross section sets."
"MIX-SOL-THERM-010-009",0,"J. Doe","2.0",False,True,False,"The uncertainty in Fe and other impurities discussed in Section 2.1.8 is treated as a bias and not an uncertainty. It seems that this should be treated as an uncertainty. ","If these biases are treated as uncertainties, calculated and expected results agree better for a number of codes and cross section sets."
"PU-COMP-MIXED-002-006",0,"J. Doe","1.0",False,False,True,"There are a number of unquantified or under-quantified uncertainties, such as the composition and thickness of contamination control material (tape and plastic wrap) that covered each plutonium oxide-containing polyethylene box in the array. Other uncertainties could arise from the plutonium oxide density, heterogeneity of the oxide and polystyrene moderator, thermal expansion of the boxes, and loss of hydrogen due to radiolysis in the moderator. No temperature data reported, but the reason for the contaimination control material was because the boxes got so hot that they melted the glue holding the PE boxes together.","These benchmarks represent the only loose plutonium oxide benchmarks in the handbook, and have historically been considered important for criticality safety validation. "
"PU-COMP-MIXED-002-022",0,"J. Doe","1.0",False,False,True,"There are a number of unquantified or under-quantified uncertainties, such as the composition and thickness of contamination control material (tape and plastic wrap) that covered each plutonium oxide-containing polyethylene box in the array. Other uncertainties could arise from the plutonium oxide density, heterogeneity of the oxide and polystyrene moderator, thermal expansion of the boxes, and loss of hydrogen due to radiolysis in the moderator. No temperature data reported, but the reason for the contaimination control material was because the boxes got so hot that they melted the glue holding the PE boxes together.","These benchmarks represent the only loose plutonium oxide benchmarks in the handbook, and have historically been considered important for criticality safety validation. "
"MIX-COMP-THERM-012-001",1,"J. Doe","1.0",False,True,False,"There is an inconsistency between cases results. A strong overestimation by more than 3% is observed for some cases whereas a strong underestimation by 3% is observed for others whatever the library. ","This discrepancy is not common to other MCT series. The composition of the polystyrene boxes could be at stake. Indeed some parameters were derived from calculations."
"MIX-COMP-THERM-012-015",1,"J. Doe","1.0",False,True,False,"There is an inconsistency between cases results. A strong overestimation by more than 3% is observed for some cases whereas a strong underestimation by 3% is observed for others whatever the library. ","This discrepancy is not common to other MCT series. The composition of the polystyrene boxes could be at stake. Indeed some parameters were derived from calculations."
"MIX-COMP-THERM-012-033",1,"J. Doe","1.0",False,True,False,"There is an inconsistency between cases results. A strong overestimation by more than 3% is observed for some cases whereas a strong underestimation by 3% is observed for others whatever the library. ","This discrepancy is not common to other MCT series. The composition of the polystyrene boxes could be at stake. Indeed some parameters were derived from calculations."
```

What is SG-8
------------

Subgroup 8 (SG-8) is an OECD/NEA Working Party for Nuclear Criticality Safety (WPNCS)
sub group charged with developing a methodology for collecting and disseminating 
feedback on evaluations from qualified experts to better serve users of the 
ICSBEP benchmarks.

Over twenty-five years of benchmarking activity, the expectations and review 
rigor required for ICSBEP has evolved, the benchmarks are being used for 
unanticipated scenarios, tools and computational power exist to solve more 
complex problems, and new practitioners are entering the field. 

A need has been recognized to preserve expert knowledge and judgement regarding 
the suitability of ICSBEP evaluations to common uses such as modern code validation, 
nuclear data evaluation, and nuclear data adjustment. 


Technical Significance
----------------------

With the increasing rigor of the ICSBEP review process, there exists a 
disparity between earlier and modern benchmarks in terms of uncertainty 
quantification and more realistic modelling of the configurations. For example, 
earlier benchmarks may quote unrealistic uncertainties that are then used to 
set safety limits or assess nuclear data evaluations. Additionally, there are 
benchmarks that have clear consistency problems, internally across cases or 
compared to other, similar benchmarks.
