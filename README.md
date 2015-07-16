A pretty-printer for files containing more than one json object. 

Consider the following file:

```json
{"abc": "def"}{"ham": "spam", "numbers": [1, 2, 3]}{"foo": "bar"}
```

The contents of this file do not constitute a valid json object when taken as a whole. Instead, the file contains a _stream_ of json objects. Jsoncat will pretty-print this file as so:

```json
{
	"abc": "def"
}
{
	"ham": "spam",
	"numbers": [
		1,
		2,
		3
	]
}
{
	"foo": "bar"
}
```

## Installation

```bash
pip install jsoncat
```

## Usage

Read from a file:

```bash
jsoncat myfile.json
```

Read from stdin:

```bash
cat myfile.json | jsoncat
```

Read a gzipped json stream:

```bash
cat myfile.json.gz | zcat | jsoncat
```
