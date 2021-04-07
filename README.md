# Ekommerce

Use this URL as base to requests:

> `https://ekommerce.herokuapp.com/

## Endpoints:

### POST api/signup/

- it doesn't needs authentication
- What differences admin to salesman to client is:
  - admin:
    - is_superuser: True
    - is_staff: True
  - salesman:
    - is_superuser: False
    - is_staff: True
  - admin:
    - is_superuser: False
    - is_staff: False

> #### request body:
>
> ```
> {
>    "username": "admin",
>    "password": "admin@123",
>    "is_superuser": True,
>    "is_staff": False,
> }
> ```

- **If everything goes right:**
  - http status code: 201
    > #### response body:
    >
    > ```
    > {
    >    "id": 1,
    >    "username": "admin",
    >    "is_superuser": True,
    >    "is_staff": False,
    > }
    > ```

### POST api/login/

- it doesn't needs authentication (purpose is exactly authenticate)

> #### request body:
>
> ```
> {
>    "username": "admin",
>    "password": "admin@123",
> }
> ```

- **If everything goes right:**
  - http status code: 200
    > #### response body:
    >
    > ```
    > {
    >    "token": "f9f96aaeb7cc86fe19f34074ae302c0a42be4592"
    > }
    > ```

### POST api/orders/

- need authentication

> #### request body:
>
> ```
> {
>    "product_list": [1,2],
>    "total_price": 0,
> 	  "description": "test",
>    "status": "test",
>    "client_id": 1
> }
> ```

- **If everything goes right:** http status code: 201
  > #### response body:
  >
  > ```
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
  > ```

### PATCH api/orders/

- need authentication

### Status can receive the following values:

- ENVIADO - for order sent
- ENTREGUE - for order delivered
- CANCELADO - for canceled order
> #### request body:
>
> ```
> {
>     "status": "CANCELADO",
>     "id": 1
> }
> ```

- **If everything goes right:** http status code: 200
> #### response body:
>
> ```
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
> ```

### GET api/inventories/

- don't need authentication

-**If everything goes right:** http status code: 201

> #### response body:
>
> ```
> [
>   {
>     "id": 1,
>     "available": true,
>     "total_amount": 27,
>     "product_data": {
>       "id": 1,
>       "name": "refrigerante Coca Cola",
>       "category": "refrigerante",
>       "image": "image.jpg",
>       "price": 4.5,
>       "description": "refrigerante Coca Cola garrafa 2 litros"
>     }
>   },
>   {
>     "id": 2,
>     "available": false,
>     "total_amount": 0,
>     "product_data": {
>       "id": 2,
>       "name": "Chocolate Laka",
>       "category": "doces",
>       "image": "image.jpg",
>       "price": 6.5,
>       "description": "Chocolate Laka branco"
>     }
>   }
> ]
> ```

### GET api/inventories/<int:product_id>/

- don't need authentication

-**If everything goes right:** http status code: 201

> #### response body:
>
> ```
>   {
>     "id": 1,
>     "available": true,
>     "total_amount": 27,
>     "product_data": {
>       "id": 1,
>       "name": "refrigerante Coca Cola",
>       "category": "refrigerante",
>       "image": "image.jpg",
>       "price": 4.5,
>       "description": "refrigerante Coca Cola garrafa 2 litros"
>     }
>   }
> ```

- **If something went wrong:** http status code: 400
  > ```
  > {
  >   "message": "this product does not exist in inventory"
  > }
  > ```

### GET api/inventories/records/

- need authentication
- admin ou salesman acess

-**If everything goes right:** http status code: 201

> #### response body:
>
> ```
> [
>   {
>    "id": 1,
>    "amount": 30,
>    "transaction_type": "refuel",
>    "transaction_time": "2021-03-06T21:42:53.903503Z",
>    "product_data": {
>      "id": 1,
>      "name": "refrigerante Coca Cola",
>      "category": "refrigerante",
>      "image": "image.jpg",
>      "price": 4.5,
>      "description": "refrigerante Coca Cola garrafa 2 litros"
>     }
>   }
>   {
>    "id": 2,
>    "amount": 1,
>    "transaction_type": "sale",
>    "transaction_time": "2021-03-06T21:52:48.685782Z",
>    "product_data": {
>      "id": 1,
>      "name": "refrigerante Coca Cola",
>      "category": "refrigerante",
>      "image": "image.jpg",
>      "price": 4.5,
>      "description": "refrigerante Coca Cola garrafa 2 litros"
>    }
>   }
> ]
> ```

### PUT api/inventories/refuel/<int:product_id>/

- need authentication
- admin ou salesman acess

> #### request body:
>
> ```
> {
>     "amount": "20"
> }
> ```

-**If everything goes right:** http status code: 201

> #### response body:
>
> ```
>   {
>    "id": 1,
>    "amount": 30,
>    "transaction_type": "refuel",
>    "transaction_time": "2021-03-06T21:42:53.903503Z",
>    "product": 1
>  }
> ```

- **If something went wrong:** http status code: 400
  > ```
  > {
  >   "message": "does not have products in the inventory"
  > }
  > ```

### POST api/products/

- need authentication
- admin ou salesman acess

> #### request body:
>
> ```
> {
> 	"name": "refrigerante Coca",
> 	"price": 4.5,
> 	"description": "refrigerante Coca Cola garrafa 2 litros",
> 	"amount": 30,
> 	"image": "image.jpg",
> 	"category": "refrigerante"
> }
> ```

-**If everything goes right:** http status code: 201

> #### response body:
>
> ```
>   {
>    "id": 1,
>    "name": "refrigerante Coca",
>    "category": "refrigerante",
>    "image": "image.jpg",
>    "price": 4.5,
>    "description": "refrigerante Coca Cola garrafa 2 litros"
>  }
> ```

- **If something went wrong:** http status code: 400
  > ```
  > {
  >   "message": "It was not possible to create the product, try again"
  > }
  > ```
