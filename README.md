# Ekommerce

Use this URL as base to requests:

> `http://127.0.0.1:8000/`

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

### Status pode receber os seguintes valores:

- ENVIADO - para pedido enviado
- ENTREGUE - para pedido entregue
- CANCELADO - para pedido cancelado
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

### POST api/levels/

- Header -> Authorization: Token-admin

> #### request body:
>
> ```
> {
> 	"name": "floor 1",
> 	"fill_priority": 2,
> 	"bike_spots": 1,
> 	"car_spots": 2
> }
> ```

- **If everything goes right:** http status code: 201
  > #### response body:
  >
  > ```
  > {
  >   "id": 1,
  >   "name": "floor 1",
  >   "fill_priority": 2,
  >   "available_spots": {
  >     "available_bike_spots": 1,
  >     "available_car_spots": 2
  >   }
  > }
  > ```

### GET api/levels/

- **If everything goes right:** http status code: 200
  > #### response body:
  >
  > ```
  > [
  >   {
  >     "id": 1,
  >     "name": "floor 1",
  >     "fill_priority": 5,
  >     "available_spots": {
  >       "available_bike_spots": 20,
  >       "available_car_spots": 50
  >     }
  >   },
  >   {
  >     "id": 2,
  >     "name": "floor 2",
  >     "fill_priority": 3,
  >     "available_spots": {
  >       "available_bike_spots": 10,
  >       "available_car_spots": 30
  >     }
  >   }
  > ]
  > ```

### POST api/pricings/

- Header -> Authorization: Token-admin

> #### request body:
>
> ```
> {
> 	"a_coefficient": 100,
> 	"b_coefficient": 100
> }
> ```

- **If everything goes right:** http status code: 201
  > #### response body:
  >
  > ```
  > {
  >   "id": 1,
  >   "a_coefficient": 100,
  >   "b_coefficient": 100
  > }
  > ```

### POST api/vehicles/

- Header -> Authorization: Token-admin

> #### request body:
>
> ```
> {
> 	"vehicle_type": "car",
> 	"license_plate": "AYO1029"
> }
> ```

- **If everything goes right:** http status code: 201
  > #### response body:
  >
  > ```
  > {
  >   "id": 1,
  >   "license_plate": "AYO1029",
  >   "vehicle_type": "car",
  >   "arrived_at": "2021-01-25T17:16:25.727541Z",
  >   "paid_at": null,
  >   "amount_paid": null,
  >   "spot": {
  >     "id": 2,
  >     "variety": "car",
  >     "level_name": "floor 1"
  >   }
  > }
  > ```

### POST api/vehicles/<int:vehicle_id>/

- Header -> Authorization: Token-admin

- **If everything goes right:** http status code: 200
  > #### response body:
  >
  > ```
  > {
  >   "license_plate": "AYO1029",
  >   "vehicle_type": "car",
  >   "arrived_at": "2021-01-21T19:36:55.364610Z",
  >   "paid_at": "2021-01-21T19:37:23.016452Z",
  >   "amount_paid": 100,
  >   "spot": null
  > }
  > ```

>     {
>       "name": "product 2",
>       "price": 10.25,
>       "description": "product 2 test",
>       "image": "product2.png",
>       "category": "category prod 2"
>     }
>
> ],
> "client_id": 1
> }
>
> ```
>
> ```
