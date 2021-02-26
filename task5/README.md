# To run Flask app:
```
python app.py
```
# Request for prediction:
```
curl http://0.0.0.0:5555/predict -H 'Content-Type: application/json' -d '{
    "features": [[5.0, 4.2, 1.5, 0.3], [5, 6, 7, 8]]
}'
```
