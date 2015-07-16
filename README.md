A pretty-printer for files containing more than one json object.

For example, consider the following file:

```json
{"abc": "def"}{"ham": "spam"}{"foo": "bar"}
```

The contents of this file do not constitute a valid json object in their entirety. Instead, the file contains a _stream_ of json objects. Jsoncat will pretty-print this file as so:

```json
{
	"abc": "def"
}
{
	"ham": "spam"
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

```bash
jsoncat myfile.json
```

For gzipped json streams:

```bash
cat myfile.json.gz | zcat | jsoncat
```
