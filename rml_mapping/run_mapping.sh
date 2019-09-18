#!/bin/bash

SUFFIX=.rml.ttl
INPUT=$1
FILE=${INPUT%"$SUFFIX"}



#--------------- Turtle Mapping -------------------
STARTTIME=$(date +%s%N)

java -jar rmlmapper-4.3.3-r95.jar -m $1 -s turtle -o "examples/"$FILE".ttl"

ENDTIME=$(date +%s%N)
TIME_TTL=$((($ENDTIME - $STARTTIME)/1000000))

echo 'Turtle mapping took an average of ' $TIME_TTL


#--------------- NQuad Mapping -------------------
STARTTIME=$(date +%s%N)

java -jar rmlmapper-4.3.3-r95.jar -v -m $1 -s nquads -o $FILE".nq"

ENDTIME=$(date +%s%N)
TIME_NQ=$((($ENDTIME - $STARTTIME)/1000000))

echo 'NQuad mapping took an average of ' $TIME_NQ

#--------------- JSON-LD Mapping -------------------
STARTTIME=$(date +%s%N)

java -jar rmlmapper-4.3.3-r95.jar -m $1 -s jsonld -o "examples/"$FILE".jsonld"

ENDTIME=$(date +%s%N)
TIME_JSON=$((($ENDTIME - $STARTTIME)/1000000))

echo 'JSON-LD mapping took an average of ' $TIME_JSON
