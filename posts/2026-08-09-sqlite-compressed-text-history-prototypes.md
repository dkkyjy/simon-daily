# SQLite compressed text-history prototypes

        **Date:** 2026-08-09 22:05 UTC
        **Link:** https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype/#atom-everything
        **Tags:** compression, sqlite, speech-to-text

        ---

        Research: SQLite compressed text-history prototypes I'm perennially interested in options for storing revision histories in relational databases. While out on a dog walk I had a new idea: how about taking the full text of every prior version in a big JSON array of strings and then applying zlib or zstd compression to the whole thing? Surely that would compress really well due to all of the repeated strings. The new GPT‑Live voice mode in the ChatGPT iPhone app has got really good, so I discussed the prototype with that. You still can't share URLs to voice conversations, but here's what I said copied from the transcript as a proper stream of consciousness: I have an interesting idea for a scheme for saving all previous versions of a piece of text that's constantly edited in a SQLite database um column in as efficient a way as possible. Okay, so I built these kinds of systems in the past, and it's always difficult to come up with a efficient way to do this. Like the easiest way is you have a row for every previous copy of the previous previous value of the string. But if it's a long document Like20 kilobytes of data, that means that every single edit adds another 20 kilobytes of data to the database, right. So, what I've now thinking, is um compression would work really well, right? If you Bundle all of those different um Every every version of this document all the way back to the start if you were to apply a good compression algorithm to them that should basically wipe out huge amounts of the redund- the um redundant text, right Um, so what I'd thinking is how about really, really simple mechanism There is a history column on the single on

*(truncated, see original)*
