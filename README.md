# LARPVAULT

Static LARP Clips store — baby-blue (#7DD3FC) theme. Login `larp` / `123`.

## Local
```
python serve.py
# http://localhost:8787  (or PORT env)
# or
python -m http.server 8787
```

## Deploy to Render (GitHub → Web Service)
1. Push this folder to GitHub (root must contain `serve.py`, `render.yaml`, `index.html`)
2. Render → New → Web Service → Connect repo
3. Render auto-detects `render.yaml`:
   - **Environment:** Python
   - **Build Command:** *(empty)*
   - **Start Command:** `python serve.py`
   - **Health Check:** `/`
4. Deploy → `https://larpvault.onrender.com`

`serve.py` handles `PORT` env, mocks `/api/auth/session` (`larp`), `/api/safety-check`, `/api/market/stats` and strips `?_rsc=` so dashboard tabs don't 404.
`render.yaml` sets `type: web` `env: python` `plan: free`.
