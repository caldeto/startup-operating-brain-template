# FAQ

## Is this an app?

No. It is a versioned Obsidian vault template plus GitHub workflows and local validators.

## Should agents read the whole vault?

No. Agents should follow `AGENT_START_HERE`, global rules, and the relevant context pack.

## Can I use a different cloud provider?

Yes. Use `{{CLOUD_PROVIDER}}` or bootstrap with your provider name.

## Are examples part of my vault?

No. They are references. Bootstrap copies from `template/`, not from `examples/`.

## Are GitHub Actions required?

No. They are optional. Local gates are the source of verification.
