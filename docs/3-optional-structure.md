# Optional structure overview

What's included in `.template`:

```
TODO tree
```

I find some of these folders situationally useful:

+ `conf/`
+ `docs/`
+ `tests/`
+ `references/`

## Configuration

If a lot of configuration is required e.g. training deep learning models, suggest to open a new `conf/` folder and store configuration files there.

## Tests

Tests are recommended for individual pieces of logic if possible. See recipes for more info.

## References

Put files here that are not directly involved in development, but are somewhat related. e.g. old handover code, supporting info from Powerpoints od Docx files, PDFs etc

## Docs

Dump any project documentation into `docs/`. Typically dump stuff that is VCS friendly here, like MD files. 

At the moment, a `docs/` folder is not provisioned. Small projects have info contained in README and notebooks. Up to user to implement if scope calls for it. Corporate environments usually have separate documentation in MS Word or MS Powerpoint. Established places might have a team wiki, project wiki etc. Bottomline, create the docs folder if you need to. 

Can do it as an information dump:

```
TODO tree of informal info dump
```

If time permits, can set things up with neat documentation. See Documentation section in recipes

