# Ekommerce

Use this URL as base to requests:

> `http://127.0.0.1:8000/`

## Endpoints:

### POST api/orders/

- need authentication

> #### request body:
>
>```
> {    
>    "product_list": [1,2],
>    "total_price": 0,
> 	  "description": "test",
>    "status": "test",
>    "client_id": 1
> }
> ```
-  **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "id": 1,
>   "total_price": 25.50,
>   "status": "REALIZADO",
>   "description": "test",
>   "product_list": [
>     {
>       "name": "product 1",
>       "price": 15.25,
>       "description": "product 1 test",
>       "image": "product1.png",
>       "category": "category prod 1"
>     },
>     {
>       "name": "product 2",
>       "price": 10.25,
>       "description": "product 2 test",
>       "image": "product2.png",
>       "category": "category prod 2"
>     }
>   ],
>   "client_id": 1
> }
>```

### PATCH api/orders/

- need authentication

### Status pode receber os seguintes valores:
- ENVIADO - para pedido enviado
- ENTREGUE - para pedido entregue
- CANCELADO - para pedido cancelado
> #### request body:
>
>```
> {    
>     "status": "CANCELADO",
>     "id": 1
> }
> ```
-  **If everything goes right:** http status code: 200
> #### response body:
>
>```
> {
>   "id": 1,
>   "total_price": 25.50,
>   "status": "CANCELADO",
>   "description": "test",
>   "product_list": [
>     {
>       "name": "product 1",
>       "price": 15.25,
>       "description": "product 1 test",
>       "image": "product1.png",
>       "category": "category prod 1"
>     },
>     {
>       "name": "product 2",
>       "price": 10.25,
>       "description": "product 2 test",
>       "image": "product2.png",
>       "category": "category prod 2"
>     }
>   ],
>   "client_id": 1
> }
>```
