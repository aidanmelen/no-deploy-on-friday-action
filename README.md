# No Deploy on Friday action

This action aims to codify the unspoken rule of "No Deployments on Friday". This is achieved by simply terminating the action with a non-zero exit code when the date conditions are met; which in turn, causes the remaining steps in the workflow to cancel. At last, your weekend is safe once again.

## Inputs

## `NO_DEPLOYMENT_DAYS`

**Optional** A comma delimited list of weekdays that will prevent deployments. Defaults to `"Friday, Saturday, Sunday"`.

## `TZ`

**Optional** The timezone name. Defaults to `UTC`. See Wikipedia for the complete list of timezone names: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones.

## `COUNTRY`

**Optional** The country of origin. This determines which the holiday calendar to use.


## `HOLIDAYS`

**Optional** Whether to prevent deployments on holidays. This is applied in addition to the "`NO_DEPLOYMENT_DAYS`" input.

## Outputs

## `deployment`

'true' if the deployment was canceled and otherwise 'false'.

## `reason`

The reason for the outcome.

## Example usage

Simple example.

```yaml
- name: Checkout
  uses: actions/checkout@v2
- name: No Deployments on Friday
  uses: ./
  id: no-deployment-on-friday
```

Complete example.

```yaml
- name: Checkout
  uses: actions/checkout@v2
- name: No Deployments on Friday
  uses: ./
  id: no-deployment-on-friday
  env:
    NO_DEPLOYMENT_DAYS: 'Friday, Saturday, Sunday'
    TZ: 'MST'
    COUNTRY: 'US'
    HOLIDAYS: true
```
