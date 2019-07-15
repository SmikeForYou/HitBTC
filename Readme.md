### Requirements
```bash
python3 --version
# Python 3.6.7
```
### Local development
1.Clone repo and get into it:
```bash
git clone https://github.com/SmikeForYou/HitBTC.git && cd HitBTC
```
2.Update .env with API_KEY and API Secret <br />
3.Create local virtual environment and install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```
4.Run app with
```bash
(venv) FLASK_APP=server.py flask run
```

## Features
If you want to update fetcher with another endpoints, you need too add normalization dict to this [file](endpoint_normalization_config.py) folowing the next rules:
<br />
{
"method": "GET"(only get is supported), <br /> 
"uri": "/your/endpoint", <br /> 
"normalization_rules": { <br /> 
    "output_field_1": "input_field_you_want_to_get_from_url_response" <br /> 
    "output_field_2": { <br /> 
        "default": "Fill if you want to return some hardcoded value" <br /> 
    }<br /> 
}<br /> 
}

