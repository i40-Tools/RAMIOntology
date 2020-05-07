# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [2.0.1] 2020-05-30
Version 2.0.1 of the AAS RDF Serialization


### Added

* `http://admin-shell.io/aas/2/0/Key/idType` propert for `aas:Key`
* `PolicyDecisionPoint/externalPolicyDecisionPoints`
* `http://admin-shell.io/aas/2/0/Property/value`
* `http://admin-shell.io/aas/2/0/ReferenceElement/value`
* `http://admin-shell.io/aas/2/0/SubmodelElementCollection/value`


### Changed

* Namespace:  from `aas: <https://www.admin-shell.io/aas/2/0/rdf#>` to `aas: <http://admin-shell.io/aas/2/0/>`
* reorganized all attributes to their classes with the pattern NAMESPACE '/' CLASS '/' ATTRIBUTE
* `rdfs:label "some label"@en` to `rdfs:label "some label"^^xsd:string` as the label is not dependent on the English language.
* `aas:assetKind` to `http://admin-shell.io/aas/2/0/Asset/kind`
* `aas:DataSpecificationPhysicalUnit` to `http://admin-shell.io/DataSpecificationTemplates/DataSpecificationPhysicalUnit/2/0/`
* `aas:DataSpecificationIEC61360` to `http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0/DataSpecificationIEC61360`
* `aas:DataTypeIEC61360` to `http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0/DataTypeIEC61360` together with all of its instances
* `aas:DataSpecificationPhysicalUnit` to `http://admin-shell.io/DataSpecificationTemplates/DataSpecificationPhysicalUnit/2/0/` together with all of its attributes
* `aas:keyElement` to `http://admin-shell.io/aas/2/0/Key/type`
* `PolicyEnforcementPoint/externalPolicyDecisionPoints` to `PolicyEnforcementPoint/externalPolicyEnforcementPoint`
* `aas:propertyValueId` to `http://admin-shell.io/aas/2/0/Property/valueId`
* `aas:isCaseOf rdfs:domain aas:Reference .` to `aas:isCaseOf rdfs:range aas:Reference .`
* `aas:relationsshipFirst` to `http://admin-shell.io/aas/2/0/RelationshipElement/first`
* `aas:relationsshipSecond` to `http://admin-shell.io/aas/2/0/RelationshipElement/second`
* `aas:propertyCategory` to `http://admin-shell.io/aas/2/0/Property/category`


### Removed

* `owl:disjointWith` annotations as their added value is limited and the potential to create conflicts is high.
* `aas:describes` is not in the AAS Meta Model anymore.
* Class `aas:Category` does not exist in the AAS Meta Model.
* `aas:sourceOfDefinition` and `aas:definition`
* `aas:inAccordanceWith`
* `aas:embeddedDataSpecification`
