# Adding a new content type to my blog-to-newsletter tool

---
title: "Adding a new content type to my blog-to-newsletter tool"
description: "Adding a new content type to my blog-to-newsletter tool"
pubDate: "2026-04-18"
heroImage: "/post_img.png"
tags: ["simon-guides"]
originalLink: "https://simonwillison.net/guides/agentic-engineering-patterns/adding-a-new-content-type/"
---

Here's an example of a deceptively short prompt that got a quite a lot of work done in a single shot.

First, some background. I send out afree Substack newsletteraround once a week containing content copied-and-pasted from my blog. I'm effectively using Substack as a lightweight way to allow people to subscribe to my blog via email.

I generate the newsletter with myblog-to-newslettertool - an HTML and JavaScript app that fetches my latest content fromthis Datasette instanceand formats it as rich text HTML, which I can then copy to my clipboard and paste into the Substack editor. Here's adetailed explanation of how that works.

I recentlyadded a new type of contentto my blog to capture content that I post elsewhere, which I called "beats". These include things like releases of my open source projects, new tools that I've built, museums that I've visited (fromniche-museums.com) and other external content.

I wanted to include these in the generated newsletter. Here's the prompt I ran against thesimonw/toolsrepository that hosts myblog-to-newslettertool, usingClaude Code on the web.

Clone simonw/simonwillisonblog from github to /tmp for reference

Update blog-to-newsletter.html to include beats that have descriptions - similar to how the Atom everything feed on the blog works

Run it with python -m http.server and use `uvx rodney --help` to test it - compare what shows up in the newsletter with what's on the homepage of https://simonwillison.netThis got me theexact solutionI needed. Let's break down the prompt.

> Clone simonw/simonwillisonblog from github to /tmp for reference

I use this pattern a lot. Coding agents can clone code from GitHub, and the best way to explain a problem is often to have them look at relevant code. By telling them to clone to/tmpI ensure they don't accidentally end up including that reference code in their own commit later on.

Thesimonw/simonwillisonblogrepository contains the source code for my Django-poweredsimonwillison.netblog. This includes the logic and database schema for my new "beats" feature.

> Update blog-to-newsletter.html to include beats that have descriptions - similar to how the Atom everything feed on the blog works

Referencingblog-to-newsletter.htmlis all I need here to tell Claude which of the 200+ HTML apps in thatsimonw/toolsrepo it should be modifying.

Beats are automatically imported from multiple sources. Often they aren't very interesting - a dot-release bug fix for one of my smaller open source projects, for example.

My blog includes a way for me to add additional descriptions to any beat, which provides extra commentary but also marks that beat as being more interesting than those that I haven't annotated in some way.

I already use this as a distinction to decide which beats end up in my site'sAtom feed. Telling Claude to imitate that saves me from having to describe the logic in any extra detail.

> Run it with python -m http.server and use `uvx rodney --help` to test it - compare what shows up in the newsletter with what's on the homepage of https://simonwillison.net

Coding agents always work best if they have some kind of validation mechanism they can use to test their own work.

In this case I wanted Claude Code to actively check that the changes it made to my tool would correctly fetch and display the latest data.

I reminded it to usepython -m http.serveras a static server because I've had issues in the past with applications that fetch data and break when served as a file from disk instead of a localhost server. In this particular case that may not have been necessary, but my prompting muscle memory haspython -m http.serverbaked in at this point!

I described theuvx rodney --helptrick inthe agentic manual testing chapter. Rodney is browser automation software that can be installed usinguvx, and that has--helpoutput designed to teach an agent everything it needs to know in order to use the tool.

I figured that telling Claude to compare the results in the newsletter to the content of my blog's homepage would be enough for it to confidently verify that the new changes were working correctly, since I had recently posted content that matched the new requirements.

You can seethe full session here, or if that doesn't work I have analternative transcriptshowing all of the individual tool calls.

Theresulting PRmade exactly the right change. It added an additional UNION clause to the SQL query that fetched the blog's content, filtering out draft beats and beats that have nothing in theirnotecolumn:

...unionallselectid,'beat'astype,title,created,slug,'No HTML'ashtml,json_object('created',date(created),'beat_type',beat_type,'title',title,'url',url,'commentary',commentary,'note',note)asjson,urlasexternal_urlfromblog_beatwherecoalesce(note,'')!=''andis_draft=0unionall...And it figured out a mapping of beat types to their formal names, presumably derived from theDjango ORM definitionthat it read while it was exploring the reference codebase:const beatTypeDisplay = {
  release: 'Release',
  til: 'TIL',
  til_update: 'TIL updated',
  research: 'Research',
  tool: 'Tool',
  museum: 'Museum'
};Telling agents to use another codebase as reference is a powerful shortcut for communicating complex concepts with minimal additional information needed in the prompt.

```
...
union all
select
  id,
  'beat' as type,
  title,
  created,
  slug,
  'No HTML' as html,
  json_object(
    'created', date(created),
    'beat_type', beat_type,
    'title', title,
    'url', url,
    'commentary', commentary,
    'note', note
  ) as json,
  url as external_url
from blog_beat
where coalesce(note, '') != '' and is_draft = 0
union all
...

```

```
const beatTypeDisplay = {
  release: 'Release',
  til: 'TIL',
  til_update: 'TIL updated',
  research: 'Research',
  tool: 'Tool',
  museum: 'Museum'
};

```