# tiny-tool-collection
A collection of small pieces of code that otherwise would not need a full repo.

## Dummy cert generation

```
mkdir dummy
cd dummy
openssl ecparam -genkey -name secp384r1 -out secret.key
openssl req -new -x509 -sha256 -key secret.key -out cert.crt -days 3650
```
or
```
mkdir dummy
cd dummy
openssl req -new -x509 -nodes -newkey ec:<(openssl ecparam -name secp384r1) -keyout secret.key -out cert.crt -days 3650
```

## License

Licensed under the WTFPL license.
