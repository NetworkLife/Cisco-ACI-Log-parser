# Cisco-ACI-Log-parser
Improve/speed the parsing of Cisco ACI logs (eventRecord, faultRecord, fabricNode, aaaModLR...). One script at a time :)

##

*** I'm creating this project as a way to improve my Python skills, while following DevNet study plan ***

## Start by getting the ACI logs from an APIC Controller, as recommended by the TAC

Login to an apic controller:

    bash
    mkdir /tmp/tac-basic-output
    cd /tmp/tac-basic-output

    Run one icurl at time in bash mode (Important)
    icurl 'http://localhost:7777/api/class/firmwareARunning.xml' > firmwareARunning.xml
    icurl 'http://localhost:7777/api/class/fabricNode.xml' > fabricNode.xml
    icurl 'http://localhost:7777/api/class/faultInfo.xml' > faultInfo.xml
    icurl 'http://localhost:7777/api/class/aaaModLR.xml?order-by=aaaModLR.created|desc&page-size=100000' > aaaModLR.xml
    icurl 'http://localhost:7777/api/class/faultRecord.xml?order-by=faultRecord.created|desc&page-size=100000&page=0' > faultRecord-0.xml
    icurl 'http://localhost:7777/api/class/faultRecord.xml?order-by=faultRecord.created|desc&page-size=100000&page=1' > faultRecord-1.xml
    icurl 'http://localhost:7777/api/class/faultRecord.xml?order-by=faultRecord.created|desc&page-size=100000&page=2' > faultRecord-2.xml
    icurl 'http://localhost:7777/api/class/faultRecord.xml?order-by=faultRecord.created|desc&page-size=100000&page=3' > faultRecord-3.xml
    icurl 'http://localhost:7777/api/class/faultRecord.xml?order-by=faultRecord.created|desc&page-size=100000&page=4' > faultRecord-4.xml
    icurl 'http://localhost:7777/api/class/eventRecord.xml?order-by=eventRecord.created|desc&page-size=100000&page=0' > eventRecord-0.xml
    icurl 'http://localhost:7777/api/class/eventRecord.xml?order-by=eventRecord.created|desc&page-size=100000&page=1' > eventRecord-1.xml
    icurl 'http://localhost:7777/api/class/eventRecord.xml?order-by=eventRecord.created|desc&page-size=100000&page=2' > eventRecord-2.xml
    icurl 'http://localhost:7777/api/class/eventRecord.xml?order-by=eventRecord.created|desc&page-size=100000&page=3' > eventRecord-3.xml
    icurl 'http://localhost:7777/api/class/eventRecord.xml?order-by=eventRecord.created|desc&page-size=100000&page=4' > eventRecord-4.xml
    cd /tmp
    tar zcf tac-basic-output.tgz tac-basic-output
    cp tac-basic-output.tgz /data/techsupport
    rm -r tac-basic-output

Extract tac-basic-output.tgz in the same folder as the Python script explained in the next chapter

## Parser script

This script takes all .xml files of the folder, prettyPrint them with the lxml module, and search for a specific string inside.

    Prerequisites:
        pip install lxml

    Args:
        x: word to search

    Returns:
        The lines matching the word we are searching for

### How to use it ?
Launch the script with the "string" to be found, as the firsts argument

>python parser.py **string**

    Ben> python parser.py FDO12345678
    +----------------+
    | fabricNode.xml |
    +----------------+
    Lines inside fabricNode.xml matching the word: FDO12345678

      <fabricNode adSt="on" address="192.168.1.2" annotation="" apicType="apic" childAction="" delayedHeartbeat="no" dn="topology/pod-1/node-201" extMngdBy="" fabricSt="active" id="201" lastStateModTs="2020-04-14T11:08:35.433+01:00" lcOwn="local" modTs="2020-04-14T11:08:35.510+01:00" model="N9K-C93180YC-FX" monPolDn="uni/fabric/monfab-default" name="Leaf201" nameAlias="" nodeType="unspecified" role="leaf" serial="FDO12345678" status="" uid="0" vendor="Cisco Systems, Inc" version=""/>
