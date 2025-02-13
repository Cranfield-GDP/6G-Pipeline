Policy Configuration Files for Policy Control Function
---

The policy configuration files are stored as yaml files including pcc rules, policy decisions and traffic rules.

### Traffic Rules

The traffic rules defines the valid traffic flow path with a list of DNAIs (Data Network Access Identifier), e.g., 

```yaml
edge-scenario:
  routeToLocs:
  - dnai: access 
  - dnai: ulcl
  - dnai: aupf2
  - dnai: edge

internet-scenario:
  routeToLocs:
    - dnai: access
    - dnai: ulcl
    - dnai: aupf1
    - dnai: internet
```

### PCC Rules

PCC is a mechanism used to:
- Enforce policies: Control the quality of service (QoS), traffic prioritization, and access to network resources.
- Manage charging: Apply charging rules based on usage, service type, or other criteria.

```yaml
internet-rule:
  flowInfos:
    - flowDescription: permit out ip from any to assigned
  precedence: 10
  refTcData:
    - internet-scenario

edge-rule:
  flowInfos:
    - flowDescription: permit out ip from any to assigned
  precedence: 9
  refTcData:
    - edge-scenario
```

### Policy Decisions

The policy decision files defines which policy to choose for a given context, the context can be a specific network slice, a specific UE, or a specific dnn, etc., e.g., 

```yaml
decision_supi1:
  pcc_rules:
  - internet-rule
  supi_imsi: '208950000000031'
decision_supi2:
  pcc_rules:
  - internet-rule
  - edge-rule
  supi_imsi: '208950000000032'
```

with the above policy decision, UE1 (...00031) only has access to the `internet` data network while UE2 (...00032) will have access to both `internet` and `edge`.

### Speciail notes on the policy rules
If the policy is defined as below, then the second policy about the edge will be ignored by the PCF and the `31` UE will only be able to access the internet but not the edge server.

```yaml
decision_supi1:
  pcc_rules:
  - internet-rule-qos-constrained
  supi_imsi: '208950000000031'
decision_supi1a:
  pcc_rules:
  - edge-rule-qos-unlimited
  supi_imsi: '208950000000031'
```