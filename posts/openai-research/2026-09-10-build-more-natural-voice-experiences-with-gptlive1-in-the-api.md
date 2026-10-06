# Build more natural voice experiences with GPT‑Live‑1 in the API

**Date:** 2026-09-10 00:00 UTC
**Link:** https://openai.com/zh-Hans-CN/index/introducing-gpt-live-1-in-the-api/

---

GPT‑Live‑1 brings natural, full-duplex voice conversations to the API, with stronger instruction following, custom voices, and telephony support."

GPT‑Live‑1 brings ChatGPT’s natural, full-duplex conversations to the API, with more control over how voice agents speak and act."

Current poster for Vimeo Yelp Testimonial 1225436485."

We’re launching GPT‑Live‑1 in the API, giving developers a powerful, natural voice model for building voice-enabled apps and business workflows.

For the API release of GPT‑Live‑1, we’ve focused on new capabilities that let developers steer and customize voice experiences around their users, workflows, and goals.

A core GPT‑Live‑1 strength, smooth interruption handling, is already delivering business impact: in early evaluations, Speak found that GPT‑Live‑1 gave learners more time to think before the language tutor responded, cutting interruptions by almost 80% versus previous turn-based systems."

Improves interruption handling via a single model that reasons over incoming and outgoing audio together, avoiding the latency and brittle handoffs of chained STT–LLM–TTS architectures."

GPT‑Live‑1 can delegate reasoning and tool calls to a backend text model like GPT‑6 Astra or a third-party model."

Lets developers shape an agent’s tone, pace, and conversational style through the system prompt."

Better handles background noise and silence without interrupting the conversation or narrating every step out loud."

Improves context retention and conversational quality across extended interactions."

Enables deployment of full-duplex voice agents for phone calls, from restaurant reservations to customer support."

Source image from the GPT-Live-1 API blog draft. Unpublished staging asset."

Yelp Host seamlessly secures a reservation with GPT-Live-1 handling background noise, side conversations, and interruptions."

Traditional voice agents stitch together speech-to-text, a reasoning model, and text-to-speech.

Each handoff adds latency and creates more opportunities to lose timing, context, or the natural rhythm of a conversation.

GPT‑Live‑1 handles listening and speaking in a single model, simplifying the voice layer.

This lets the conversation continue while work happens in the background."

Compared to our cascaded build, GPT-Live-1 simplified our code base by 80% and removed 23K lines of code.

This enabled natural, real-time patient conversations & freed our team to improve the experience from booking an appointment to navigating care."

Logo artwork from approved Figma frame 1:289. Transparent SVG canvas adapts optical sizing to the existing card container."

Developers choose the models, tools, and agent harness behind the conversation.

For example, they might pair GPT‑Live‑1 with a model like Luna for high-volume tasks like scheduling or order updates, and use a model like Astra for complex customer issues that require reasoning.

That flexibility lets developers match reasoning depth, speed, and cost to each task."

GPT‑Live‑1 natively provides ASR transcripts and response text.

It also offers strong alphanumeric understanding and supports keyword biasing.

Although GPT‑Live‑1 is not a turn-based model, it natively supports turn detection, so developers can continue to build around explicit turn boundaries."

Across our evaluations, GPT‑Live‑1 improves Full Duplex Bench performance by 30 percentage points over GPT‑Realtime‑2.

Paired with GPT‑6 Astra at medium reasoning effort, it also ranks #1 on Tau3, which measures frontier voice-agent intelligence on end-to-end tasks."

Evaluates spoken customer-service tasks in airline, retail, and telecom domains.

Pass@1 measures task success; the headline gives each domain equal weight."

Adding GPT-Live-1 into Yelp Host and Hatch improved turn-taking and accuracy over our traditional voice architecture.

When Yelp Host uses GPT-Live-1 to answer calls, like reservations and food orders, we're seeing meaningful improvements in call handling rates.

Callers are also speaking fuller, more natural sentences, which tells us the experience on the other end of the phone feels genuinely different."

