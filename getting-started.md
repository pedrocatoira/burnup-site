---
title: Getting started · Burn-up for Jira
---

# Getting started with Burn-up for Jira

Burn-up for Jira draws a burn-up chart for any Epic or release: **scope** (red), **done** (green), a **forecast** at your planned weekly capacity (blue dashed) with a predicted end date, and an **ideal line** to your deadline (grey long-dashed). It works for Scrum and Kanban, because capacity is always per week.

## 1. Install

Install the app from the Atlassian Marketplace on your Jira Cloud site. It is free for up to 10 users and has a 30-day trial above that.

The app only reads Jira data, with the viewer's permissions, and never changes anything.

## 2. Set up story points (optional)

Throughput charts (issue counts) work straight away. For story point charts, a Jira admin picks the field once:

1. Go to **Jira settings → Apps → Burn-up**.
2. **Story points field**: choose your field. The app suggests "Story Points" or "Story point estimate" when it finds them.
3. **Issue types counted**: by default all standard types; sub-tasks are excluded so work isn't counted twice.
4. **Unestimated issues**: count them as 0 (default) or use a default estimate. Charts always show how many are unestimated.

Project admins can override the field and issue types for one project in **Project settings → Apps → Burn-up**.

## 3. Chart an Epic

1. Open an Epic and open the **Burn-up** panel on the issue view.
2. Fill in:
   - **Based on**: Throughput or Story points.
   - **Capacity per week**: how much the team plans to finish each week (decimals allowed). After the first chart, hints show the **observed** average of the last 6 weeks and, with a deadline, the capacity **to hit the deadline**. Click **Use** to copy one in.
   - **Start date** and **Deadline** (optional).
3. Click **Create Burn-up**.

The inputs are saved for the Epic, so the next person who opens it sees the same chart. Change any input and click **Update Burn-up** to redraw.

## 4. Chart a release

Open the project and choose **Burn-up** in the project sidebar, then pick a release. The rest works as for Epics.

## 5. Read the chart

- **Scope** counts every issue from the day it was created, even if it joined the Epic later. Issues moved out of the Epic or release count until the week they left. Won't Do and Duplicate count as done.
- **Done** is the state at the end of each week (Sunday 23:59, site time zone), so reopened issues drop out and come back when done again.
- **Forecast** starts today (or at a future start date) and climbs by your capacity each week until it reaches today's scope. It assumes scope stays flat.
- The **info box** compares planned, observed and to-hit-deadline capacity, and shows whether you are **on track** or **late by N weeks**.
- Hover a done point to see which issues were completed that week.

## 6. Share it

Use the **copy** icon at the top right of the chart to copy it as an image (always on a light background), or **Download PNG**.

## Good to know

- **Fresh data**: charts are cached for 15 minutes for each viewer. Click **Refresh data** to read Jira again now.
- **Large Epics and releases**: above 2,000 issues the chart is built in the background, with a progress bar. You can close the page; the chart is ready when you come back. The limit is 20,000 issues.
- **Removed issues**: the first time an Epic is charted, the app checks the project for issues that used to belong to it. The chart shows straight away and updates when the check finishes.
- **Permissions**: everyone sees the chart with their own Jira permissions, so people who can't see some issues get a chart without them.

## Troubleshooting

| You see | What to do |
| --- | --- |
| "Burn-up needs an active license" | A Jira admin can subscribe or renew in **Manage apps** (the message links there for admins). |
| Story points is greyed out | No story points field is set: see step 2. |
| "No issues in this Epic yet" | Add child issues of the counted types, then open the panel again. |
| A message about too many issues | The Epic or release has more than 20,000 issues of the counted types. Narrow the issue types in settings. |

Questions: [support@catoira.app](mailto:support@catoira.app) · [Privacy policy](privacy-policy.md)
