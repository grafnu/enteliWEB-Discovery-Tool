Examples for BACnet device / object / property discover using REST API provided by enteliWEB Software

There is a cloud based enteliWEB, connected to virtual BACnet devices running in Delta Cloud Engineering that is used
in these examples

URL for enteliWEB - https://eu.deltacontrols.com

Authenticate using OAuth 2.0
  Username = Partner
  Password = DemoomeD
 
 BACnet Site Name - Benson House
 Containing 90 Virtual devices to provide a virtual building. Note that the FCU controllers at addresses 
 101-118 / 201-218 / 301-318 have a simulation running in their control strategy that make readings change
 in order to provide realistic simulated data
 
 example REST calls:
 
  To get a list of BACnet devicesas a JSON dictionary:-
  
    GET ('https://eu.entelicloud.com/enteliweb/api/.bacnet/Benson House?alt=json')
   
   To get a list of BACnet objects within a BACnet device:-
   
    GET ('https://eu.entelicloud.com/enteliweb/api/.bacnet/Benson House/101?alt=json')
   
   To get a list of BACnet properties within a BACnet object of a BACnet device:-
   
    GET ('https://eu.entelicloud.com/enteliweb/api/.bacnet/Benson House/101/analog-input,1?alt=json
   
   To get one specific BACnet property from a BACnet object of a BACnet device:-
   
    GET ('https://eu.entelicloud.com/enteliweb/api/.bacnet/Benson House/101/analog-input,1/present_value?alt=json
    (note the 'Property Name' must be a BACnet property as defined in ISO-16484-5
  
  Supports BACnet Rev 19
  
