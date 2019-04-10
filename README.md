# RAMIOntology
Repository containing the developing of the RAMI vocabulary.

The Reference Architecture Model Industry 4.0 that was developed by the [**`Platform Industry 4.0`**](https://www.plattform-i40.de/PI40/Navigation/DE/Home/home.html) is a three-dimensional map showing how to approach the issue of Industry 4.0 in a structured manner. RAMI ensures that all participants involved in Industry 4.0 discussions understand each other. The concept of the RAMI is based on data and is closely associated with the Industrial Data Space (IDS).

The main question is: *Who provides the data for intepretation?* It is the "digital-twin" of each asset. The official name for this is **Asset-Administration-Shell** (AAS).
The AAS provides organizations the opportunity to share data and exchange it in "value chains"/"value networks".

![example](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0v_gGsBH7qGsdDBYS_z-OuqsvYXvjgImxHlZLQZ_Rv6oCtdqjYQ "AAS example")

The RAMIOntology is based on the document [**`details_of_the_AAS.pdf`**](https://www.zvei.org/fileadmin/user_upload/Presse_und_Medien/Publikationen/2018/November/Details_of-the_Asset_Administration_Shell/Details_of-the_Asset_Administration_Shell.PDF). This document specifies the structural principles of the AAS and and outlines a metamodel. The goal of this document was to specify mandatory and optional attributes using RDF-serialization. Furthermore it was necessary to check all dependecies and modify the metamodel to provide a transparent model that can be integrated into the reference architecture model.

The [**`shapes`**](schema/) in this repository are available for validation and are all based on the metamodel. There were some iterations, so they don't match 100%. The annotated version of this document can be downloaded [here](http://116.203.149.114/2018-verwaltungsschale-im-detail-annotated-umls.pdf).

The Ontology contains the vocabulary that is necessary for the RAMI-AAS.

Use the [shacl-playground](http://shacl.org/playground/) to check if your RDF-model is conform to the shape.

We tested some shapes using the shacl playground. The tested files are stored with their output in the [tests-directory](tests).

***
## The Example
The **`Raspberry Pi 3b+`** was used as an example of an asset that is described in an AAS
- we created a valid [**`AASX-archive`**](RaspberryPi3bPlus_EXAMPLE/Raspberry_Pi_3b_plus.aasx)
    - this AASX-archive contains a [**`XML-model`**](RaspberryPi3bPlus_EXAMPLE/Raspberry_Pi_3b_plus/aasx/iais_fraunhofer_de_en_aas_examples/iais_fraunhofer_de_en_aas_examples_raspberry_pi_3b_plus.aas.xml) which contains all conceptDescriptions and information about the asset
- we created also a [**`RDF-model`**](RaspberryPi3bPlus_EXAMPLE/rdfttlsolution.ttl)
    - based on the [**`modified metamodel`**](http://116.203.149.114/2018-verwaltungsschale-im-detail-annotated-umls.pdf)
    - conform to [**`shapes`**](schema/)

The information content is almost the same. The models match from the raw data, but the asset can still be displayed more clearly with all dependencies by using RDF.

### Reasoning
We created a rami-ruleset that contains:
- basic rules that are extensions of the metamodel

In addition we created a domain-specific-ruleset for all computing devices, i.e. Raspberry Pis
These rules detect if the asset is for example:
- a computer
- carriable by a human
- a powered device
- PoE suppliable
- ...

We evaluated the rdf-model of the Raspberry Pi 3b+. The output file is called [**`rdfttlsolution_with_reasoning.nt`**](RaspberryPi3bPlus_EXAMPLE/evaluated/rdfttlsolution_with_reasoning.nt) and contains around 334 derived triples.

***
We used [Linked-Data-Fu](https://linked-data-fu.github.io) for reasoning.

We edited the Ontology with [Protégé](https://protege.stanford.edu).
