create
use keeper;

-- 9d0521066eb6bf894dec4e0bcf713ac2536366d9dec723e19d3de141c560316b
-- 02c88a1ac39bb0fac5acbc317377aeb204851a01804812b86c2f5fefddda7fa10f
-- 87ad31bdf40fa7911a24cd537fe4397c8436b38ec9834d525ef15ec80cec78fb
-- 030f94edd22e4a8f84dca199f8492333997ca06524451e7d8ae464135a47d0a08d

-- 8535a0e3100a23e55f6c58f08c1fc253e5781d5a9951b839539c21134a3e1dba
-- 031fa2175a903d0d4daf12cde1df624611918bb7f8ab64980ca1960aa0b32e40f2
-- 023e8d9d5101cec8fdea4e1c4a6ad15a157b40e1b1093a5f3ba731173a41e982fd
-- 09d4b78c4b6069cba3c8c29b911268eb2ec82de3ab9018c7898392a9f7671db3



Insert into keyinfo(user,privatekey,publickey,signkey,verifykey)
Values (
"0x78658C9AaD8523BB283029C43135CF87339ADC21",
"9d0521066eb6bf894dec4e0bcf713ac2536366d9dec723e19d3de141c560316b",
"02c88a1ac39bb0fac5acbc317377aeb204851a01804812b86c2f5fefddda7fa10f",
"87ad31bdf40fa7911a24cd537fe4397c8436b38ec9834d525ef15ec80cec78fb",
"030f94edd22e4a8f84dca199f8492333997ca06524451e7d8ae464135a47d0a08d");

Insert into keyinfo(user,privatekey,publickey,signkey,verifykey)
Values (
"0x7161a4eCE5dD841756ee38cBEa7da055F29302c9",
"52bbf9b095ddfe609b10b05745e0f7668bd9f3e4cd546e4cca66964eb3557d78",
"02f49c7ab8d27e0e77c389403bb8568278ba17d14029da54397b6ce072cb5b785a",
"f31d01ca0ad79fb4aac134e8a329a066d62c9ed2d14605a318076315e42b6190",
"03329ab81c66fd71d97be7185e7ff071db20ede95507f731d27cb533fc1d9ae1c4");


Create table keyinfo(
user varchar(255),
privatekey longtext,
publickey longtext,
signkey longtext,
verifykey longtext
)

Create table balanceinfo(
user varchar(255),
balance int
)

Create table datainfo(
price int,
timestamp datetime,
datahash varchar(255),
category longtext,
name longtext,
buyer longtext,
owner longtext,
state int
)


Create table db(
encrypt longtext,
decrypt longtext,
cfrag longtext,
datahash varchar(255)
)
