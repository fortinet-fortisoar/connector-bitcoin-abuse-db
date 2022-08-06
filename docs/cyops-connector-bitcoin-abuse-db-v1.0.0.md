## About the connector
BitcoinAbuse.com is a public database of bitcoin addresses used by scammers, hackers, and criminals. This connector lets you tracking bitcoin addresses used by ransomware, blackmailers, fraudsters, etc.
<p>This document provides information about the Bitcoin Abuse DB Connector, which facilitates automated interactions, with a Bitcoin Abuse DB server using FortiSOAR&trade; playbooks. Add the Bitcoin Abuse DB Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Bitcoin Abuse DB.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-bitcoin-abuse-db`

## Prerequisites to configuring the connector
- You must have the URL of Bitcoin Abuse DB server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Bitcoin Abuse DB server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Bitcoin Abuse DB</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>URL of the bitcoin-abuse-db connector to access the connector website.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Lookup Abuse Types<br></td><td>Look up the abuse_type_id for use with the report address API.<br></td><td>lookup_abuse_type <br/>Investigation<br></td></tr>
<tr><td>Get Lookup Distinct Reports<br></td><td>This report is cached and only updates once per hour.<br></td><td>lookup_abuse_type <br/>Investigation<br></td></tr>
<tr><td>Check Address<br></td><td>Provide details of the given address. This report is cached and only updates once per hour.<br></td><td>check_given_address <br/>Investigation<br></td></tr>
<tr><td>Get Complete Download<br></td><td>Returns a CSV file containing all reports within the given time period. The "1d" file is updated daily in the early morning. The "30d" file is updated weekly on Sunday morning. The "forever" file is updated monthly on the 15th of the month. All updates occur between 2am-3am UTC.<br></td><td>get_all_reports <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Lookup Abuse Types
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "label": ""
</code><code><br>}</code>
### operation: Get Lookup Distinct Reports
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Token<br></td><td>Api token required for authentication.<br>
</td></tr><tr><td>Page<br></td><td>Provide only to get details of any particular page.<br>
</td></tr><tr><td>Reverse<br></td><td>Reverse the order of reports. So, oldest reports are first.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "current_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "data": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "first_page_url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "from": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "next_page_url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "path": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "prev_page_url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "to": ""
</code><code><br>}</code>
### operation: Check Address
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Token<br></td><td>Api token required for authentication.<br>
</td></tr><tr><td>Address<br></td><td>Provide the lookup address.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "address": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "first_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "last_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "recent": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "abuse_type_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "abuse_type_other": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_at": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>
### operation: Get Complete Download
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Token<br></td><td>Api token required for authentication.<br>
</td></tr><tr><td>Time Period<br></td><td>Allowed options are 1d, 30d, or forever.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

The output contains a non-dictionary value.
## Included playbooks
The `Sample - bitcoin-abuse-db - 1.0.0` playbook collection comes bundled with the Bitcoin Abuse DB connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Bitcoin Abuse DB connector.

- Get Lookup Abuse Types
- Get Lookup Distinct Reports
- Check Address
- Get Complete Download

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
