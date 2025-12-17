# FastAPI sample app

tl;dr:
- `GET /` -> hello, world;
- `GET /berry` -> random berry of the day;
- `GET /calc?x=100` -> return x + super secret number.

## Running

To locally run the app, create a venv and install dependencies via:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then start the server at port 8123 (for example) with:
```bash
uvicorn src.main:app --reload --port 8123
```

Or use docker:
```bash
docker build -t fastapi-sample .
docker run -p 8123:8123 -d fastapi-sample
```

The app will be available at `http://localhost:8123`.

## Testing

Unit-test are located in src/test. Run
```bash
pytest src/test
```
for testing.


## CI/CD

The project is build, tested and automatically deployed whenever new code is pushed to the *main* branch.  
Find the (possibly) live version of the project hosted at [foo.requef.com](https://foo.requef.com).
