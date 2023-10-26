# Book Recommendation System
This repository is about a book recommendation system and has transferred to a web service that was written by python. 
this project contains two part. The fris, is model and implimentation for predict books. The second, is a web service for geting output of the moedle as API. (codes about creating model not included)     

## About the mode
In Overall, the aproach of creating model is collaborating filtering and the output files of the model are `PivotTable.csv` and `Re-Array.npy`. 

## API Documentation


### Recomend New Book
This API gets a book name as the user's preferred book and returns a similar book that could be interesting to the user.

#### Request
```http
Curl http://127.0.0.1:8000/recomend/?book=1984
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `book` | `string` | **Required**. Book Name |

#### Response

```javascript
{
  "status": 200,
  "result":
  {
    "Book": "1984",
    "response": [
    "Animal Farm",
    "The Handmaid's Tale",
    "Brave New World",
    "The Vampire Lestat (Vampire Chronicles, Book II)",
    "The Hours : A Novel"
    ]
    }
}
```

### Receive sent requests
This API returns the result of all requests that sent by the user.

#### Request
```http
Curl http://127.0.0.1:8000
```

#### Response

```javascript
{
  "status": 200,
  "result":
  {
    "Book": "1984",
    "response": [
    "Animal Farm",
    "The Handmaid's Tale",
    "Brave New World",
    "The Vampire Lestat (Vampire Chronicles, Book II)",
    "The Hours : A Novel"
    ]
    }
}
```

## Status Codes

Thi web-service returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |
