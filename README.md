[![Lint](https://github.com/aidanmelen/no-deploy-on-friday-action/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/aidanmelen/no-deploy-on-friday-action/actions/workflows/lint.yml)
[![Tests](https://github.com/aidanmelen/no-deploy-on-friday-action/actions/workflows/tests.yml/badge.svg)](https://github.com/aidanmelen/no-deploy-on-friday-action/actions/workflows/tests.yml)
[![End2End](https://github.com/aidanmelen/no-deploy-on-friday-action/actions/workflows/e2e.yml/badge.svg)](https://github.com/aidanmelen/no-deploy-on-friday-action/actions/workflows/e2e.yml)

# No Deploy on Friday action

This action aims to codify the unwritten rules like "No Deployments on Friday". This is achieved by simply terminating the action with a non-zero exit code when the date conditions are met; which in turn, causes the remaining steps in the workflow to cancel. At last, your weekend is safe once again.

## Inputs

## `NO_DEPLOYMENT_DAYS`

**Optional** A comma delimited list of weekdays that we do not deploy on. Defaults to `Friday, Saturday, Sunday`.

## `TZ`

**Optional** The timezone name. See Wikipedia for the complete list of timezone names: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. Defaults to `UTC`.

## `COUNTRY`

**Optional** The country of origin. This determines which the national holiday calendar to use. Defaults to `US`


## `HOLIDAYS`

**Optional** Whether to prevent deployments on national holidays. This is applied in addition to the `NO_DEPLOYMENT_DAYS` input. Defaults to `true`

## Outputs

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
- name: Reason For Previous Step
  if: always()
  run: echo "${{ steps.no-deployment-on-friday.outputs.reason }}"
- name: Mock Deployment
  run: echo "Deploy something here..."
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
- name: Reason For Previous Step
  if: always()
  run: echo "${{ steps.no-deployment-on-friday.outputs.reason }}"
- name: Mock Deployment
  run: echo "Deploy something here..."
```
