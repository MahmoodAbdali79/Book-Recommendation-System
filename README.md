# Book Recommendation System
This repository is about a book recommendation system and has transferred to a web service that was written by python. 
this project contains two part. The fris, is model and implimentation for predict books. The second, is a web service for geting output of the moedle as API. (codes about creating model not included)     

## About the mode
In Overall, the aproach of creating model is collaborating filtering and the output files of the model are `PivotTable.csv` and `Re-Array.npy`. 

## API Documentation


## Recomend New Book

### Request
```http
GET /api/campaigns/?api_key=12345678901234567890123456789012
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `book` | `string` | **Required**. Book Name |

### Response

```javascript
{
  "message" : string,
  "success" : bool,
  "data"    : string
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
