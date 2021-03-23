# 💾  Fake Data Generator Database API

<quote>
	This is a custom fake data generator, which is completely free to use, and the data inside is going to be even expanded  to create tens of thousands of new account options.
</quote>

### Used Technologies:
```
FastAPI
.csv Management
```

### Deployed:


### Usage:
- GET male name:
	- `"/{token}/malename"`
- GET female name:
	- `"/{token}/femalename"`
- GET surname:
	- `"/{token}/surname"`
- GET male full name (name & surname)
	- `"/{token}/male/fullname"`
- GET female full name (name & surname)
	- `"/{token}/female/fullname"`
- GET randomly generated age
	- `"/{token}/age"`
- GET complete male account (name & surname & age)
	- `"/{token}/male/account"`
- GET complete woman account (name & surname & age)
	- `"/{token}/female/account"`

Wrong Token AUTH Try:
- `"Wrong API Token."`

### License:
MIT
