from xml.etree import ElementTree


class AAS:
    id_short = "{http://www.admin-shell.io/aas/1/0}idShort"
    description = "{http://www.admin-shell.io/aas/1/0}description"
    identification = "{http://www.admin-shell.io/aas/1/0}identification"
    embedded_data_specification = "{http://www.admin-shell.io/aas/1/0}embeddedDataSpecification"
    data_specification_content = "{http://www.admin-shell.io/aas/1/0}dataSpecificationContent"
    preferred_name = "{http://www.admin-shell.io/IEC61360/1/0}preferredName"
    short_name = "{http://www.admin-shell.io/IEC61360/1/0}shortName"
    unit = "{http://www.admin-shell.io/IEC61360/1/0}unit"
    source_of_definiton = "{http://www.admin-shell.io/IEC61360/1/0}sourceOfDefinition"
    datatype = "{http://www.admin-shell.io/IEC61360/1/0}dataType"
    definition = "{http://www.admin-shell.io/IEC61360/1/0}definition"


for concept_description in ElementTree.parse("conceptDescriptions.xml").getroot():

    uri = None
    id_short = None
    preferred_name = None
    short_name = None
    definition = None
    isCaseOf = None

    for child in concept_description:
        if child.tag == AAS.id_short:
            id_short = child.text
        elif child.tag == AAS.identification:
            uri = child.text
        elif child.tag == AAS.embedded_data_specification:
            for prop in child:
                if prop.tag == AAS.data_specification_content:
                    for propchild in prop[0]:
                        if propchild.tag == AAS.preferred_name:
                            preferred_name = propchild.text
                        elif propchild.tag == AAS.short_name:
                            short_name = propchild.text
                        elif propchild.tag == AAS.datatype:
                            isCaseOf = str(propchild.text).lower()
                        elif propchild.tag == AAS.definition:
                            definition = propchild[0].text
    rdf = ""
    rdf += "<"+str(uri)+">\n"
    rdf += "    a rami:conceptDictionary ;\n"
    rdf += "    rami:idShort \""+id_short+"\"^^xsd:string ;\n"
    rdf += "    rdfs:label \""+id_short+"-ConceptDictionary\"^^xsd:string ;\n"
    rdf += "    rdfs:coment \"The ConceptDictionary contains the ConceptDescription of the property '"+str(id_short)+"'\"@en ;\n"
    rdf += "    rami:hasConceptDescription [\n"
    rdf += "        a rami:conceptDescription ;\n"
    if preferred_name is not None and str(preferred_name).strip(" ").strip("\n") is not "" :
        rdf += "        rami:preferredName \""+preferred_name+"\"@en ;\n"
    else :
        if short_name is not None:
            rdf += "        rami:preferredName \"" + short_name + "\"@en ;\n"
    if short_name is not None:
        rdf += "        rami:shortName \""+short_name+"\"^^xsd:string ;\n"
    if definition is not None:
        rdf += "        rami:definition \""+definition+"\"@en ;\n"
    rdf += "    ] ; \n"
    rdf += "    rami:hasDataSpecification _:DataSpecificationIEC61360 ."

    print(rdf)