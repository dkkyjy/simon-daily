# smolmachines / smolvm as a sandbox for untrusted Python & JavaScript

        **Date:** 2026-08-19 23:16 UTC
        **Link:** https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
        **Tags:** research, sandboxing, ai, github-actions, generative-ai, llms, claude-mythos-fable

        ---

        > *Feed summary: Research: smolmachines / smolvm as a sandbox for untrusted Python & JavaScript
        I tasked Claude Fable 5 running in Claude Code for web with the following research task:

Put https://smolmachine*

19th August 2026

[Research](/elsewhere/research/)
[smolmachines / smolvm as a sandbox for untrusted Python & JavaScript](https://github.com/simonw/research/tree/main/smolmachines-untrusted-sandbox#readme)
— Testing smolvm 1.8.3 shows it is well suited for sandboxing untrusted Python and JavaScript data transformations using hardware-isolated VMs rather than shared-kernel containers. Offline local images, no-network execution, CPU/RAM limits, guest-enforced timeouts, storage quotas, read-only input mounts, writable output mounts, and `--unprivileged` all worked as intended, with cold starts around 0.6–1.5 seconds and warm executions around 50 ms.

I tasked Claude Fable 5 running in Claude Code for web with the following research task:

> `Put https://smolmachines.com through its paces as a fast secure sandbox. Explore what it would take to use this to run untrusted Python and JavaScript code in a way that is limited in what RAM and CPU time it can take up (protection against "while true") with no network access and filesystem access only to designated files`
>
> `Goal is to be able to use this to execute user-provided tasks for things like data transformations`

It quickly ran into a problem: the Claude Code for web environment can't run [smol machines](https://smolmachines.com). Quoting the [notes it wrote](https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/smolmachines-untrusted-sandbox/notes.md#environment-check):

> * This Claude Code container: Linux 6.18.5-fc-v20 (itself a Firecracker guest), 4 vCPU, 15GB RAM. **No /dev/kvm, no vmx/svm CPU flags** → no nested virt.
> * `smolvm machine run` fails as expected: "kvm not available".
> * Plan B: GitHub Actions ubuntu runners DO expose /dev/kvm → run the real test battery via a temporary workflow on this branch, collect logs, remove workflow in final commit.

And Plan B is [what it did](https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/.github/workflows/smolvm-sandbox-test.yml), installing smolvm and running [these tests](https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/smolmachines-untrusted-sandbox/run-tests.sh) directly in a GitHub Actions runner against that branch.

That was a creative solution to the environmental limits posed by Claude Code for web. Another example of Fable being [relentlessly proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/).

Posted [19th August 2026](/2026/Aug/19/) at 11:16 pm