Logo artwork from approved Figma frame 1:289. Transparent SVG canvas adapts optical sizing to the existing selector container."

A good language tutor knows when to give learners space and when to step in, and GPT-Live-1 brings that naturalness to Speak’s Live Tutor Lessons—in our early evaluations, it cut interruptions during thinking pauses by almost 80% compared with previous turn-based systems."

GPT‑Live-1 shows what a full-duplex model can unlock: It moves AI voice support from the stop-start rhythm toward the natural flow of a phone call.

Customers can pause, interrupt, and change direction naturally; voice delivery is a clear step forward; and Fin can combine that natural conversation with its proprietary support system to do the deeper work needed to resolve the issue.

For us, this is the clearest signal yet of where voice support is heading."

With Devin and GPT-Live-1, working with an AI engineer starts to feel more like collaborating with a teammate.

You can talk through an idea, pressure-test an approach, or just hand off work while you’re away from your keyboard."

Developers need voices that fit their product and sound natural to the people using it.

With GPT‑Live‑1, we’re expanding from a small set of real-time voices to a broader selection across accents, dialects, and languages giving developers more choice in how their assistants sound."

Quartz voice sample from the approved 2026-09-10 recording package."

Devin Live works with you in real time to build, test, and ship software in the cloud."

Picsart creative workspace demo video for GPT-Live-1."

Source image from the GPT-Live-1 API blog draft; final media subject to review."

Powered by OpenAI’s GPT-Live-1, Picsart’s creative AI Agents let creators brainstorm, generate, refine, and publish content through real-time voice conversation."

HeyGen language learning video's existing Vimeo thumbnail."

A scenario-based language tutor built by HeyGen LiveAvatar showcasing GPT-Live-1's custom voice, interruption handling and function calls."

OpenAI Presence's voice agent guides a customer support call in real time, using GPT‑Live‑1 to maintain natural conversation while resolving the issue."

Evaluates spoken banking support with knowledge retrieval and account tools.

Pass@1 is the fraction of 97 banking_knowledge tasks completed successfully."

Evaluates pause handling, conversational turn taking, interruptions, and backchannels."

Tests reactions to background speech, speech to another person, listener backchannels, and interruptions."

Measures how quickly the agent starts its reply after the user finishes a turn."

Tests tool use from spoken requests containing natural pauses, hesitations, and self-corrections.

Evaluates the spoken answer to tool-using requests containing pauses, hesitations, and self-corrections.

Scores how well the answer matches the reference intent."

Ripple voice sample from the approved 2026-09-10 recording package."

Vesper voice sample from the approved 2026-09-10 recording package."

Willow voice sample from the approved 2026-09-10 recording package."

Stone voice sample from the approved 2026-09-10 recording package."

Gleam voice sample from the approved 2026-09-10 recording package."

Meridian voice sample from the approved 2026-09-10 recording package."

Bossa voice sample from the approved 2026-09-10 recording package."

Tempo voice sample from the approved 2026-09-10 recording package."

Beacon voice sample from the approved 2026-09-10 recording package."

Delta voice sample from the approved 2026-09-10 recording package."

Cinder voice sample from the approved 2026-09-10 recording package."

We’ll continue to expand voice options and language availability over the coming months."

Pair it with the backend model and agent harness that fit your product, then build a voice experience that can scale with the work it needs to do."

Connecting GPT-Live-1 to Codex. This excerpt shows how an application passes conversation context to Codex and returns its answer to GPT-Live-1.

Connection setup and delegation handling are omitted."

Presence helps enterprises deploy trusted AI agents that can answer questions, resolve issues, use company systems, take approved actions, and escalate to people when needed.

Reach out to your OpenAI account director to learn more."

Clean 1080 x 1080 cover image generated from the approved Dotcom wallpaper bank.

Square crop of the supplied OAI_Finances_4_16x9 texture for the ChatGPT for Financial Services listing art card."
