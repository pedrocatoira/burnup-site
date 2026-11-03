---
title: Privacy policy · Burn-up for Jira
---

# Privacy policy

**Burn-up for Jira** · Effective November 2, 2026 · Draft, to be reviewed before publishing

This policy explains what Burn-up for Jira ("the app") reads, stores and shares when it is installed on an Atlassian Jira Cloud site. The app is published by Catoira Consulting Inc ("we").

## Summary

- The app runs entirely on Atlassian's Forge platform. It has no servers of its own and sends no data outside Atlassian.
- It only **reads** Jira data, as the person viewing the chart, and never changes it.
- It stores chart settings and a short list of issue ids in Atlassian-hosted Forge storage. A 15-minute cache of each viewer's chart is the only other data it keeps.
- No third parties, no analytics, no tracking, no advertising.

## What the app reads

To draw a chart for an Epic or a release, the app reads from your Jira site, with the permissions of the person viewing it:

- the Epic or release (key, summary or name) and its issues: ids, keys, created dates, status and status history, and the story points field when story points are used;
- for issues that used to belong to the Epic or release, the history of their parent or fix version, so removed issues can be shown up to the week they left;
- site settings needed to draw the chart: statuses, the site time zone, number fields (for the story points picker), issue types, and the viewer's admin permissions (to decide who can change settings).

The app requests only the `read:jira-work` scope for Jira data and has no write access to Jira.

## What the app stores, and for how long

Everything below is kept in Forge storage, which Atlassian hosts for the app on its own infrastructure.

| Data | Purpose | Kept |
| --- | --- | --- |
| Site settings and project overrides: story points field, issue types counted, how unestimated issues count | Configure the charts | Until the app is uninstalled |
| Chart inputs per Epic or release: metric, capacity per week, start date, deadline | Show the same chart to the next person who opens it | Until the app is uninstalled |
| Former members of an Epic: issue ids, the time each one left, and when the Epic was last checked | Show removed issues in past weeks (Jira can't search parent history) | Until the app is uninstalled |
| Chart cache: the computed chart (weekly totals, keys of issues completed each week, the Epic or release key and name), stored per viewer under their Atlassian account id | Open charts quickly | 15 minutes, then deleted |
| Background job records for large charts: status and progress, the requesting viewer's Atlassian account id, the Epic or release id; the job's input (issue ids and chart inputs) | Build large charts and show progress | Inputs deleted when the job ends; records deleted after 1 day |

Issue summaries, descriptions, comments, attachments and other issue content are not stored. The cache is per viewer because each chart is read with that viewer's permissions, so it is never shown to anyone else.

When the app is uninstalled, Atlassian deletes its Forge storage under Atlassian's data retention rules for Forge apps.

## Logs

Atlassian keeps operational logs for Forge apps that the publisher can read. The app's production logs contain only ids, counts, durations and error types (for example an HTTP status). They never contain issue content.

## Sharing

We do not sell, rent or share data with anyone. The app uses no third-party services, analytics, tracking, advertising or cookies of its own. Data is only processed by Atlassian, as the platform the app runs on, under [Atlassian's privacy policy](https://www.atlassian.com/legal/privacy-policy).

## Your choices

- Site and project admins control which issue types and fields the app uses, in the app's settings.
- Uninstalling the app stops all processing and leads to deletion of its storage, as described above.
- For questions or requests about data, contact [support@catoira.app](mailto:support@catoira.app).

## Changes

We will post changes to this policy on this page and update the effective date.
